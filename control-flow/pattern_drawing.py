# pattern_drawing.py

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # الانتقال للسطر التالي
        row += 1

if __name__ == "__main__":
    main()
