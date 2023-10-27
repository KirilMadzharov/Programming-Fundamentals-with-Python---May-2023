net = 0
tax = 0
total = 0

while True:

    price = input()

    if price == "special" or price == "regular":
        break

    price = float(price)

    if price < 0:
        print("Invalid price!")
        continue

    net += price
    tax += price * 0.2
    total = net + tax

if total == 0:
    print("Invalid order!")

else:
    if price == "special":
        total *= 0.9

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")
