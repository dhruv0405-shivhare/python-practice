num = int(input("enter number"))
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    cube = digit ** 3
    sum = sum + cube
    temp //=10
if num == sum:
    print("it is armstrong")         
else:
    print("it is not armstrong")    