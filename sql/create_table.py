import pymysql

# 🔹 Database connection details
username = "root"
password = "Krishna1@#$"   # replace with your MySQL password
host = "localhost"

# Connect to MySQL server
connection = pymysql.connect(
    host=host,
    user=username,
    password=password
)

cursor = connection.cursor()

cursor.execute("Create Database if not exists credit_fraud;")
cursor.execute("Use credit_fraud;")

create_table_query = """

CREATE TABLE IF NOT EXISTS transactions (
    Time INT,
    V1 DOUBLE,
    V2 DOUBLE,
    V3 DOUBLE,
    V4 DOUBLE,
    V5 DOUBLE,
    V6 DOUBLE,
    V7 DOUBLE,
    V8 DOUBLE,
    V9 DOUBLE,
    V10 DOUBLE,
    V11 DOUBLE,
    V12 DOUBLE,
    V13 DOUBLE,
    V14 DOUBLE,
    V15 DOUBLE,
    V16 DOUBLE,
    V17 DOUBLE,
    V18 DOUBLE,
    V19 DOUBLE,
    V20 DOUBLE,
    V21 DOUBLE,
    V22 DOUBLE,
    V23 DOUBLE,
    V24 DOUBLE,
    V25 DOUBLE,
    V26 DOUBLE,
    V27 DOUBLE,
    V28 DOUBLE,
    Amount DOUBLE,
    Class TINYINT
);
"""
cursor.execute(create_table_query)

connection.commit()
cursor.close()
connection.close()

print("Database and table created successfully")