# Function to draw a diamond pattern
def draw_diamond(rows):
    # Upper part of the diamond
    for i in range(1, rows + 1, 2):
        spaces = " " * ((rows - i) // 2)  # Create leading spaces
        stars = "*" * i                   # Create stars for the row
        print(spaces + stars)

    # Lower part of the diamond
    for i in range(rows - 2, 0, -2):
        spaces = " " * ((rows - i) // 2)  # Create leading spaces
        stars = "*" * i                   # Create stars for the row
        print(spaces + stars)

# Get user input for the diamond size
rows = int(input("Enter an odd number of rows for the diamond: "))

# Ensure the input is odd for symmetry
if rows % 2 == 0:
    print("Please enter an odd number.")
else:
    draw_diamond(rows)
