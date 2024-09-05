def diamond(letter):
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
                row += "*"
        pattern.append(row)

    # Print the lower half (mirror of the upper half)
    for row in reversed(pattern[:-1]):
        pattern.append(row)
    return "".join(pattern)