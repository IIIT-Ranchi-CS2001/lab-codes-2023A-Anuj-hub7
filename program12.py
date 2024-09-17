num=int(input("Enter the number :"))
print("the multiplication table :")
for i in range(1,num+1):
    for j in range(1,num+1):
        print(i*j,end="   ")
    print()    
