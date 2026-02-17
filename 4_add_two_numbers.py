a= int(input("enter first value = "))
b = int(input("enter second value = "))
sum = int(a+b)
print(f"Your total sum of ({a}) + ({b}) = ({sum})")# this is the new method called as f-string
print("Your total sum of ({a}) + ({b}) = ({sum})")# this nothing do just simply print as it is .
print("Your total sum of ({}) + ({}) = ({})".format(a, b, sum))# this is the oldest method 