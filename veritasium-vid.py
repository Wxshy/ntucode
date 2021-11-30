import random
import pygame
import time


class Cell():
    def __init__(self, alive):
        self.alive = True if alive == 1 else False
        self.neighbour_count = 0

    def update(self):
        if self.alive:
            if  not (self.neighbour_count == 3 or self.neighbour_count == 2):
                self.alive = False
        else:
            if self.neighbour_count == 3:
                self.alive = True

        self.neighbour_count = 0
        
def create_grid(x = 10, y = 10):
    grid = []

    for _ in range(y):
        t = []
        for _ in range(x):
            t.append(Cell(random.randint(0,1)))

        grid.append(t)

    return grid


def print_grid(grid):
    for r in grid:
        print([c.alive for c in r])



def get_neighbours(grid):
    old_grid = grid

    for x in range(len(old_grid)):
        for y in range(len(old_grid)):
            offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                    (1, 0), (-1, 1), (0, 1), (1, 1)]
                    
            current = old_grid[x][y]
            possible_neighbors = {(x + x_add, y + y_add) for x_add, y_add in offsets}

            neighbours = {(pos[0], pos[1]) for pos in possible_neighbors if pos[0] in pos_index and pos[1] in pos_index}

            for nx, ny in neighbours:        
                if grid[nx][ny].alive:
                    current.neighbour_count += 1
            
            current.update()

width = 10
height = 10


pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Game Of Life')

pos_index = [0,1,2,3,4,5,6,7,8,9]


grid = create_grid(height, width)

print_grid(grid)



run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    get_neighbours(grid) 



    cell_width = screen.get_width() / width
    cell_height = screen.get_height() / height
    border_size = 2

    alive_colour = (0,255,0)
    dead_colour = (255,0,0)

    for y in range(10):
        for x in range(10):
            if grid[y][x].alive:
                pygame.draw.rect(screen, alive_colour, (x * cell_width + border_size, y * cell_height + border_size, cell_width - border_size, cell_height - border_size))
            else:
                pygame.draw.rect(screen, dead_colour, (x * cell_width + border_size, y * cell_height + border_size, cell_width - border_size, cell_height - border_size))

    
    print_grid(grid)

    pygame.display.update()
    time.sleep(1)
    clock.tick(60)

                        
pygame.quit()
quit()


