# Standard Move
if len(inp) == 2:
 
    # Try block to handle errant input
    try: 
        val = list(map(int, inp))
    except ValueError:
        clear()
        print("Wrong input!")
        instructions()
        continue
    
   # Flag Input
elif len(inp) == 3:
    if inp[2] != 'F' and inp[2] != 'f':
        clear()
        print("Wrong Input!")
        instructions()
        continue
 
    # Try block to handle errant input  
    try:
        val = list(map(int, inp[:2]))
    except ValueError:
        clear()
        print("Wrong input!")
        instructions()
        continue
    
    
    # Sanity checks
if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
    clear()
    print("Wrong Input!")
    instructions()
    continue
 
# Get row and column numbers
r = val[0]-1
col = val[1]-1

# If cell already been flagged
if [r, col] in flags:
    clear()
    print("Flag already set")
    continue
 
# If cell already been displayed
if mine_values[r][col] != ' ':
    clear()
    print("Value already known")
    continue
 
# Check the number for flags    
if len(flags) < mines_no:
    clear()
    print("Flag set")
 
    # Adding flag to the list
    flags.append([r, col])
     
    # Set the flag for display
    mine_values[r][col] = 'F'
    continue
else:
    clear()
    print("Flags finished")
    continue

# If landing on a mine --- GAME OVER    
if numbers[r][col] == -1:
    mine_values[r][col] = 'M'
    show_mines()
    print_mines_layout()
    print("Landed on a mine. GAME OVER!!!!!")
    over = True
    continue

def show_mines():
    global mine_values
    global numbers
    global n
 
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                mine_values[r][col] = 'M'


# If landing on a cell with 0 mines in neighboring cells
elif numbers[r][n] == 0:
    vis = []
    mine_values[r][n] = '0'
    neighbours(r, col)
    
    def neighbours(r, col):
     
    global mine_values
    global numbers
    global vis
 
    # If the cell already not visited
    if [r,col] not in vis:
 
        # Mark the cell visited
        vis.append([r,col])
 
        # If the cell is zero-valued
        if numbers[r][col] == 0:
 
            # Display it to the user
            mine_values[r][col] = numbers[r][col]
 
            # Recursive calls for the neighbouring cells
            if r > 0:
                neighbours(r-1, col)
            if r < n-1:
                neighbours(r+1, col)
            if col > 0:
                neighbours(r, col-1)
            if col < n-1:
                neighbours(r, col+1)    
            if r > 0 and col > 0:
                neighbours(r-1, col-1)
            if r > 0 and col < n-1:
                neighbours(r-1, col+1)
            if r < n-1 and col > 0:
                neighbours(r+1, col-1)
            if r < n-1 and col < n-1:
                neighbours(r+1, col+1)  
                 
        # If the cell is not zero-valued            
        if numbers[r][col] != 0:
                mine_values[r][col] = numbers[r][col]
                
                # If selecting a cell with atleast 1 mine in neighboring cells  
else:   
    mine_values[r][col] = numbers[r][col]
    
    # Check for game completion 
if(check_over()):
    show_mines()
    print_mines_layout()
    print("Congratulations!!! YOU WIN")
    over = True
    continue


    

    