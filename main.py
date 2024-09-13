foods = []
prices = []
total = 0
x = 0

while True:
    food = input("Enter food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter price of {food}: "))
        prices.append(price)


print("\nShopping list:")
for x in range(len(foods)):
    print(f"{foods[x]:<25}: ${prices[x]:,.2f}")
    total += prices[x]

print()
print(f"Total: ${total:,.2f}")
