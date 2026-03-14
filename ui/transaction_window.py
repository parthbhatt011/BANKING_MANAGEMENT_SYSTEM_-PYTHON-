from rich.console import Console
from services.transaction_service import deposit_money, withdraw_money

console = Console()

def deposit_ui():
    console.clear()
    console.print("=== Deposit Money ===")
    account_id = int(input("Account ID: "))
    amount = float(input("Amount: "))
    try:
        result = deposit_money(account_id, amount)
        console.print(f"[green]{result}[/green]")
    except Exception as e:
        console.print(f"[red]{e}[/red]")
    input("Press Enter to continue")

def withdraw_ui():
    console.clear()
    console.print("=== Withdraw Money ===")
    account_id = int(input("Account ID: "))
    amount = float(input("Amount: "))
    try:
        result = withdraw_money(account_id, amount)
        console.print(f"[green]{result}[/green]")
    except Exception as e:
        console.print(f"[red]{e}[/red]")
    input("Press Enter to continue")