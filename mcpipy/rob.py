from mrg import *

steve = MrGTurtle()

steve.pendelay(0)
# steve.turtle(None)
steve.gridalign()

steve.countdown(5)

# steve.penblock(block.SEA_LANTERN)
# steve.hover(-1)

length = 50
times=50

starting_pos = steve.where_is_steve_now()

for rob in range(times):
    if steve.even_height():
        steve.penblock(block.OBSIDIAN)
    else:
        steve.penblock(block.SEA_LANTERN)
    steve.polygon(4,length)
    steve.hover(1)

steve.gotopos(starting_pos)

steve.penup()
steve.go(1)
steve.right(90)
steve.go(1)
steve.left(90)
steve.pendown()

steve.penblock(block.SLIME_BLOCK)

for rob in range(5):
    steve.polygon(4,length-2, fill=True)
    steve.hover(1)

