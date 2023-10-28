chars_string = input()
chars_dict = {}

for char in chars_string:

    if char != " ":

        if char not in chars_dict:
            chars_dict[char] = 0

        chars_dict[char] += 1

for key, value in chars_dict.items():
    print(f"{key} -> {value}")

