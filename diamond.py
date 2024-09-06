"""
# Mahn's solution 
def rows(letter):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_index = letters.index(letter)
    row_indices = list(range(letter_index)) + list(range(letter_index, -1, -1))

    result = []

    for i in row_indices:
        current_letter = letters[i]
        
        spaces = letter_index - i
        
        # Letter "A" does not have inner spacing
        if i == 0:
            row = " " * spaces + current_letter + " " * spaces
        else:
            # To add inner spacing for letters that are not "A"
            inner_spaces = " " * (2 * i - 1)
            row = " " * spaces + current_letter + inner_spaces + current_letter + " " * spaces
        
        result.append(row)

    return result

if __name__ == "__main__":
    letter=input("Enter a letter: ")
    for i in rows(letter):
        print(i)
"""
