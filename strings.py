
from decimal import Decimal


a = "Good' + 'Morning"
b = "python" + "Technology"
print(len(a))
print(b)
c= "Python" + "3.5"
print(c)
d = "12" + "34"
print(d)

print("good "*5) # string repetition
# print("good "* "5") 
#print("good "* 5.0)

str = "Python is Easy!!!"
print(str)
print(str[0])
print(str[3 : 9])
print(str[4:])
print(str * 2)
print(str[-1 ])
print(str[:5])
print("What's Your name?")
print('What\'s Your name?')
print("The boy replies,\"My name is Aaditya.\"")
print("The boy replies,\"\nMy name is Aaditya.\"")
print("The boy replies,\"\tMy name is Aaditya.\"")
print("The boy replies,\ My name is Aaditya.")

print("*************Escape Sequences*************")
print("\\")
print("\'")
print("\"")
print("Hello\nWorld")
print("Hello\tWorld")
print("\056")
print("\x2E")
print("\x87")

print("**********Conversion***********")
print(int(0b11011))
print(oct(51))
print(int(0x360))
print(hex(51))
print(int(0x33))

# print(3<<2) left shift
# print(42>>2) right shift

x = [1,2]
y= [1,2]
z=x
print("x is z:" ,x is z)

x1 = 5
y1=5
x2 ="Hello"
y2 = "Hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1)
print(x2 is  y2)
print(x3 is y3)

print("******Membership Operators******")
#in not in


# check if 'H' is present in a message

message = "HELLO WORLD"
print('H' in message  )
print('HELLO' in message  )
print("hello" in message)

dict = {1 : 'a', 2 : 'b'}

print(1 in dict)
print('a' in dict.values())

# Ternary Operator
a, b = 10, 20
min = a if a<b else b
print(min)


x = 5

print("Positive" if x > 0 else "Negative")
x = -5
print("Positive" if x > 0 else "Negative")
x = 0.5
print("Positive" if x > 0 else "Negative")

expr = 10 +20*30
print(expr)

print((40+20)*30/10)
print(40+(20*30)/10)

print(False == False or True)
print(False == (False or True))
print(100/10*10)