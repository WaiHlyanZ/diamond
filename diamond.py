
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

