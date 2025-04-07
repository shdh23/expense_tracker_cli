import json
import os
expenses_file = "expenses.json"
budget_file = 'data/budget.json'

def load_expenses():
    """
    Loads expenses from the JSON file.
    """
    try:
        with open(expenses_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Error: Could not decode JSON. Starting with an empty list.")
        return []

def save_expenses(expenses):
    """
    Saves expenses to the JSON file.
    """
    try:
        with open(expenses_file, "w") as file:
            json.dump(expenses, file, indent=4)
    except IOError as e:
        print(f"⚠️ Error: Could not save expenses to file. {e}")


def load_budget():
    if not os.path.exists(budget_file):
        return {}
    with open(budget_file, 'r') as f:
        return json.load(f)

def save_budget(budget):
    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=4)
