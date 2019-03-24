from mrg import *

steve = MrGTurtle()

steve.pendelay(0)
# steve.turtle(None)
steve.gridalign()

steve.countdown(5)

steve.penblock(block.SEA_LANTERN)
# steve.hover(-1)

steps = 8
height = 42
length = 12
sides = 3
# for h in range(height):
#
#     if steve.height_multiple_of(3):
#         steve.penblock(block.SEA_LANTERN)
#     else:
#         steve.penblock(block.GLASS)
#
#     steve.polygon(90,1,fill=True)
#     steve.hover()
#



length = 3
w = 10
h = 10


steve.hover(-1)
original_position = steve.where_is_steve_now(roundnearest=True)
steve.gotopos(original_position)
for i in range(0,7):
    steve.hover(20*i)
    steve.angle(0)
    steve.star(5+i,40)
    # steve.move(45*i)
