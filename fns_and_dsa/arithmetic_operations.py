def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        return "Error: Invalid operation"
    
print(perform_operation(20, 4, "add"))
print(perform_operation(7, 3, "subtract"))
print(perform_operation(6, 8, "multiply"))
print(perform_operation(75, 15, "divide"))
