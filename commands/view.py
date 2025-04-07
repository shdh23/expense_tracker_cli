from data.storage import load_expenses
def view_expenses(args):
    """
    View all expenses in the list.
    """
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    
    if args.category:
        expenses = [expense for expense in expenses if expense['category'] == args.category]
        if not expenses:
            print(f"No expenses found in category '{args.category}'.")
            return
    
    for expense in expenses:
        print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: ${expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")
    
