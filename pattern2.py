lim=int(input("Enter the limit:"))
for row in range(1, lim + 1):
 for colm in range(row, lim + 1):
    print(" ",end=" ")
 for colm in range(1, row + 1):
         print("*", end=" ")
 print()
