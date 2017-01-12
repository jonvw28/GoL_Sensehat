from GoL import *

# Run some examples of what can be done with GoL.py functions

board = GoL_glider()
for i in range(100):
    GoL_show(board)
    board = GoL_step(board)
    sleep(0.1)

board = GoL_blinker()
new_board = GoL_step(board)
for i in range(50):
    GoL_show_ages(new_board,board)
    temp = new_board
    new_board = GoL_step(new_board)
    board = temp
    sleep(0.1)

board = GoL_pentomino()
new_board = GoL_step(board)
for i in range(100):
    GoL_show_ages(new_board,board)
    temp = new_board
    new_board = GoL_step(new_board)
    board = temp
    sleep(0.1)
