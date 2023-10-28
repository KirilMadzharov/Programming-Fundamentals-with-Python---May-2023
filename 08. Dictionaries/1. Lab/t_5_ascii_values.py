words = input().split(", ")

ascii_dict = {word: ord(word) for word in words}

print(ascii_dict)
