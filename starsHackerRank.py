def print_right_aligned_triangle(n):
    for i in range(1, n + 1):
        spaces = n - i        # leading spaces: for line i (1-based) we need n-i spaces
        stars  = i            # number of stars equals the line index
        print(' ' * spaces + '*' * stars)

# Example for n = 4

