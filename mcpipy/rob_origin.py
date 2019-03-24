from mrg import *

steve = MrGTurtle()
steve.pendelay(0.001)
steve.angle(0)
steve.gridalign()
current_pos = steve.where_is_steve_now(roundnearest=True)
steve.countdown(3)

steve.gotopos(Vec3(0,0,0))
