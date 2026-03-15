from rich.console import Console
from rich.panel import Panel
from ui.transaction_window import deposit_ui, withdraw_ui,showbalance_ui

console = Console()
def dashboard(user):
    while True:
        console.clear()
        console.print(Panel(f"Welcome {user['name']}", style="bold green"))
        console.print("1. Deposit Money")
        console.print("2. Withdraw Money")
        console.print("3. Show Balance")
        choice = input("Select option: ")
        if choice == "1":
            deposit_ui()
        elif choice == "2":
            withdraw_ui()
        elif choice == "3":
            showbalance_ui()
        elif choice == "4":
            break
        else:
            console.print("[red]Invalid option[/red]")
            input("Press Enter to continue")