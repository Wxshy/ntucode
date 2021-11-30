import random


grid = []

for _ in range(10):
    t = []
    for _ in range(10):
        t.append(random.randint(0,1))

    grid.append(t)

for i in grid:
    print([x for x in i])

def get_neighbours(grid):
    #return grid but with how many alive neighbours
    neighbours_alive = []
    x = 0
    y = 0
    current = grid[y][x]
    neighbours = [
        [
        grid[y-1][x-1],
        grid[y-1][x],
        grid[y-1][x+1]
        ],
        [
        grid[y][x-1],
        grid[y][x+1]
        ],
        [
        grid[y+1][x-1],
        grid[y+1][x],
        grid[y+1][x+1]
        ]
    ]
    print((x,y),' neighbours')
    print(neighbours)
            
                        
get_neighbours(grid)


