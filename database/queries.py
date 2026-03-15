from database.db_connection import get_connection

def create_user(name,email,password_hash,role,created_at):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name,email,password_hash,role,created_at) VALUES(?,?,?,?,?)",(name, email, password_hash, role, created_at))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def show_account(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Account Details:")
        print("user id: "), user["user_id"]
        print("Email:", user["email"])
        print("Account No:", user["account_id"])
        print("Created at:", user["created_at"])
    else:
        print("User not found")

def create_account(email,user_id,account,created_at):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts(email,user_id,account_id,created_at) VALUES(?,?,?,?)",(email,user_id,account,created_at))
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

def show_balance(account_id):
    conn= get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
       return user["balance"]
    else:
        print("User not found")