

import sqlite3

db_name = 'test.db'
conn = sqlite3.connect(db_name)

cursor = conn.cursor()

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT
);
"""

CREATE_SECOND_TABLE = """CREATE TABLE IF NOT EXISTS users_info (
    user_id INTEGER NOT NULL,
    user_phone TEXT NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

INSERT = """INSERT INTO users (name, description)
VALUES 
    ('Den', 'Regular user'),
    ('Alex', 'Admin'),
    ('Ivan', 'New member');
"""