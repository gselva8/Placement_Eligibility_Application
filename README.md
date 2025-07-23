
# 🎓 Placement Eligibility App for (ED Tech)

This is a simple web application built with **Streamlit**, utilizing a dummy student dataset generated using the **Faker library**. It allows users to filter student data and extract insights based on defined eligibility criteria.

---

##  🖥️ How It Works 

- Generate fake student data using the **Faker** library
- Store and manage data in a **SQLite** database
- Use **OOP (Object-Oriented Programming)** in Python for clean structure
- Build a real-time, interactive web app using **Streamlit**
- Display SQL insights with **10 custom queries**
- **Download** filtered queries into .csv file

---

## 📌 What Does This App Do?

This app helps you:

- ✅ See how many students are **Placed** based on Eligibility
- 🔍 Find students who are **Ready for placement** but not yet placed
- 🔍 Find students who are **Not Ready for placement** based on Eligibility
- 📊 View detailed reports using built-in buttons

It’s built for **placement coordinators and mentors** to make the placement process easier and smarter.

## 🧰 Tools and Technologies Used

- Python 3.12
- Streamlit
- SQLite
- Faker

---

## 📁 Project Folder Structure

```
placement-eligibility-app/
│
├── README.md
│
├── app.py        # Main Streamlit app
│
├── placement.db  # SQLite DB from the notebook
│
└── Dataset_creation_and_storing.ipynb # Notebook for dataset creation
```

---

## 📊 SQL Insights Included

The application includes the following SQL insights:

1. Top 3 placed students and their CTC.
2. Second top programming student based on average programming score.
3. Students with good communication and weak programming.
4. Bottom 3 placed students and their CTC.
5. List of students who are not ready for placement.
6. Company that hired the most students.
7. Top 3 students with average (communication + project score) > 70%
8. Count of students placed.
9. Count of students ready for placement.
10. Count of students not ready.

---

## Developed by 

**SelvaKumaran G**  
Project Related to: **Data Science**  
Domain: **ED Tech**
---

