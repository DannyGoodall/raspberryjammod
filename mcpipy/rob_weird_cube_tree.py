from mrg import *

steve = MrGTurtle()
steve.pendelay(0.001)
steve.angle(0)
steve.gridalign()
steve.countdown(3)

steve.penblock(block.SEA_LANTERN)
starting_pos = steve.where_is_steve_now()
for direction in [0, 90, 180, 270]:
    steve.gotopos(starting_pos)
    steve.angle(direction)
    for n in range(5):
        steve.cube(10)
        steve.move_diagonally(10)
        steve.hover(10, pendown=False)
