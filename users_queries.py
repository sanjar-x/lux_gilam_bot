create_user_query = """
    INSERT INTO users (telegram_id, username, first_name, last_name, language_code) 
    VALUES (?, ?, ?, ?, ?)
    """
get_users_query = "SELECT * FROM users"
get_user_query = "SELECT * FROM users WHERE id = ?"
get_user_by_telegram_id_query = "SELECT * FROM users WHERE telegram_id = ?"
get_user_by_username_query = "SELECT * FROM users WHERE username = ?"

update_active_status_query = """
    UPDATE users
    SET is_active = ?
    WHERE telegram_id = ?
"""
update_admin_status_query = """
    UPDATE users
    SET is_admin = ?
    WHERE telegram_id = ?
"""
update_operator_status_query = """
    UPDATE users
    SET is_operator = ?
    WHERE telegram_id = ?
"""
