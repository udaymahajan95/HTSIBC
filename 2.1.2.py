def exchange_three_values(a,b,c):
    t = a
    a = c
    c = b 
    b = t
    print(f"After exchange, the first number is {a}, the second number is {b}, and the third number is {c}.")

print("Enter the three numbers to exchange their values.")
print("Enter the first number.")
a = input()
print("Enter teh seond number,")
b = input()
print("Enter the third number.")
c = input()
exchange_three_values(a,b,c)
