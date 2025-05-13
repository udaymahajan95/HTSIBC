def exchange(a,b):
    t = a
    a = b
    b = t
    print(f"After exchange, the first number is {a}  and second number is {b}")

print("Enter the two numbers to exchange their values.")
print("Enter the first number.")
num1 = input()
print("Enter the second number") 
num2 = input()
exchange(num1,num2)  
