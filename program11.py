num=int(input("Enter the number:"))
a=0
b=1
count=0
print("the febonacci serise is :" ,a ,b,end=' ')
while(num!=0):
    count=a+b
    a=b
    b=count
    print(count,end=" ")
    num-=1