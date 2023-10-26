n = int(input())

total = 0
for order in range(n):
    capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    order_sum = capsule * days * capsules_needed
    if 0.01 <= capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_needed <= 2000:
        total += order_sum
        print(f"The price for the coffee is: ${order_sum:.2f}")
print(f"Total: ${total:.2f}")