a=int(input("Enter start:"))
b=int(input("Enter end:"))
for i in range(a,b + 1):
  if all(int(d)%2==0 for d in str(i)):
   print(i)
