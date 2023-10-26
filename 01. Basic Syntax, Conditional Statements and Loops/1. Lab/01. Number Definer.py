number = float(input())

if number == 0:
    print("zero")

if number > 1000000:
    print("large positive")
elif 0 < number < 1:
    print("small positive")
elif 1 < number < 1000000:
    print("positive")

if number < -1000000:
    print("large negative")
elif 0 > number > -1:
    print("small negative")
elif number < -1:
    print("negative")

