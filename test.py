# print("ABCDE"[0:2])

letter = input("Input: ")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_index = letters.index(letter)
rows = list(range(letter_index)) + list(range(letter_index, -1, -1))

print(list(range(letter_index)))
print(list(range(letter_index, -1, -1)))
print(rows)