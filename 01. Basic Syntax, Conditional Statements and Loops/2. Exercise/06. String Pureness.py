number_of_strings = int(input())

for _ in range(number_of_strings):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(string, "is not pure!")
    else:
        print(string, "is pure.")
