decimal=int(input("Enter Number : "))
if decimal==0:
    print(0)
else:
    binary=""
    while decimal>0:
        remainder=decimal%2
        decimal=decimal//2
        binary=str(remainder)+binary
    print(binary)