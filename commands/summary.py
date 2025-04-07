from datetime import datetime
from data.storage import load_expenses

def summary(args):
    expenses = load_expenses()
    total = sum(e['amount'] for e in expenses)
    print(f"💰 Total Expenses: {total:.2f}$")

def summary_by_month(args):
    expenses = load_expenses()
    month = args.month.zfill(2)
    year = str(datetime.now().year)
    filtered = [e for e in expenses if e['date'].startswith(f"{year}-{month}")]
    total = sum(e['amount'] for e in filtered)
    print(f"📆 Summary for {year}-{month}: {total:.2f}$")
    if not filtered:
        print("No expenses found for this month.")
        return