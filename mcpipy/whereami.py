from mine import *
from sys import argv
from time import sleep

mc = Minecraft()

old_x = 0
old_y = 0
old_z = 0
while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    if old_x != x or old_y != y or old_z != z:
        mc.postToChat("x = {}, y = {}, z = {}".format(x,y,z))
    sleep(1)
    old_x = x
    old_y = y
    old_z = z
