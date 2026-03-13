from db_connection import get_connection

def create_user(name,email,password_hash,role,created_at):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name,email,password_hash,role) VALUES(?,?,?,?)",(name, email, password_hash, role, created_at))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_account(user_id,account_type,created_at):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts(user_id,account_type,created_at) VALUES(?,?,?)",(user_id,account_type,created_at))
    conn.commit()
    conn.close()

def get_account(account_id):
    conn= get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,))
    account = cursor.fetchone()
    conn.close()
    return account

def update_balance(account_id,amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?",(amount, account_id))
    conn.commit()
    conn.close()

def create_transaction(account_id, type, amount, timestamp, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (account_id, type, amount, timestamp, description) VALUES (?, ?, ?, ?, ?)",(account_id, type, amount, timestamp, description))
    conn.commit()
    conn.close()