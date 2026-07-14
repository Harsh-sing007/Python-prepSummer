#              *
#             ***
#            *****
#           *******
#            *****
#             ***
#              *
# write the code to print the above star pattern in Python.

def print_star_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))