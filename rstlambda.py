square = lambda a: a * a
rectangle = lambda l,b: l * br
triangle = lambda b, h: 1/2 * b * h

a = float(input("enter a side of square:"))
br = float(input("enter a breadth of rectangle:"))
l = float(input("enter a length of rectangle:"))
b = float(input("enter a base of traingle:"))
h = float(input("enter a height of traingle:"))

print("area of rectangle:", rectangle(l,br))
print("area of square:", square(a))
print("area of triangle:", triangle(b,h))

