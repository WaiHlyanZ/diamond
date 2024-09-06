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

