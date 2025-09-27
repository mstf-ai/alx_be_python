# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """عرض التاريخ والوقت الحالي"""
    current_date = datetime.now()  # حفظ التاريخ والوقت الحالي
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """حساب التاريخ بعد إضافة عدد معين من الأيام"""
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    # الجزء الأول: عرض التاريخ والوقت الحالي
    current_date = display_current_datetime()

    # الجزء الثاني: حساب تاريخ مستقبلي
    while True:
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
