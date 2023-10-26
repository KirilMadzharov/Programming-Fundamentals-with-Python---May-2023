list_of_numbers = input().split()
reversed_list = []

for number in list_of_numbers:
    current_number = -int(number)
    reversed_list.append(current_number)

print(reversed_list)
