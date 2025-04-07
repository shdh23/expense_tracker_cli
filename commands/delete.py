from data.storage import load_expenses, save_expenses

def delete_expense(args):
    """
    Deletes an expense from the list of expenses.
    """
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    # Find the expense with the given ID
    expense_to_delete = next((expense for expense in expenses if expense['id'] == args.id), None)
    
    if not expense_to_delete:
        print(f"❌ No expense found with ID {args.id}.")
        return

    # Remove the expense from the list
    expenses.remove(expense_to_delete)
    
    # Save the updated list of expenses
    save_expenses(expenses)
    
    print(f"✅ Expense with ID {args.id} deleted.")