create_users_table_query = """
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    telegram_id INTEGER NOT NULL UNIQUE,
    username TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    language_code TEXT,
    is_active INTEGER DEFAULT 1,
    is_admin INTEGER DEFAULT 0,
    is_operator INTEGER DEFAULT 0,
    started_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
drop_users_table_query = "DROP TABLE IF EXISTS users;"


create_country_table_query = """
CREATE TABLE countries (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""
drop_countries_table_query = "DROP TABLE IF EXISTS countries;"


create_collections_table_query = """
CREATE TABLE collections (
    id INTEGER PRIMARY KEY,
    name TEXT,
    cost DECIMAL(10, 2),
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)
"""
drop_collections_table_query = "DROP TABLE IF EXISTS collections;"


create_materials_table_query = """
CREATE TABLE materials (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""
drop_materials_table_query = "DROP TABLE IF EXISTS materials;"


create_styles_table_query = """
CREATE TABLE styles (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""
drop_styles_table_query = "DROP TABLE IF EXISTS styles;"


create_carpet_table_query = """
CREATE TABLE carpets (
    id INTEGER PRIMARY KEY,
    name TEXT,
    country_id INTEGER,
    collection_id INTEGER,
    material_id INTEGER,
    style_id INTEGER,
    form TEXT,
    colors INT,
    density INT,
    pile_height INT,
    height FLOAT,
    width FLOAT,
    FOREIGN KEY (country_id) REFERENCES countries(id)
    FOREIGN KEY (collection_id) REFERENCES collections(id),
    FOREIGN KEY (material_id) REFERENCES materials(id),
    FOREIGN KEY (style_id) REFERENCES styles(id)
)
"""
drop_carpets_table_query = "DROP TABLE IF EXISTS carpets;"


creat_tables_queries = [
    create_users_table_query,
    create_country_table_query,
    create_collections_table_query,
    create_materials_table_query,
    create_styles_table_query,
    create_carpet_table_query,
]
drop_tables_queries = [
    drop_users_table_query,
    drop_carpets_table_query,
    drop_collections_table_query,
    drop_countries_table_query,
    drop_styles_table_query,
    drop_materials_table_query,
]
