from data.storage import load_expenses

def update_expense(args):
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    
    # Find the expense with the given ID
    expense_to_update = next((expense for expense in expenses if expense['id'] == args.id), None)
    if not expense_to_update:
        print(f"❌ No expense found with ID {args.id}.")
        return
    
    # Update the expense details
    if args.description: expense_to_update['description'] = args.description
    if args.amount: expense_to_update['amount'] = round(float(args.amount), 2)
    if args.category: expense_to_update['category'] = args.category
    if args.date: expense_to_update['date'] = args.date
