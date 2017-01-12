import numpy as np
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def GoL_step(cells, size=(8,8)):
    '''
    Take a single Game of Life Step
    '''
    new_cells = np.zeros(size, dtype = cells.dtype)
    for i in range(size[0]):
        for j in range(size[1]):
            tot_nbrs = cells[(i-1)%size[0],(j-1)%size[1]]
            tot_nbrs += cells[i%size[0],(j-1)%size[1]]
            tot_nbrs += cells[(i+1)%size[0],(j-1)%size[1]]
            tot_nbrs += cells[(i-1)%size[0],(j)%size[1]]
            tot_nbrs += cells[(i+1)%size[0],(j)%size[1]]
            tot_nbrs += cells[(i-1)%size[0],(j+1)%size[1]]
            tot_nbrs += cells[(i)%size[0],(j+1)%size[1]]
            tot_nbrs += cells[(i+1)%size[0],(j+1)%size[1]]

            if cells[i,j] == 0 and tot_nbrs == 3:
                new_cells[i,j] = 1
            elif cells[i,j] == 1 and (tot_nbrs == 2 or tot_nbrs == 3):
                new_cells[i,j] = 1
            else:
                new_cells[i,j]=0
    return new_cells

def GoL_show(cells):
    '''
    Display Alive cells as green and dead cells as red
    '''
    for i in range(8):
        for j in range(8):
            if cells[i,j] == 1:
                sense.set_pixel(i,j,0,255,0)
            else:
                sense.set_pixel(i,j,255,0,0)

def GoL_show_ages(cells,old_cells):
    '''
    Display deaths as dull red, births as green and surviving cells as blue
    '''
    for i in range(8):
        for j in range(8):
            if cells[i,j] == 0 and old_cells[i,j] == 0:
                sense.set_pixel(i,j,0,0,0)
            elif cells[i,j] == 0 and old_cells[i,j] == 1:
                sense.set_pixel(i,j,127,0,0)
            elif old_cells[i,j] == 0:
                sense.set_pixel(i,j,0,255,0)
            else:
                sense.set_pixel(i,j,0,0,255)

def GoL_init():
    '''
    Initialise a random grid of live cells
    '''
    cells = np.random.choice((0,1),size=(8,8))
    return( cells )
                

def GoL_blinker():
    '''
    Initialise a Blinker
    '''
    cells = np.zeros(shape = (8,8), dtype = 'int32')
    cells[2,2] = 1
    cells[2,3] = 1
    cells[2,4] = 1
    return cells

def GoL_glider():
     '''
     Initialise a Glider
     '''
     cells = np.zeros(shape = (8,8), dtype = 'int32')
     cells[2,2] = 1
     cells[2,3] = 1
     cells[2,4] = 1
     cells[3,4] = 1
     cells[4,3] = 1
     return cells

def GoL_pentomino():
     '''
     Initialise a cool shape - more fun on bigger boards
     '''
     cells = np.zeros(shape = (8,8), dtype = 'int32')
     cells[2,3] = 1
     cells[2,4] = 1
     cells[3,2] = 1
     cells[3,3] = 1
     cells[4,3] = 1
     return cells
