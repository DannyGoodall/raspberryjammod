#
# Code by Alexander Pruss and under the MIT license
#
from random import randint, choice

from mineturtle import *

class MrGTurtle(Turtle):

    def hover(self, count=1):
        pos = self.mc.player.getPos()
        new_pos = Vec3(float(pos.x), float(pos.y+count), float(pos.z))
        self.goto(new_pos.x, new_pos.y, new_pos.z)

        self.mc.player.setPos(float(pos.x), float(pos.y+count+1), float(pos.z))

    def interior_angle(self, sides):
        return (float(sides)-2.0) * 180.0 / float(sides)

    def polygon(self, sides, length, align=True, face_origin=True):
        self.align_it(align)
        angle_to_turn = 180-self.interior_angle(sides)
        for side in range(sides):
            self.go(length)
            self.right(angle_to_turn)

    def move(self, distance):
        # Similar to go but no drawline
        [dx,dy,dz] = self.getHeading()
        newX = self.position.x + dx * distance
        newY = self.position.y + dy * distance
        newZ = self.position.z + dz * distance
        self.position.x = newX
        self.position.y = newY
        self.position.z = newZ
        self.positionOut()
        self.delay()

    def align_it(self, align=True):
        if align:
            self.gridalign()

    def move_relative(self, x, y, align=True):
        # Move relative to current position, y indicates the direction we are facing
        self.align_it(align)
        self.move(x)
        self.right(90)
        self.move(y)
        self.left(90)

    def is_odd(self, number):
        return number % 2 == 1

    def is_even(self, number):
        return not self.is_odd(number)


steve = MrGTurtle()
steve.pendelay(0.05)

old_pos = steve.mc.player.getPos()
new_pos = steve.position
steve.penblock(
    block.WOOL_WHITE
)

steve.align_it(True)
while True:
    # steve.mc.postToChat(new_pos)
    time.sleep(0.1)
    if int(old_pos.x) != int(new_pos.x) or int(old_pos.y) != int(new_pos.y) or int(old_pos.z) != int(new_pos.z):
        steve.mc.setBlock(int(new_pos.x), int(new_pos.y), int(new_pos.z), block.WOOL_WHITE.id)

    old_pos = new_pos
    new_pos = steve.mc.player.getPos()


