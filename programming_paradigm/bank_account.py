class BankAccount:
    def __init__(self, initial_balance=0):
        # استخدام اسم خاص (private attribute) لتطبيق مبدأ الكبسلة (encapsulation)
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """إضافة مبلغ إلى الرصيد"""
        self.__account_balance += amount

    def withdraw(self, amount):
        """سحب مبلغ من الرصيد إذا كان كافياً"""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """عرض الرصيد الحالي بتنسيق عشري دقيق"""
        print(f"Current Balance: ${self.__account_balance:.2f}")
