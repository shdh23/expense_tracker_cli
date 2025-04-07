# 💸 Expense Tracker CLI

A simple command-line expense tracker to help you manage your finances.  
You can add, update, delete, view expenses, set monthly budgets, filter by category, and export data to CSV.

---

## 📦 Features

- ✅ Add expenses with description, amount, category, and date.
- 📝 Update or delete existing expenses by ID.
- 🔍 View all expenses or filter by category.
- 📊 View total summary or monthly summary of expenses.
- 💰 Set monthly budgets and get warnings when exceeded.
- 📁 Export all expenses to a CSV file.

---

## 🚀 Getting Started

### 📁 Clone the Repo
```sh
git clone https://github.com/shdh23/expense_tracker_cli.git
cd expense-tracker-cli
```

🐍 Run with Python 3
Make sure you have Python 3 installed.

🧰 Usage
Add an Expense
```sh
python tracker.py add "Groceries" 120 --category Food --date 2025-04-05
```

View All Expenses
```sh
python tracker.py view
```

Filter by Category
```sh
python tracker.py view --category Food
```

Update an Expense
```sh
python tracker.py update 1 --amount 1300 --description "Grocery Shopping"
```

Delete an Expense
```sh 
python tracker.py delete 2
```

View Total Summary
```sh
python tracker.py summary
```

View Monthly Summary
```sh
python tracker.py summary-month 04
```

Set Monthly Budget
```sh
python tracker.py set-budget 2025-04 5000
```

Export to CSV
```sh
python tracker.py export --filename my_expenses.csv
```

📂 Project Structure

expense-tracker-cli/
├── tracker.py                 # Main CLI entry point
├── data/
│   ├── storage.py             # Load/save expenses & budgets
│   ├── expenses.json          # Data storage
│   └── budget.json            # Monthly budget data
├── commands/
│   ├── add.py
│   ├── view.py
│   ├── update.py
│   ├── delete.py
│   ├── summary.py
│   ├── set_budget.py
│   └── export.py

✅ Validations
❌ Prevents adding expenses with negative or non-numeric amounts.

⚠️ Warns if monthly budget is exceeded after adding expenses.

❌ Prevents updating/deleting non-existent expense IDs.

Project idea: https://roadmap.sh/projects/expense-tracker