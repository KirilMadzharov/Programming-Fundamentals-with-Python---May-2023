phonebook = {}
command = input().split("-")

while len(command) > 1:
    current_key = command[0]
    current_value = command[1]
    phonebook[current_key] = current_value
    command = input().split("-")

searched_numbers = int(command[0])
for number in range(searched_numbers):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
