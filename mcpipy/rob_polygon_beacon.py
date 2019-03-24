from mrg import *

steve = MrGTurtle()
steve.pendelay(0.001)
steve.angle(0)
steve.gridalign()
current_pos = steve.where_is_steve_now(roundnearest=True)
steve.penblock(block.SEA_LANTERN)
steve.countdown(3)

stained_glass_blocks = [
    block.STAINED_GLASS_WHITE,
    block.STAINED_GLASS_ORANGE,
    block.STAINED_GLASS_MAGENTA,
    block.STAINED_GLASS_LIGHT_BLUE,
    block.STAINED_GLASS_YELLOW,
    block.STAINED_GLASS_LIME,
    block.STAINED_GLASS_PINK,
    block.STAINED_GLASS_GRAY,
    block.STAINED_GLASS_LIGHT_GRAY,
    block.STAINED_GLASS_CYAN,
    block.STAINED_GLASS_PURPLE,
    block.STAINED_GLASS_BLUE,
    block.STAINED_GLASS_BROWN,
    block.STAINED_GLASS_GREEN,
    block.STAINED_GLASS_RED,
    block.STAINED_GLASS_BLACK
]
steve.penblock(block.AIR)
sides = 22
distance = 20
vertices = steve.polygon(sides, distance)
for pos in vertices:
    steve.gotopos(pos)
    steve.beacon(glass_block=steve.pick_one(stained_glass_blocks))
