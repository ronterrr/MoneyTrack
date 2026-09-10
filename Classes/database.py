import sqlite3
conn = sqlite3.connect("moneytrack.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT
    )
""")
conn.commit()

conn.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")
conn.commit()

conn.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        amount REAL,
        type TEXT,
        description TEXT,
        date TEXT,
        account_id INTEGER,
        category_id INTEGER
    )
""")
conn.commit()


def get_transactions_by_type(transaction_type):
    cursor = conn.execute("SELECT * FROM transactions WHERE type = ?", (transaction_type,))
    return cursor.fetchall()

def get_monthly_summary(month, year):
    date_prefix = f"{year}-{month:02d}"
    cursor = conn.execute("""
        SELECT type, SUM(amount) FROM transactions
        WHERE date LIKE ?
        GROUP BY type
    """, (date_prefix + "%",))
    return cursor.fetchall()


def add_transaction_prompt():
    print("\n--- Add New Transaction ---")
    try:
        amount = float(input("Enter amount: "))
        transaction_type = input("Enter type (income/expense): ").strip().lower()
        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD): ").strip()
        account_id = int(input("Enter account ID: "))
        category_id = int(input("Enter category ID: "))

        conn.execute(
            """
                INSERT INTO transactions (amount, type, description, date, account_id, category_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
            (amount, transaction_type, description, date, account_id, category_id)
        )
        conn.commit()

        print("Transaction added successfully!")
    except ValueError:
        print("Invalid input. Please ensure numbers are used for amounts and IDs, and dates follow YYYY-MM-DD")