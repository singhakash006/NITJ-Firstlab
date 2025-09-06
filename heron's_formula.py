import math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

s = (a+b+c)/2

ans = s*(s-a)*(s-b)*(s-c)
print(math.sqrt(ans))

