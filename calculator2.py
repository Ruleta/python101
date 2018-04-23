x = int(raw_input("Enter the value for x: "))
y = int(raw_input("Enter the value for y: "))

operation = raw_input("Choos opoeration: *, -, +, /")


if operation == "+":
    res_x_y = x + y
elif operation == "-":
    res_x_y = x-y
elif operation == "*":
    res_x_y = x * y
elif operation == "/":
    res_x_y = x / y
else:
    res_x_y = "Invalid operation!"


print res_x_y

