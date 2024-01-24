import sqlite3
from datetime import datetime
from database_queries import (
    create_user_query,
    get_users_query,
    get_user_query,
    get_user_by_telegram_id_query,
    get_user_by_username_query,
)


def create_user(telegram_id, username, first_name, last_name, language_code):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(
        create_user_query,
        (telegram_id, username, first_name, last_name, language_code, datetime.now()),
    )
    connection.commit()
    cursor.execute(get_user_by_telegram_id_query, (telegram_id))
    user_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_data


def get_users():
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(get_users_query)
    users_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return users_data


def get_user(id: int):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(get_user_query, (id))
    user_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_data


def get_user__by_telegram_id(telegram_id: int):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(get_user_by_telegram_id_query, (telegram_id))
    user_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_data


def get_user_by_username(username: str):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(get_user_by_username_query, (username))
    user_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_data


# create_user(123456, "username", "FirstName", "LastName", "en")
