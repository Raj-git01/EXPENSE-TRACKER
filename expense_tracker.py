import os


def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")


def save_expenses(expenses):
    try:
        with open("expenses.txt", "w") as file:
            for expense in expenses:
                file.write(f"{expense['description']},{expense['amount']}\n")
    except IOError:
        print("Error: Could not save expenses.")


def load_expenses():
    expenses = []

    if not os.path.exists("expenses.txt"):
        return expenses

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                description, amount = line.strip().split(",")
                expenses.append({
                    "description": description,
                    "amount": float(amount)
                })
    except (IOError, ValueError):
        print("Error: Could not load expenses.")

    return expenses


def add_expense(expenses):
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expenses.append({
        "description": description,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    print("\nExpenses:")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['description']} - ${expense['amount']:.2f}")
        total += expense["amount"]

    print(f"\nTotal spent: ${total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
