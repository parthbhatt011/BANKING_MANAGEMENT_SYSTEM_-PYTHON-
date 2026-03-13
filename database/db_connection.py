import sqlite3

database = "bank.db"

def get_connection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    #user table
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'customer',
        created_at TEXT NOT NULL
    )
    """)

    #Account table

    # Accounts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        balance REAL DEFAULT 0,
        account_type TEXT DEFAULT 'savings',
        created_at TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        timestamp TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY(account_id) REFERENCES accounts(account_id)
    )
    """)

    conn.commit()
    conn.close()