import csv
from data.storage import load_expenses
from datetime import datetime

def export_expenses(args):
    expenses = load_expenses()
    filename = args.filename or "expenses_export.csv"

    if args.month:
        try:
            month = args.month.zfill(2)
            if not (1 <= int(month) <= 12):
                print("❌ Invalid month. Please provide a valid month (01-12).")
                return
            year = str(datetime.now().year)
            expenses = [e for e in expenses if e['date'].startswith(f"{year}-{month}")]
        except ValueError:
            print("❌ Invalid month format. Please provide a valid month (01-12).")
            return
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "description", "amount", "category", "date"])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"✅ Expenses exported to {filename}")
    except Exception as e:
        print(f"❌ Error exporting to CSV: {e}")
