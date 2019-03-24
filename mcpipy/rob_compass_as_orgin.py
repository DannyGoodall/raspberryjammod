from mrg import *

steve = MrGTurtle()
steve.pendelay(0)
steve.gridalign()
starting_pos = steve.where_is_steve_now(roundnearest=True)
steve.countdown(5)

steve.angle(0)
# black it out
steve.penblock(block.OBSIDIAN)
steve.gotopos(Vec3(0,-1,0))
for turns in range(4):
    steve.polygon(4,20, fill=True)
    steve.right(90)


steve.penblock(block.SEA_LANTERN)
length = 20
for count, turns in enumerate(range(8)):
    steve.gotopos(Vec3(0,-1,0))
    steve.go(length) if count % 2 == 0 else steve.go(length/4*3)
    steve.right(45)
steve.hover(5)