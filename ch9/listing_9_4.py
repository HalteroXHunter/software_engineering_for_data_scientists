import sqlite3
import pandas as pd

sqliteConnection = sqlite3.connect("data/customers.db")
cursor = sqliteConnection.cursor()

select_query = """SELECT * FROM
    customer_churn_predictions"""
cursor.execute(select_query)
customer_records = cursor.fetchall()
# print(customer_records)
cursor.close()

print(pd.read_sql("""SELECT *
    FROM customer_churn_predictions""",
    sqliteConnection))