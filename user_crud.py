import sqlite3
from datetime import datetime
from users_queries import (
    create_user_query,
    get_users_query,
    get_user_query,
    get_user_by_telegram_id_query,
    get_user_by_username_query,
    update_active_status_query,
    update_admin_status_query,
    update_operator_status_query,
)


def create_user(
    telegram_id: int, username: str, first_name: str, last_name: str, language_code: str
):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(
        create_user_query,
        (telegram_id, username, first_name, last_name, language_code),
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


def update_active_status(telegram_id, is_active: bool):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(update_active_status_query, (is_active, telegram_id))
    connection.commit()

    cursor.close()
    connection.close()


def update_admin_status(telegram_id, is_admin: bool):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(update_admin_status_query, (is_admin, telegram_id))
    connection.commit()

    cursor.close()
    connection.close()


def update_user_operator_status(telegram_id, is_operator: bool):
    connection = sqlite3.connect("luxgilam.db")
    cursor = connection.cursor()

    cursor.execute(update_operator_status_query, (is_operator, telegram_id))
    connection.commit()

    cursor.close()
    connection.close()


# create_user(123456, "username", "FirstName", "LastName", "en")
