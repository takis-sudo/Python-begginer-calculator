first_value = float(input("First number: "))
operation = input("Choose operation(+,-,*,**,root)")

if operation == "root":
    print(first_value**0.5)
elif operation == "+":
    second_value = float(input("Second number: "))
    print(first_value+second_value)
elif operation == "-":
    second_value = float(input("Second number: "))
    print(first_value-second_value)
elif operation == "*":
    second_value = float(input("Second number: "))
    print (first_value*second_value)
elif operation == "**":
    power = float(input("Power of: "))
    print(first_value**power)

print ("Press any key to continue...")
if input():
    exit