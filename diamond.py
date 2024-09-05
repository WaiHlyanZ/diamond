
def pattern(letter, inverted=False, common_row=True, value=1) -> list:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # the index is included up to that letter
    if not common_row:
        at_letter = alphabet.index(letter)
    else:
        at_letter = alphabet.index(letter) + 1

    gap = 1
    # odd sequence of gap
    # gaps = [odd for odd in range(1, at_letter + 3, 2)]
    # print(gaps)

    # calculate the diamond's width & height (not nessary)
    # width = ((alphabet.index(letter) + 1) * 2) - 1

    # checking mode
    # for upright
    if not inverted:
        # needed character
        character = alphabet[:at_letter]
        # number of num_space in each side (left and right)
        num_space = at_letter - value
        # # start of an odd sequence
        # gap = 1
    else:
    # for inverted
        start = alphabet.index(letter)
        num_space = 0

        # for outputing the last common row
        # if common_row:
        #     character = alphabet[start::-1]
        # else:
        #     character =  alphabet[start-1::-1]        

    
    result = []
    # top half including the middle row
    for _, chr in enumerate(character):
        # print(chr)
        
        # first row is not fit into my theory so I kicked out.
        if chr == 'A':
            row = " " * num_space + chr + " " * num_space
        else:
            row = " " * num_space + chr + " " * gap + chr + " " * num_space
            # gap increases as an odd sequence 
            gap += 2
        
        # if inverted:
        #     # num_space is increased
        #     num_space += 1
        # else:
            # num_space is decreased
        num_space -= 1
        

        result.append(row)
    
    return result

def rows(letter):
    return pattern(letter, common_row=False, value=0) + list(reversed(pattern(letter)))


