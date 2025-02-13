num=int(input("Enter Number : "))
sum=0
while num>0:
    temp=num%10
    num=num//10
    sum+=temp
print("Sum of Digits : ", str(sum))