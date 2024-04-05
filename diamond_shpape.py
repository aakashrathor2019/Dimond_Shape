def print_diamond(n):
    # Upper half of the diamond
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    
    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Test the function with n = 4
print_diamond(4)
