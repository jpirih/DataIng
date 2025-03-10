
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