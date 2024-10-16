#variables
first_value = float(input("First number: "))
second_value = float(input("Second number: "))
unit = input("Select opperation(+,-,*,/,**)")

#if conditions

if unit == "+":
    print(first_value+second_value)
elif unit == "-":
    print(first_value-second_value)
elif unit == "*":
    print(first_value*second_value)
elif unit == "/":
    print(first_value/second_value)
elif unit == "**":
    print (first_value**second_value)
print ("Press any key to continue...")
#Code for exit 
if input():
    exit