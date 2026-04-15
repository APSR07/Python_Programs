fact = 1

ranges = int(input("Enter the range of factorial number = "))

for i in range (1, ranges+1):
    fact = fact * i

print("the factorial of given range is = ", fact)


# using while loop

whileFact = 1
i = 1

while(i <= ranges):
    whileFact = whileFact * i
    i = i+1

print("the factorial of given range is = ", whileFact)