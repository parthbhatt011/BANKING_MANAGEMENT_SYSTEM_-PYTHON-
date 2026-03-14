from rich.console import Console
from rich.panel import Panel
from services.auth_service import login_user, register_user
from ui.dashboard import dashboard
from database.db_connection import get_connection

console = Console()


def login_screen():

    while True:

        console.clear()
        console.print(Panel("         BANKING MANAGEMENT SYSTEM      ", style="bold blue"))

        console.print("1. Login")
        console.print("2. Register")
        console.print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":

            email = input("Email: ")
            password = input("Password: ")

            try:
                user = login_user(email, password)
                console.print("[green]Login successful[/green]")
                dashboard(user)

            except Exception as e:
                console.print(f"[red]{e}[/red]")
                input("Press Enter to continue")

        elif choice == "2":

            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")

            try:
                register_user(name, email, password)
                console.print("[green]User registered successfully[/green]")
                input("Press Enter to continue")

            except Exception as e:
                console.print(f"[red]{e}[/red]")
                input("Press Enter to continue")

        elif choice == "3":
            break

        else:
            console.print("[red]Invalid option[/red]")
            input("Press Enter to continue")