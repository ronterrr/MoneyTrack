import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns

console = Console()

def show_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold cyan]=== FINANCIAL OVERVIEW ===[/bold cyan]\n")

    # Metrics Summary Panels
    total_income = 5000.00
    total_expenses = 3200.00
    net_savings = total_income - total_expenses

    inc_panel = Panel(f"[bold green]${total_income:,.2f}[/bold green]", title="Total Income")
    exp_panel = Panel(f"[bold red]${total_expenses:,.2f}[/bold red]", title="Total Expenses")
    
    savings_color = "green" if net_savings >= 0 else "red"
    sav_panel = Panel(f"[bold {savings_color}]${net_savings:,.2f}[/bold {savings_color}]", title="Net Savings")

    console.print(Columns([inc_panel, exp_panel, sav_panel]))
    console.print("\n")

    # Recent Activity Table
    table = Table(title="Recent Activity", show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Type", width=10)
    table.add_column("Category", width=18)
    table.add_column("Amount", justify="right", width=12)

    sample_transactions = [
        {"date": "2026-09-01", "type": "Income", "category": "Salary", "amount": 5000.00},
        {"date": "2026-09-03", "type": "Expense", "category": "Housing", "amount": 1500.00},
        {"date": "2026-09-05", "type": "Expense", "category": "Food", "amount": 200.00},
    ]

    for tx in sample_transactions:
        if tx["type"] == "Income":
            amt_str = f"[green]+${tx['amount']:,.2f}[/green]"
        else:
            amt_str = f"[red]-${tx['amount']:,.2f}[/red]"
        
        table.add_row(tx["date"], tx["type"], tx["category"], amt_str)

    console.print(table)
    input("\nPress Enter to return to the main menu.")
   

if __name__ == "__main__":
    show_dashboard()
    