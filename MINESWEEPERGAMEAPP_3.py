# Function for setting up Mines
def set_mines():
 
    global numbers
    global mines_no
    global n
 
    # Track of number of mines already set up
    count = 0
    while count < mines_no:
 
        # Random number from all possible grid positions 
        val = random.randint(0, n*n-1)
 
        # Generating row and column from the number
        r = val // n
        col = val % n
 
        # Place the mine, if it doesn't already have one
        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col] = -1
            
            
            
            