class Transaction:
    def __init__(self, amount, category, description, is_income):
        self.amount = amount
        self.category = category
        self.description = description
        self.is_income = is_income

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "is_income": self.is_income
        }