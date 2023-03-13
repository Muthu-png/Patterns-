row = 0
col = 6
for i in range(0,4):
    # print("ganesh")
    for j in range(0,7):
        if j==i:
            print("*",end="")
        elif i==row and j==col:
            print("*",end=" ")
            row=row+1
            col=col-1
        else:
            print(end=" ")   
    print("")