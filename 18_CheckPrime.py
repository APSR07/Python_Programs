num = int(input("enter a number for checking prime or not = "))
flag = 0

for i in range(2, num+1):
    if(num % i == 0):
        flag = flag + 1
    
if(flag == 1):
    print("the number is prime")

else:
    print("not prime")