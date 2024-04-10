#Print a diamond shape with 2n rows
def print_diamond(n):
    # Upper part of the diamond
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    
    # Lower part of the diamond
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Main program
n = int(input("Enter the number of rows for the diamond: "))
print_diamond(n)
