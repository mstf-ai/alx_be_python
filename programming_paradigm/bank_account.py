class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # خاص (encapsulated)

    def deposit(self, amount):
        """إضافة مبلغ إلى الرصيد"""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """سحب مبلغ إذا كان الرصيد كافياً"""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """عرض الرصيد الحالي"""
        print(f"Current Balance: ${self.__account_balance}")
