word = input()
lowercase_word = word.lower()

sand = lowercase_word.count('sand')
water = lowercase_word.count('water')
fish = lowercase_word.count('fish')
sun = lowercase_word.count('sun')

print(sand + water + fish + sun)
