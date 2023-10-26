age = int(input())

this = ''
if age <= 14:
    this = "toddy"
elif age <= 18:
    this = "coke"
elif age <= 21:
    this = "beer"
else:
    this = "whisky"

print(f"drink {this}")
