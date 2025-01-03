# Function to generate pyramid number pattern

def pyramid_pattern(n):
    for i in range(1, n+1):
        # Print spaces before the numbers
        print(" " * (n - i), end="")

        # Print the increasing numbers
        for j in range(1, i+1):
            print(j, end="")

        # Print the decreasing numbers
        for j in range(i-1, 0, -1):
            print(j, end="")

        # Move to the next line
        print()


n = 5  
pyramid_pattern(n)
