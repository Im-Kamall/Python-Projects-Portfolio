class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = float(amount)

    def to_list(self):
        return [
            self.date,
            self.category,
            self.description,
            self.amount
        ]

    def __str__(self):
        return (
            f"{self.date} | "
            f"{self.category} | "
            f"{self.description} | "
            f"₹{self.amount:.2f}"
        )