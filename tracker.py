import argparse
from commands.add import add_expense
from commands.view import view_expenses
from commands.update import update_expense
from commands.delete import delete_expense
from commands.summary import summary_by_month, summary
from commands.set_budget import set_budget
from commands.export import export_expenses

def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")
    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add', help='Add an expense')
    parser_add.add_argument('description', type=str, help='Description of the expense')
    parser_add.add_argument('amount', type=float, help='Amount of the expense')
    parser_add.add_argument('--category', type=str, help='Category of the expense')
    parser_add.add_argument('--date', type=str, help='Date of the expense (YYYY-MM-DD)')
    parser_add.set_defaults(func=add_expense)

    parser_view = subparsers.add_parser('view', help='View all expenses')
    parser_view.set_defaults(func=view_expenses)

    parser_view = subparsers.add_parser('view')
    parser_view.add_argument('--category', help="Filter by category")
    parser_view.set_defaults(func=view_expenses)


    parser_update = subparsers.add_parser('update', help='Update an expense')
    parser_update.add_argument('id', type=int, help='ID of the expense to update')
    parser_update.add_argument('--description', type=str, help='New description of the expense')
    parser_update.add_argument('--amount', type=float, help='New amount of the expense')
    parser_update.add_argument('--category', type=str, help='New category of the expense')
    parser_update.add_argument('--date', type=str, help='New date of the expense (YYYY-MM-DD)')
    parser_update.set_defaults(func=update_expense)
    
    parser_delete = subparsers.add_parser('delete', help='Delete an expense')
    parser_delete.add_argument('id', type=int, help='ID of the expense to delete')
    parser_delete.set_defaults(func=delete_expense)
    
    parser_summary = subparsers.add_parser('summary')
    parser_summary.set_defaults(func=summary)

    parser_summary_month = subparsers.add_parser('summary-month', help='Get summary of expenses for a month')
    parser_summary_month.add_argument('month', type=str, help='Month to summarize (MM)')
    parser_summary_month.set_defaults(func=summary_by_month)

    parser_budget = subparsers.add_parser('set-budget')
    parser_budget.add_argument('month', help='Format: YYYY-MM')
    parser_budget.add_argument('amount')
    parser_budget.set_defaults(func=set_budget)

    parser_export = subparsers.add_parser('export')
    parser_export.add_argument('--filename', help="Output CSV filename")
    parser_export.add_argument('--month', type=str, help="Month to export (MM)")
    parser_export.set_defaults(func=export_expenses)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()