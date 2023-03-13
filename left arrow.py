n = int(input("enter the number of rows : "))

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print("")  
for i in range(n+1):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range(5-i+1):
        print("*",end=" ")
    print(" ")                  
          