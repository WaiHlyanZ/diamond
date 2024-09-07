# Shine's solution
def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    height = alphabet.index(letter) + 1
    width = 2 * height - 1
    pattern = []

    # Generate the upper half of the pattern
    for i in range(height):
        row = ""
        for j in range(width):
            if j == height - 1 - i or j == height - 1 + i:
                row += alphabet[i]
            else:
                row += " "
        pattern.append(row)

    # Mirror the pattern for the lower half
    for row in reversed(pattern[:-1]):
        pattern.append(row)

    return pattern

# Example usage

if __name__ == "__main__":
    letter=input("Enter a letter: ")
    for i in rows(letter):
        print(i)


#========================================================================================================================================================================
# Wai Hlyan's solution

def pattern(letter, pieces, common_row=True) -> list:
    # the index is included up to that letter
    at_letter = pieces.index(letter) + 1
    # gaps go with odd sequence
    gap = 1   
    # needed character
    character = pieces[1:at_letter]
    # number of num_space in each side (left and right)
    num_space = at_letter - 1
    
    # first row is not fit into my logic so I kicked out.
    first_item = row = " " * num_space + pieces[0] + " " * num_space
    result = [first_item]
    # top half including the middle row
    for chr in character:
        # we need to decrease early bcz of the first row
        num_space -= 1
        row = " " * num_space + chr + " " * gap + chr + " " * num_space
        # gap increases as an odd sequence 
        gap += 2
        
        result.append(row)
    # the last row will include or not
    if not common_row and len(result) > 1:
        result.pop()

    return result

def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (letter in alphabet):
        return f"Unallowed character\nAllowed character: {alphabet}"
    if letter == alphabet[0]:
        return [alphabet[0]]
    return pattern(letter, pieces=alphabet, common_row=False) + list(reversed(pattern(letter, pieces=alphabet)))

if __name__ == "__main__":
    x = rows("E")
    for i in range(len(x)):
        print(x[i])

        
#===========================================================================================================================

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


