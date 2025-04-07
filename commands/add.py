from data.storage import load_expenses, save_expenses, load_budget
from datetime import datetime

def add_expense(args):
    """
    Adds an expense to the list of expenses.
    """
    try:
        amount = float(args.amount)
        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return
    
    expenses = load_expenses()
    expense = {
        "id": len(expenses) + 1,
        "description": args.description,
        "amount": round(float(args.amount), 2),
        "category": args.category,
        "date": args.date or datetime.today().strftime('%Y-%m-%d')
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added.")

    month = expense['date'][:7]  # 'YYYY-MM'
    total = sum(e['amount'] for e in expenses if e['date'].startswith(month))
    budget = load_budget().get(month)

    if budget and total > budget:
        print(f"⚠️ Warning: Monthly budget of {budget}$ exceeded! Current: {total}$")

