import sqlite3
from tables_queries import creat_tables_queries, drop_tables_queries


def create_all_tables():
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()
    for query in creat_tables_queries:
        cursor.execute(query)
        connection.commit()
    cursor.close()
    connection.close()


def reset_database():
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()
    for query in drop_tables_queries:
        cursor.execute(query)
        connection.commit()
    for query in creat_tables_queries:
        cursor.execute(query)
        connection.commit()
    cursor.close()
    connection.close()


reset_database()

# connection.commit()
# cursor.execute()
# cursor.fetchone()
# cursor.fetchall()
# cursor.fetchmany()
# cursor.close()
# description = cursor.description
# rowcount = cursor.rowcount
