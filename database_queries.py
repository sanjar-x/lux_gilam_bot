create_users_table_query = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER NOT NULL UNIQUE,
    username TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    language_code TEXT,
    is_admin INTEGER DEFAULT 0,
    is_operator INTEGER DEFAULT 0,
    started_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
create_user_query = """
    INSERT INTO users (telegram_id, username, first_name, last_name, language_code, started_date) 
    VALUES (?, ?, ?, ?, ?, ?)
    """
get_users_query = "SELECT * FROM users"
get_user_query = "SELECT * FROM users WHERE id = ?"
get_user_by_telegram_id_query = "SELECT * FROM users WHERE telegram_id = ?"
get_user_by_username_query = "SELECT * FROM users WHERE username = ?"
