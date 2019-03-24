from mrg import *

steve = MrGTurtle()
steve.pendelay(0.001)
steve.angle(0)
steve.gridalign()
current_pos = steve.where_is_steve_now(roundnearest=True)
steve.penblock(block.SEA_LANTERN)
steve.countdown(3)

steve.beacon()
steve.gotopos(current_pos)
for n in [5,7,9,11,13,15]:
    steve.move_x(1)
    steve.move_z(-1)

    steve.hover(n + 3)
    steve.cube(n)