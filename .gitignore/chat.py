def rows(letter, inverted=False, common_row=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # calculate the diamond's width & height (not nessary)
    # width = ((alphabet.index(letter) + 1) * 2) - 1

    # checking mode
    # for upright
    if not inverted:
        # needed character
        character = alphabet[:alphabet.index(letter) + 1]
        # number of num_space in each side (left and right)
        num_space = alphabet.index(letter)
        # start of an odd sequence
        gap = 1
    else:
    # for inverted
        
        character =  alphabet[alphabet.index(letter)-1::-1]
        return character

    

    result = []
    # top half including the middle row
    for chr in character:
        # first row is not fit into my theory so I kicked out.
        if chr == 'A':
            row = '-' * num_space + chr + '-' * num_space
        else:
            row = '-' * num_space + chr + '-' * gap + chr + '-' * num_space
            # gap increases as an odd sequence
            gap += 2
        # num_space is decreased 
        num_space -= 1
        result.append(row)
    
    return result

# Function to print the diamond
# def print_diamond(letter):
#     diamond = rows(letter)
#     for row in diamond:
#         print(row)
# print_diamond('E')

x = rows("C", inverted=False)
for i in x:
    print(i)

