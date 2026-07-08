value_1 = float(input("Enter the first value: "))
operator = input("Enter the operator (+, -, *, /): ")
value_2 = float(input("Enter the second value: "))

if operator == "+":
  print(f"Result: {value_1 + value_2}")

elif operator == "-":
  print(f"Result: {value_1 - value_2}")

elif operator == "*":
  print(f"Result: {value_1 * value_2}")

elif operator == "/":
  if value_2 == 0:
    print("Cannot divide by zero")
  else:
    print(f"Result: {value_1 / value_2}")

else:
  print("Invalid operator")
