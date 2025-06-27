from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

# To run use uvicorn server:app --relocad

class Expense(BaseModel):
    amount: float
    category: str
    notes: str
    # It is used for data validation and also help us to return certain columns that is given in this class

class DateRange(BaseModel):
    start_date: date
    end_date : date
app = FastAPI()

@app.post("/insert/{expense_date}")
def insert_expenses(expense_date:date, expenses:List[Expense]):
    for expense in expenses:
        db_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)

    return {"message":"Expenses Inserted Successfully"}

@app.get("/expenses/{expense_date}")
def get_expenses(expense_date:date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses


@app.delete("/delete/{expense_id}")
def delete_expenses(expense_id:int):
    db_helper.delete_expenses_for_id(expense_id)
    print(f"Deleting ID: {expense_id}") 
    return f"Deleting ID: {expense_id}"

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data =db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from database")
    
    total = sum([row['total']for row in data])
    breakdown ={}
    for row in data:
        percentage = (row['total']/total)*100 if total!=0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown

@app.get("/analytics_month/{year}")
def get_analytics_month(year:int):
    data = db_helper.fetch_expense_summary_by_month(year)
    return data