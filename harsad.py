num = int(input("enter number"))
sum = 0
temp = num
while temp>0:
    digit = temp % 10
    sum = sum + digit
    temp //=10
if num % sum == 0:
    print("it is harsad")
else:
    print("it is not")        