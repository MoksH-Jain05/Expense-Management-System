import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper",'server.log')

@contextmanager   #it is special lib used to remove repition of code
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password = "root",
        database = "expense_manager"
    )

    if connection.is_connected():
        print("Connnection Successful")
    else:
        print("Failed in Connecting to a Database")

    cursor = connection.cursor(dictionary=True)
    yield cursor             # it will return cursor like generator do and below given statement will not be executed.
    if commit:
        connection.commit()      # whenenver a sub function come out from with these statement wil be executed
    cursor.close()
    connection.close()


def delete_expenses_for_id(expense_id):
    logger.info(f"delete_expenses_for_date called with {expense_id}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("Delete from expenses where id = %s",(expense_id,))
        

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses _for_data called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("Select * from expenses where expense_date = %s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expenses(expense_date,amount, category, notes):
    logger.info(f"insert_expenses called with date:{expense_date}, amount:{amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("Insert Into expenses (expense_date,amount,category,notes) values(%s,%s,%s,%s)",(expense_date,amount,category,notes))

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fetch expense_summary for start: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''Select category,sum(amount) as total from expenses where expense_date
        between %s and %s group by category
        ''',(start_date,end_date))
        expenses = cursor.fetchall()
        return expenses

def fetch_expense_summary_by_month(year):
    logger.info(f"fetch expense summary of month")
    with get_db_cursor() as cursor:
        cursor.execute('''select  month(expense_date) as month,
        monthname(expense_date) AS month_name,
        sum(amount) as total
        from expenses 
        where YEAR(expense_date) = %s
        group by month, month_name;''',(year,))
        expenses =cursor.fetchall()
        return expenses

if __name__ == "__main__":
    # expenses =fetch_expense_summary_by_month(2024)
    # for row in expenses:
    #     print(row)

    expenses = fetch_expenses_for_date("2025-06-25")
    print(expenses)
    insert_expenses("2025-06-25",500,"Food","chaat")
    expenses = fetch_expenses_for_date("2025-06-25")
    print(expenses)
    # pass


