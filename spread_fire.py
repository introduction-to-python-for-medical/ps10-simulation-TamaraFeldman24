import random  # for generating a random number
import copy  # to create a copy in memory of an object

# for plots:
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

def initialize_forest(grid_size=30, p_tree=0.6):
    """Initialize a grid for the forest fire simulation."""
    # Build an empty grid
    grid = [[0] * grid_size for _ in range(grid_size)]

    # Assign trees randomly to the cells
    for i in range(grid_size):
        for j in range(grid_size):
            if random.random() < p_tree:
                grid[i][j] = 1

    # Set the center tree on fire
    center = grid_size // 2
    grid[center][center] = 2

    return grid

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                if (
                    (i > 0 and grid[i - 1][j] == 2)  # Up
                    or (i < grid_size - 1 and grid[i + 1][j] == 2)  # Down
                    or (j > 0 and grid[i][j - 1] == 2)  # Left
                    or (j < grid_size - 1 and grid[i][j + 1] == 2)  # Right
                ):
                    update_grid[i][j] = 2

    return update_grid

# Set up the grid
grid_size = 30
p_tree = 0.6  # Probability that a cell contains a tree

grid = initialize_forest(grid_size, p_tree)

# Run the simulation
fig, ax = plt.subplots()
for step in range(100):
    update_grid = spread_fire(grid)
    if update_grid == grid:
        break
    grid = update_grid
    ax.imshow(grid, cmap='YlOrRd', vmin=0, vmax=2)
    ax.set_title(f'Step {step}')
    display(fig)
    clear_output(wait=True)
    plt.pause(0.01)

plt.show()
