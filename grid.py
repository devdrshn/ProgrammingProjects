def draw_grid(rows, cols, robot_x, robot_y):

    # 1. Create an empty grid (Matrix) filled with dots

    grid=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append('.')
        grid.append(row)

    # 2. Place the Robot '#' at the specific coordinate
    # Note: In Python matrices, we access rows first (Y), then columns (X)

    grid[robot_y][robot_x] = '#'
    #print(grid)

    # 3. Print the grid to the screen
    
    print('\n')
    for row in grid:
        print("  ".join(row)) # Join the dots with a space for better visibility
    print('\n')

draw_grid(50,50,1,3)