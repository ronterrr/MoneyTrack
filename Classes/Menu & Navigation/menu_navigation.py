import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Classes.database import get_transactions_by_type, get_monthly_summary, add_transaction_prompt, show_dashboard
import inquirer
from rich.console import Console

console = Console()

def main_menu():
    while True:
        #an infinite loop to keep the menu running until the user chooses to exit
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
        console.print("[bold cyan]=== MONEYTRACK (Personal Finance CLI) ===[/bold cyan]\n")

        questions = [
            inquirer.List(
            'action',
            message = "Select an option:",
            choices=[
                'View Dashboard',
                'Add Transaction',
                'View Transactions',
                'Monthly Summary',
                'Exit'
            ],
            ),
        ]

        answers = inquirer.prompt(questions)
        if not answers:
            sys.exit(0)  # Exit if the user cancels the prompt

        action = answers['action']
        if action == 'View Dashboard':
            show_dashboard()
            press_any_key()
        elif action == 'Add Transaction':
            add_transaction_prompt()
        elif action == 'View Transactions':
            filter_type = input("Filter by type (Income/Expense): ")
            results = get_transactions_by_type(filter_type)
            for r in results:
                print(r)
            press_any_key()
        elif action == 'Monthly Summary':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g. 2023): "))
            summary = get_monthly_summary(month, year)
            for transaction_type, total in summary:
                print(f"{transaction_type}: {total}")
            press_any_key()
        elif action == 'Exit':
            console.print("[bold cyan]Bye[/bold cyan]")
            sys.exit(0)


def press_any_key():
    input("\nPress Enter to return to the main menu.")

if __name__ == "__main__":
    main_menu()