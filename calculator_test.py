from calculatorr import calculate

while True:
    operator = input("Enter an operator (+, -, *, /): ")
    first_value = int(input("Enter the first value: "))
    second_value = int(input("Enter the second value: "))

    result = calculate(operator, first_value, second_value)
    if result is not None:
        print(f"the result is {result}")
    else:
        print("No input specified. Please try again.")