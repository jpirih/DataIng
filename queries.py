
query_all_books = """
SELECT * FROM  books
"""
query_all_authors = """
SELECT * FROM authors
"""

query_books_with_authors = """
    SELECT b.book_id,
           b.title,
           b.publication_date,
           a.first_name,
           a.last_name
    FROM books b
    JOIN authors a
      ON b.auth_id = a.auth_id
"""

query_books_by_author =  """
    SELECT b.book_id,
           b.title,
           b.publication_date,
           a.first_name,
           a.last_name
    FROM books b
    JOIN authors a
      ON b.auth_id = a.auth_id
    WHERE b.auth_id = {}
""".format(1)


# MSSQL QUERIES

query_all_customers = """
SELECT * FROM dbo.customers 
"""

query_all_orders = """
SELECT * FROM dbo.orders
"""

query_orders_with_customer_names = """
    SELECT c.customer_id,
           c.customer_name,
           c.city,
           o.order_id,
           o.order_date,
           o.amount
    FROM dbo.customers c
    JOIN dbo.orders o
      ON c.customer_id = o.customer_id
"""

query_orders_from_customer = """
SELECT c.customer_name,
       c.city,
       o.order_id,
       o.order_date,
       o.amount
FROM dbo.customers c
JOIN dbo.orders o 
  ON c.customer_id = o.customer_id
WHERE c.customer_id = {}
""". format(1)



