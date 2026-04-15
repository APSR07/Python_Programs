num = int(input("enter a number  = "))
sum=0
i = num
remainder=0
while i>0:
    remainder=i%10
    sum += remainder
    i=i/10
print(f"the given number is {num} so the sum of their digit is {sum} ")
