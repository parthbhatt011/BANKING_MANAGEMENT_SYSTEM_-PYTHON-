from database.db_connection import initialize_db
from ui.login_window import login_screen


def main():
    initialize_db()

    login_screen()


if __name__ == "__main__":
    main()