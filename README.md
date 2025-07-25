#  Expense Management System

A full-stack personal expense tracking system built using **Streamlit** (frontend), **FastAPI** (backend), and **MySQL** (database). This app allows you to add, view, delete, and analyze expenses with a user-friendly interface and dynamic charts.

---

##  Features

-  Add multiple expenses per day with category and notes
-  View and manage expenses by date
-  Delete expenses (individually or in bulk)
-  Dashboard with pie charts and bar graphs
-  Monthly trend analysis with percent change from previous days
-  Clean UI with reset and auto-refresh logic

---

##  Tech Stack

| Layer      | Tool        |
|------------|-------------|
| Frontend   | Streamlit   |
| Backend    | FastAPI     |
| Database   | MySQL       |
| Visualization | pandas, matplotlib |

---

##  Folder Structure

```
project_expense_management/
│
├── Backend/
│   ├── server.py              # FastAPI main backend
│   ├── db_helper.py           # MySQL queries and DB logic
│   └── server.log             # Log output
│
├── Frontend/
│   ├── app.py                 # Streamlit main app
│   ├── insert.py              # Add expense tab
│   ├── view_manage.py         # View/Delete tab
│   ├── dashboard.py           # Dashboard analytics
│   ├── analytics.py           # API calls to analytics endpoint
│
├── requirements.txt           # Python dependencies
├── tests/                     # Test structure (pytest)
└── README.md                  # You're here
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/itsmoksh/Expense-Management-System.git
cd project_expense_management
```

### 2. Create Virtual Environment & Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup MySQL Database

- Create a database named `expense_db` (or your choice).
- Create the `expenses` table:

```sql
CREATE TABLE expenses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  expense_date DATE,
  amount DECIMAL(10,2),
  category VARCHAR(50),
  notes TEXT
);
```
- Update your MySQL credentials in `db_helper.py`

---

##  Running the Project

### 1. Start FastAPI Backend

```bash
cd Backend
uvicorn server:app --reload
```

### 2. Start Streamlit Frontend

```bash
cd ../Frontend
streamlit run app.py
```

---

##  Dashboard Preview

-  Pie chart: category-wise breakdown
-  Bar chart: month-wise spending
-  Metric: % change from previous day

---

##  TODO / Future Improvements

- Add user authentication
- Export filtered data as CSV/Excel
---

##  Author

**Moksh Jain**  
 [LinkedIn](https://www.linkedin.com/in/itsmoksh/)  
 [GitHub](https://github.com/MoksH-Jain05)

---

##  License

MIT License – free to use and modify.
