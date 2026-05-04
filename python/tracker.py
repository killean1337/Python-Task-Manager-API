import json
from transaction import Transaction


class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        for i, t in enumerate(self.transactions, 1):
            type_label = "Income" if t.is_income else "Expense"
            print(f"{i}. {type_label}: {t.amount} | {t.category} | {t.description}")

    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t.is_income:
                balance += t.amount
            else:
                balance -= t.amount
        return balance

    def save_to_file(self, filename="data.json"):
        with open(filename, "w") as file:
            json.dump([t.to_dict() for t in self.transactions], file, indent=4)