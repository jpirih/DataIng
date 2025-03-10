import os
from dotenv import load_dotenv
import pyodbc
import polars as pl
import pandas as pd
from queries import query_all_customers, query_all_orders, query_orders_with_customer_names, query_orders_from_customer

load_dotenv()

def set_connection_string():
    """Connect to MSSQL using env vars, return customers+orders as Polars DataFrame."""
    ms_host = os.getenv("J_MSSQL_HOST", "your_servew")
    ms_port = os.getenv("J_MSSQL_PORT", "1433")
    ms_db   = os.getenv("J_MSSQL_DB", "your_db")
    ms_user = os.getenv("J_MSSQL_USER", "username")
    ms_pass = os.getenv("J_MSSQL_PASSWORD", "")

    # Construct pyodbc connection string
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={ms_host},{ms_port};"
        f"DATABASE={ms_db};"
        f"UID={ms_user};"
        f"PWD={ms_pass};"
    )
    
    return conn_str


def fetch_mssql_data(conn_str, query):

    conn = pyodbc.connect(conn_str)
    df_ms_pandas = pd.read_sql(query, conn)
    conn.close()

    df_ms = pl.from_pandas(df_ms_pandas)
    return df_ms


conn_str = set_connection_string()

all_customers = fetch_mssql_data(conn_str, query_all_customers)
all_orders = fetch_mssql_data(conn_str, query_all_orders)
orders_with_customer_names = fetch_mssql_data(conn_str, query_orders_with_customer_names)

orders_by_first_customer = fetch_mssql_data(conn_str, query_orders_from_customer)

print("\nAll Customers from database")
print(all_customers)

print("\nAll Orders from database")
print(all_orders)

print("\nAll ordrs with customer names")
print(orders_with_customer_names)

print("\n All orders made by customer with id = 1")
print(orders_by_first_customer)