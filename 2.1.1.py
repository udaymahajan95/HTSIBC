def exchange_drink(glass_A, glass_B):

    glass_T = glass_A
    glass_A = glass_B
    glass_B = glass_T
    print(f"After exchanging, glass A has '{glass_A}' and glass B has '{glass_B}'.")

glass_A = "Raspberry Drink"
glass_B = "Lemonade Drink"

exchange_drink(glass_A, glass_B)