import sqlite3
from datetime import datetime
from database_queries import create_users_table_query


def create_tables():
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()
    cursor.execute(create_users_table_query)
    connection.commit()
    cursor.close()
    connection.close()


# connection.commit()
# cursor.execute()
# cursor.fetchone()
# cursor.fetchall()
# cursor.fetchmany()
# cursor.close()
# description = cursor.description
# rowcount = cursor.rowcount
