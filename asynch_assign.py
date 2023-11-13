def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            raise ValueError("Division by zero.")
    return result

def calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            if choice == '1':
                numbers = [float(num) for num in input("Enter numbers separated by spaces: ").split()]
            elif choice in ['2', '3', '4']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            else:
                print("Error: Invalid choice. Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Error: Invalid input. Please enter numerical values.")
            continue

        if choice == '1':
            result = add(numbers)
        elif choice == '2':
            result = subtract([num1, num2])
        elif choice == '3':
            result = multiply([num1, num2])
        elif choice == '4':
            try:
                result = divide([num1, num2])
            except ValueError as e:
                print(f"Error: {str(e)}")
                continue

        print("Result: {:.2f}".format(result))

if __name__ == "__main__":
    calculator()
