from enum import Enum

# enum
class TipeEnum(str, Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    PURCHASE = "PURCHASE"
    INVESTMENT = "INVESTMENT"