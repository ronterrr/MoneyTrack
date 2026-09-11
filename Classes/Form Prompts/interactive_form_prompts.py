import re
from datetime import datetime
import inquirer

def validate_amount(_, current):
    try:
        val = float(current)
        if val > 0:
            return True
        raise Exception()
    except Exception:
        raise inquirer.errors.ValidationError('', reason='Please enter a valid positive number.')

def validate_date(_, current):
    if re.match(r"^\d{4}-\d{2}-\d{2}$", current):
        try:
            datetime.strptime(current, "%Y-%m-%d")
            return True
        except ValueError:
            pass
    raise inquirer.errors.ValidationError('', reason="Use YYYY-MM-DD format.")

def get_categories(answers):
    if answers.get('type') == 'Income':
        return ['Salary', 'Freelance', 'Investments', 'Other']
    return ['Housing', 'Food', 'Transport', 'Utilities', 'Entertainment']

def add_transaction_prompt():
    questions = [
        inquirer.List(
            'type',
            message="Transaction Type",
            choices=['Expense', 'Income']
        ),
        inquirer.Text(
            'amount',
            message="Amount ($)",
            validate=validate_amount
        ),
        inquirer.List(
            'category',
            message="Category",
            choices=get_categories
        ),
        inquirer.Text(
            'date',
            message="Date (YYYY-MM-DD)",
            default=datetime.now().strftime("%Y-%m-%d"),
            validate=validate_date
        ),
        inquirer.Text(
            'note',
            message="Note (optional)"
        )
    ]

    answers = inquirer.prompt(questions)
    if answers:
        answers['amount'] = float(answers['amount'])
        # Save transaction logic here
        print("\nTransaction saved successfully!")

def press_any_key():
    input('\nPress Enter to return to the main menu.')

if __name__ == "__main__":
    add_transaction_prompt()
    press_any_key()
