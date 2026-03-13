from database import *
from database.db_connection import initialize_db


def main():
    initialize_db()
    print("Banking System Started")

if __name__ == "__main__":
    main()