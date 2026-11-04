a = input("Enter first string: ")
b = input("Enter second string: ")

a, b = b[0] + a[1:], a[0] + b[1:]

print("swapped=",a + " " + b)
