from tracker import ExpenseTracker
from transaction import Transaction


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Transactions")
        print("4. Show Balance")
        print("5. Save")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1" or choice == "2":
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")

            tracker.add_transaction(
                Transaction(
                    amount,
                    category,
                    description,
                    is_income=(choice == "1")
                )
            )

        elif choice == "3":
            tracker.show_transactions()

        elif choice == "4":
            print(f"Current Balance: {tracker.get_balance()}")

        elif choice == "5":
            tracker.save_to_file()
            print("Saved successfully.")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()