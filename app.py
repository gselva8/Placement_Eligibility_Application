# Import necessary libraries

import streamlit as st 
import sqlite3
import pandas as pd

# Background color using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1C3948;
    }
    [data-testid="stSidebar"] {
        background-color: #E68C3A; 
    }
    </style>
    """,
    unsafe_allow_html=True
)


# setting a wide UI page in Streamlit
st.set_page_config(layout="wide")
conn = sqlite3.connect('placement.db') # connceting with the SQLite db
cursor = conn.cursor()

# Sidebar for page selection
page = st.sidebar.radio(
    "🎯 Select page",
    ("Placement Eligibility Filter", "Top 10 Insights")
)

# Task 1: filter eligible students and show it dynamically.
if page == "Placement Eligibility Filter":


    st.title("📚ED Tech - Placement Eligibility Filter")
    st.markdown("### 📝Set the eligibility criteria using the filters below:")

    problems_min = st.slider("Min Problems Solved", 0, 100, 50)
    communication_min = st.slider("Min Communication Score", 0, 100, 75)
    mock_interview_score = st.slider("Mock Interview Scores", 0, 100, 60)
    placement_status = st.selectbox("Placement Status", ["Any", "Ready", "Not Ready", "Placed"])


    query = f"""
    SELECT s.student_id, s.name, p.problems_solved, ss.communication, pl.placement_status
    FROM Students s
    JOIN Programming p ON s.student_id = p.student_id
    JOIN SoftSkills ss ON s.student_id = ss.student_id
    JOIN Placements pl ON s.student_id = pl.student_id
    WHERE p.problems_solved >= {problems_min}
    AND pl.mock_interview_score >= {mock_interview_score}
    AND ss.communication >= {communication_min}
    """

    if placement_status != "Any":
        query += f" AND pl.placement_status = '{placement_status}'"

    df = pd.read_sql_query(query, conn)
    st.subheader("Eligible Students")
    st.dataframe(df)

    # below the data frame


# Taks 2: Providing Good Insights about the Dataset using 10 qeuries: 
elif page == "Top 10 Insights":
    st.title("📊Top Actionable insights from the Stored Data")

    # 1. Top 3 placed students and their CTC.
    st.markdown("### 1. Top 3 Placed Students and Their CTC")
    query1 = """
    SELECT s.name, p.placement_package
    FROM Students s
    JOIN Placements p ON s.student_id = p.student_id
    WHERE p.placement_status = 'Placed'
    ORDER BY p.placement_package DESC
    LIMIT 3
    """
    df1 = pd.read_sql_query(query1, conn)
    st.dataframe(df1)

    # 2. Second top student based on average of Programming Table details 
    st.markdown("### 2. Second Top Student by Average Programming Score")
    query2 = """
    SELECT s.name, p.student_id,
    (p.problems_solved + p.assessments_completed + p.mini_projects + 
    p.certifications_earned + p.latest_project_score) / 5.0 AS avg_programming_score
    FROM Programming p
    JOIN Students s ON p.student_id = s.student_id
    ORDER BY avg_programming_score DESC
    LIMIT 1 OFFSET 1
    """
    df2 = pd.read_sql_query(query2, conn)
    st.dataframe(df2)

    # 3. Select all students who have good communication (>70), weak in programming (50 - 70)
    st.markdown('### 3. Students who have good communication, weak in programming')
    query3 = """
    SELECT s.name, p.problems_solved, ss.communication
    FROM Students s
    JOIN Programming p ON s.student_id = p.student_id
    JOIN SoftSkills ss ON s.student_id = ss.student_id
    WHERE ss.communication > 70
      AND p.problems_solved BETWEEN 50 AND 70
    """
    df3 = pd.read_sql_query(query3, conn)
    st.dataframe(df3)

    # 4. bottom 3 placed students and their CTC.
    st.markdown("### 4. Bottom 3 Placed Students and Their CTC")
    query4 = """
    SELECT s.name, p.placement_package
    FROM Students s
    JOIN Placements p ON s.student_id = p.student_id
    WHERE p.placement_status = 'Placed'
    ORDER BY p.placement_package ASC
    LIMIT 3
    """
    df4 = pd.read_sql_query(query4, conn)
    st.dataframe(df4)

    # 5. Students who're not ready for placement.
    st.markdown("### 5. Students Who Are Not Placed")
    query5 = """
    SELECT s.name, p.placement_status
    FROM Students s
    JOIN Placements p ON s.student_id = p.student_id
    WHERE p.placement_status = 'Not Ready'
    """
    df5 = pd.read_sql_query(query5, conn)
    st.dataframe(df5)

    # 6. Of the placed students, which company hired the most placed students.
    st.markdown("### 6. Company That Hired the Most Students")
    query6 = """
    SELECT company_name, COUNT(*) AS hired_count
    FROM Placements
    WHERE placement_status = 'Placed'
    AND company_name IS NOT NULL
    GROUP BY company_name
    ORDER BY hired_count DESC
    LIMIT 1
    """
    df6 = pd.read_sql_query(query6, conn)
    st.dataframe(df6)

    # 7. Select top 3 students whose average of (programming score combined with communication skills) > 70%
    st.markdown("### 7. Top 3 Students by Average Programming and Communication more than 70%")
    query7 = """
    SELECT s.name,
        p.latest_project_score,
        ss.communication,
        (p.latest_project_score + ss.communication) / 2.0 AS avg_score
    FROM Students s
    JOIN Programming p ON s.student_id = p.student_id
    JOIN SoftSkills ss ON s.student_id = ss.student_id
    WHERE (p.latest_project_score + ss.communication) / 2.0 > 70
    ORDER BY avg_score DESC
    LIMIT 3
    """
    df7 = pd.read_sql_query(query7, conn)
    st.dataframe(df7)

    # 8. Count of students who got placed
    st.markdown("### 8. Students Who Are Placed")
    query8 = """
    SELECT s.name, p.placement_status
    FROM Students s
    JOIN Placements p ON s.student_id = p.student_id
    WHERE p.placement_status = 'Placed'
    """
    df8 = pd.read_sql_query(query8, conn)
    st.dataframe(df8)

    # 9. count of students who are ready for placements.
    st.markdown("### 9. Count of Students Who Are Ready for Placements")
    query9 = """   
    SELECT COUNT(*) AS Ready_for_Placement
    FROM Placements
    WHERE placement_status = 'Ready'
    """
    df9 = pd.read_sql_query(query9, conn)
    st.dataframe(df9)

    # 10. Count of students who are not ready for placements.
    st.markdown("### 10. Count of Students Who Are Not Ready for Placements")
    query10 = """
    SELECT COUNT(*) AS Not_ready_for_Placement
    FROM Placements
    WHERE placement_status = 'Not Ready'
    """
    df10 = pd.read_sql_query(query10, conn)
    st.dataframe(df10)

    # Closing the database connection
    conn.close()



