from mrg import *

steve = MrGTurtle()
steve.pendelay(0)
steve.angle(0)
steve.gridalign()
starting_pos = steve.where_is_steve_now(roundnearest=True)
steve.penblock(block.SEA_LANTERN)
steve.countdown(3)

radius = 20
for n in range(100):
    if steve.is_multiple_of(n,10):
        steve.penblock(block.SEA_LANTERN)
    else:
        steve.penblock(block.GLASS)
    steve.circle(radius, vertical=True, adjust_centre=False)
    steve.move(1)
steve.hover(30)