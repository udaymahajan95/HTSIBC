
print("Exchange the following two variables without using a third variable.")
print("Enter the first variable:")
first_var = int(input())  # Convert input to integer
print("Enter the second variable:")
second_var = int(input())  # Convert input to integer

# Swap without third variable using arithmetic
first_var = first_var + second_var
second_var = first_var - second_var
first_var = first_var - second_var

print(f"After the exchange of variables without using a third variable, the first variable is {first_var} and the second variable is {second_var}.")
