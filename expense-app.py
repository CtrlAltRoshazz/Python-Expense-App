import json
from datetime import datetime

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def add_expense(expenses, amount, category, description):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expenses.append({'date': date, 'amount': amount, 'category': category, 'description': description})
    save_expenses(expenses)
    print("Expense added successfully.")

def categorize_expenses(expenses):
    categories = set(expense['category'] for expense in expenses)
    print("Available categories:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

def view_spending_patterns(expenses):
    print("\nSpending Patterns:")
    total_expenses = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total_expenses:.2f}")

    # Group expenses by category
    category_expenses = {}
    for expense in expenses:
        category = expense['category']
        category_expenses[category] = category_expenses.get(category, 0) + expense['amount']

    # Display spending for each category
    for category, amount in category_expenses.items():
        print(f"{category}: ${amount:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. Categorize Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter a description: ")
            add_expense(expenses, amount, category, description)
        elif choice == '2':
            categorize_expenses(expenses)
        elif choice == '3':
            view_spending_patterns(expenses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
