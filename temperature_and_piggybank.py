fahrenheit = float(input("Enter a degree fahrenheit: "))

celsius = (fahrenheit -32)* (5/9)
print(f"Temperature in degree celsius is : {format(celsius, ".3f")} ")



t = int(input("Enter number of 10 Rs"))
f = int(input("Enter number of 5 Rs"))
two = int(input("Enter number of 2 Rs"))
one = int(input("Enter number of 1 Rs"))

print("Bank Balance : ", t*10 + f*5 + two*2 + one)