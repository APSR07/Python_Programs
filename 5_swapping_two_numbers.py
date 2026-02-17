a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))

a=a+b
b=a-b
a=a-b
print(f"after swapping your value of a = ({a}) and b = ({b})")

# Another approach for swapping two number but this approach is only valid for python
# a, b = b, a
# print(a, b)