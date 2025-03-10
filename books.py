import os
from dotenv import load_dotenv
import psycopg2
import pyodbc
import polars as pl
import pandas as pd

from queries import query_all_books, query_all_authors, query_books_with_authors ,query_books_by_author


pg_host = os.getenv("J_POSTGRES_HOST", "your_pg_host")
pg_port = os.getenv("J_POSTGRES_PORT", "5432")
pg_db   = os.getenv("J_POSTGRES_DB", "testko")
pg_user = os.getenv("J_POSTGRES_USER", "username")
pg_pass = os.getenv("J_POSTGRES_PASSWORD", "password")

def  pg_db_connect() -> psycopg2.connect:
    pg_host = os.getenv("J_POSTGRES_HOST", "your_pg_host")
    pg_port = os.getenv("J_POSTGRES_PORT", "5432")
    pg_db   = os.getenv("J_POSTGRES_DB", "testko")
    pg_user = os.getenv("J_POSTGRES_USER", "username")
    pg_pass = os.getenv("J_POSTGRES_PASSWORD", "password")

    conn = psycopg2.connect(
        host=pg_host,
        port=pg_port,
        dbname=pg_db,
        user=pg_user,
        password=pg_pass
    )
    
    return conn

def get_data_from_db(query: str, conn: psycopg2.connect) -> pd.DataFrame:
    """queryes postgresql datgabase and returns dataframe"""
    df_queryed_data = pd.read_sql(query, conn)
    return df_queryed_data
    

conn = pg_db_connect()

try:
    cursor = conn.cursor()
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print("Error connecting to PostgreSQL:", e)
    
    

#prints books
df_books = get_data_from_db(query_all_books, conn)
print(df_books)

# print all authors
df_authors = get_data_from_db(query_all_authors, conn)
print(df_authors)

df_books_with_authors = get_data_from_db(query_books_with_authors, conn)
print("\nBooks with names of authors")
print(df_books_with_authors)

df_books_by_auth = get_data_from_db(query_books_by_author, conn)
print("\nBooks by Al Stewart")
print(df_books_by_auth)

conn.close()

