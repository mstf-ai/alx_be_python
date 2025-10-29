def safe_divide(numerator, denominator):
    try:
        # نحاول تحويل القيم إلى أعداد عشرية
        num = float(numerator)
        den = float(denominator)

        # نحاول إجراء القسمة
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
