import copy 

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules, including edges."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1: 

               
                neighbors = []

               
                if i > 0:
                    neighbors.append(grid[i-1][j])
             
                if i < grid_size - 1:
                    neighbors.append(grid[i+1][j])
               
                if j > 0:
                    neighbors.append(grid[i][j-1])
               
                if j < grid_size - 1:
                    neighbors.append(grid[i][j+1])

                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
