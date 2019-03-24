from mrg import *

steve = MrGTurtle()
steve.pendelay(0)
steve.angle(0)
steve.gridalign()
starting_pos = steve.where_is_steve_now(roundnearest=True)
steve.penblock(block.SEA_LANTERN)
steve.countdown(3)

steps = 8
length = 20
height = 50
per_step = 360.0 / float(steps)
steve.hover(-1)
for h in range(height):
    if steve.height_multiple_of(5):
        steve.penblock(block.SEA_LANTERN)
    else:
        steve.penblock(block.STAINED_GLASS_BLUE)
    for a in range(steps):
        steve.polygon(4,12)
        steve.right(per_step)
    steve.hover()