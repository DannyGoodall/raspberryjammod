from mrg import *

steve = MrGTurtle()
steve.pendelay(0.001)
steve.angle(0)
steve.gridalign()
starting_pos = steve.where_is_steve_now(roundnearest=True)
steve.penblock(block.SEA_LANTERN)
steve.countdown(3)

steve.penblock(block.NETHERRACK)
steve.grid(3,10,10)
steve.hover()
steve.penblock(block.FIRE)
steve.grid(3,10,10)
