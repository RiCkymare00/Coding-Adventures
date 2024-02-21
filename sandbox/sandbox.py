import pygame
import numpy as np

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background_image = pygame.image.load('spiaggia.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
screen.blit(background_image, (0, 0))
clock = pygame.time.Clock()
SAND = (189,166,100)
CELL_DIM = 1
running = True

class Grid:
    def __init__(self, grid, mouse_pos):
        self.grid = grid
        self.grid[mouse_pos[1]][mouse_pos[0]] = 1
        self.grid[mouse_pos[1]+1][mouse_pos[0]] = 1
        self.grid[mouse_pos[1]-1][mouse_pos[0]] = 1
        self.grid[mouse_pos[1]][mouse_pos[0]+1] = 1
        self.grid[mouse_pos[1]][mouse_pos[0]-1] = 1

    def update_grid(self):
        for x in range(HEIGHT - CELL_DIM):
            for y in range(WIDTH):
                if self.grid[x][y] == 1:
                    pygame.draw.rect(screen, SAND, (y, x, CELL_DIM, CELL_DIM))
                    if self.grid[x + 1][y] == 0:
                        self.grid[x][y] = 0
                        self.grid[x + 1][y] = 1
                        sfondo = background_image.get_at((y, x))
                        pygame.draw.rect(screen, sfondo, (y, x, CELL_DIM, CELL_DIM))
                        pygame.draw.rect(screen, SAND, (y, x + CELL_DIM, CELL_DIM, CELL_DIM))
                        #pygame.display.flip()
                        #clock.tick(5000)

                    elif self.grid[x + 1][y] == 1:
                        if self.grid[x+1][y+1] == 1 and self.grid[x+1][y-1] == 1: 
                            self.grid[x][y] = 1
                        elif self.grid[x+1][y+1] == 0:
                            self.grid[x][y] = 0
                            self.grid[x+1][y+1] = 1
                            sfondo = background_image.get_at((y, x)) 
                            pygame.draw.rect(screen, sfondo, (y, x, CELL_DIM, CELL_DIM))
                            pygame.draw.rect(screen, SAND, (y + CELL_DIM, x + CELL_DIM, CELL_DIM, CELL_DIM))
                            #pygame.display.flip()
                            #clock.tick(5000)
                        elif self.grid[x+1][y-1] == 0:
                            self.grid[x][y] = 0
                            self.grid[x+1][y-1] = 1
                            sfondo = background_image.get_at((y, x)) 
                            pygame.draw.rect(screen, sfondo, (y, x, CELL_DIM, CELL_DIM))
                            pygame.draw.rect(screen, SAND, (y - CELL_DIM, x + CELL_DIM, CELL_DIM, CELL_DIM))
                            #pygame.display.flip()
                            #clock.tick(5000)
        return self.grid

def update_grid_thread(grid, mouse_pos):
    grid = Grid(grid, mouse_pos)
    grid.update_grid()

my_grid = np.zeros((HEIGHT, WIDTH), dtype=int)
while running:
    mouse_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
            while mouse_pressed or (event.type == pygame.MOUSEMOTION and mouse_pressed):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_pressed = False
                mouse_pos = pygame.mouse.get_pos()
                my_grid = Grid(my_grid, mouse_pos)
                my_grid = my_grid.update_grid()
                pygame.display.flip()
                clock.tick(60)
