first_character = ord(input())
second_character = ord(input())
sum_of_characters = 0
some_string = input()

for symbol in some_string:
    if first_character < ord(symbol) < second_character:
        sum_of_characters += ord(symbol)

print(sum_of_characters)
