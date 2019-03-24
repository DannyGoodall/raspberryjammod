from mrg import *

steve = MrGTurtle()

steve.pendelay(0)
# steve.turtle(None)
steve.gridalign()
steve.angle(0)

pos = None
old_pos = steve.where_is_steve_now(roundnearest=True)
while True:
    pos = steve.where_is_steve_now(roundnearest=True)
    if pos.x != old_pos.x or pos.y != old_pos.y or pos.z != old_pos.z:
        steve.chat(f"Steve is at x={int(pos.x)}, y={int(pos.y)}, z={int(pos.z)}")
        old_pos = pos
    time.sleep(1)