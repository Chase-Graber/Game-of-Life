import pygame, random

pygame.init()

ALIVE = (255, 255, 255)
DEAD = (0, 0, 0)

CELL_SIZE = 10
NUM_CELLS_X = 60
NUM_CELLS_Y = 60

SCREEN_WIDTH = CELL_SIZE * NUM_CELLS_X
SCREEN_HEIGHT = CELL_SIZE * NUM_CELLS_Y

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Cell:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
    
    def draw(self):
        if self.alive == 1:
            pygame.draw.rect(screen, ALIVE, pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))
        else:
            pygame.draw.rect(screen, DEAD, pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))
    
    def update(self, index):
        N = max(0, index - NUM_CELLS_X)
        E = min(0, )

def make_cells():
    cells = []
    for i in range(NUM_CELLS_X):
        for j in range(NUM_CELLS_Y):
            rand = random.randint(0, 1)
            cells.append(Cell(i * CELL_SIZE, j * CELL_SIZE, rand))
    
    return cells

run = True
cells = make_cells()
while run:
    clock = pygame.time.Clock()
    clock.tick(60)

    for i in range(len(cells)):
        cells[i].draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
