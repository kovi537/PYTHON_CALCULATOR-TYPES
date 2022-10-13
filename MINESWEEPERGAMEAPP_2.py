if __name__ == "__main__":
 
    # Size of grid
    n = 8
    # Number of mines
    mines_no = 8
 
    # The actual values of the grid
    numbers = [[0 for y in range(n)] for x in range(n)] 
    # The apparent values of the grid
    mine_values = [[' ' for y in range(n)] for x in range(n)]
    # The positions that have been flagged
    flags = []
    
    
    