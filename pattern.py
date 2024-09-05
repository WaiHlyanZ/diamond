# def generate_pattern(n):
#     for i in range(n):
#         row = ""
#         for j in range(n):
#             # I can't think following line without outer resources
#             if j == i or j == n - 1 - i:
#                 row += "#"
#             else:
#                 row += "*"
#         print(row)

# # Example usage:
# n = 9
# generate_pattern(n)

a = "Z-------------------------------------------------Z"
b = "-Y-----------------------------------------------Y-"
x = "-------------------------------------------------"
# print(len(x))
gaps = [odd for odd in range(1, 3+3, 2)]
print(gaps)
