import sys
import os
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
        elif action == 'Add Transaction':
            add_transaction_prompt()
        elif action == 'View Transactions':
            pass #handler for viewing transactions list
        elif action == 'Exit':
            console.print("[bold cyan]Bye[/bold cyan]")
            sys.exit(0)


def press_any_key():
    input("\nPress Enter to return to the main menu.")

if __name__ == "__main__":
    main_menu()