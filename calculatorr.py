def calculate(operator, first_value, second_value):
    if operator == "+":
        result = first_value + second_value
        return result
        
    elif operator == "-":
        result = first_value - second_value
        return result
    elif operator == "*":
        result = first_value * second_value
        return result
    elif operator == "/":
        if second_value != 0:
            result = first_value / second_value
            return result
        else:
            print("Error: Division by zero is not allowed.")
