import tkinter as tk
from database.db_connection import initialize_db
from ui.login_window import BankingApp


def main():
    initialize_db()

    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()