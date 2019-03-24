from mrg import *

steve = MrGTurtle()
steve.pendelay(0.001)
steve.angle(0)
steve.gridalign()
current_pos = steve.where_is_steve_now(roundnearest=True)
steve.penblock(block.SEA_LANTERN)
steve.countdown(10)

steve.gotopos(Vec3(0,0,0))
l = 10
steve.hover(5)
for i in range(10000):
    steve.move(l+(i*10))
    steve.right(90)
steve.gotopos(Vec3(0,0,0))
