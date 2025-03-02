num=int(input("Enter a number"))

rev=num%10
num=num//10
while(num>0):
    r=num%10
    num=num//10
    rev=rev*10+r
    
print(rev)