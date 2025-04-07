from data.storage import load_budget, save_budget

def set_budget(args):
    budget = load_budget()
    month = args.month  # Format: YYYY-MM
    try:
        amount = float(args.amount)
    except ValueError:
        print("❌ Invalid amount.")
        return
    budget[month] = round(amount, 2)
    save_budget(budget)
    print(f"✅ Budget set for {month}: {budget[month]}$")
