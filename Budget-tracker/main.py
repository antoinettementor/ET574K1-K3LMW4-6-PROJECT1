#Antoinette Mentor

# main.py

expenses = []

def add_expense():
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expenses.append({"name": name, "amount": amount})
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

def view_summary():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ${total:.2f}\n")

def view_all_expenses():
    if not expenses:
        print("\nNo expenses recorded.\n")
    else:
        print("\nAll Expenses:")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['name']} - ${exp['amount']:.2f}")
        print()

def main_menu():
    while True:
        print("=== Budget Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View All Expenses")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            view_all_expenses()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main_menu()

