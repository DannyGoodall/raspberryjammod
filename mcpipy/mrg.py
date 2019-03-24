from random import randint, choice
from mineturtle import *
from mcpi.block import SIGN

class MrGTurtle(Turtle):

    def __init__(self, mc=None, spawn_offset_x=0, spawn_offset_y=0, spawn_offset_z=0):
        super().__init__(mc=mc)
        self.world_offset = Vec3(spawn_offset_x, spawn_offset_y, spawn_offset_z)
        self.block_list = []
        self.block_count = 0
        self.single_block = True
        self.last_block = None

    def use_block_list(self):
        self.single_block = False

    def use_single_block(self):
        self.single_block = True

    def add_block_to_list(self, block):
        self.block_list.append(block)

    def clear_block_list(self):
        self.block_list = []

    def actual_draw_point(self, x, y, z, done=None):
        # If we've got a non-empty block list, then take blocks out of there. If not use self.block
        block_choices = len(self.block_list)
        block_to_use = self.block if self.single_block else self.block_list[self.block_count % block_choices]
        print(f"block_count = {self.block_count}  -> block chosen = {block_to_use}. Same? {self.last_block == block_to_use}")
        self.mc.setBlock(x, y, z, block_to_use)
        self.last_block = block_to_use
        self.block_count += 1

    def drawLine(self, x1,y1,z1, x2,y2,z2):
        def drawPoint(p, fast=False):
            if self.pen:
                if self.width == 1 and not self.fan:
                    self.actual_draw_point(p[0],p[1],p[2],self.block)
                else:
                    for point in self.nib:
                        x0 = p[0]+point[0]
                        y0 = p[1]+point[1]
                        z0 = p[2]+point[2]
                        if (x0,y0,z0) not in done:
                            self.actual_draw_point(x0,y0,z0,self.block)
                            done.add((x0,y0,z0))

            if not fast and self.delayTime > 0:
                self.position.x = p[0]
                self.position.y = p[1]
                self.position.z = p[2]
                self.positionOut()
                self.delay()

        if not self.pen and self.delayTime == 0:
            return

        # dictinary to avoid duplicate drawing
        done = set()

        if self.pen and self.fan:
            if self.delayTime > 0:
                for a in getLine(x1,y1,z1, x2,y2,z2):
                    drawPoint(a)

            triangle = getTriangle(self.fan, (x1,y1,z1), (x2,y2,z2))
            for a in triangle:
                drawPoint(a, True)
        else:
            for a in getLine(x1,y1,z1, x2,y2,z2):
                drawPoint(a)


    def chat(self, text):
        self.mc.postToChat(text)

    def countdown(self, count=10, surpress_go=False, reverse=True):
        r = reversed(range(count)) if reverse else range(count)
        for n in r:
            self.mc.postToChat(f"Counting {n+1}...")
            time.sleep(1)
        if not surpress_go:
            self.mc.postToChat(f"Go!")

    def hover(self, count=1, pendown=True):
        pen_state = self.pen
        self.pendown() if pendown else self.penup()
        pos = self.mc.player.getPos()
        new_pos = Vec3(float(pos.x), float(pos.y+count), float(pos.z))
        self.goto(new_pos.x, new_pos.y, new_pos.z)
        self.mc.player.setPos(new_pos.x, new_pos.y, new_pos.z)
        self.pendown() if pen_state else self.penup()
        return self.where_is_steve_now()

    def interior_angle(self, sides):
        return (float(sides)-2.0) * 180.0 / float(sides)

    def polygon(self, sides, length, align=True, angle=0, fill=False):
        vertices = set()
        # self.angle(angle)
        # self.align_it(align)
        if fill:
            self.startface()
        angle_to_turn = float(180)-self.interior_angle(sides)
        for side in range(sides):
            if sides+1 < sides:
                self.go(length-1)
            else:
                self.go(length-2)
                self.move(1)
            self.right(angle_to_turn)
            vertices.add(self.where_is_steve_now())
        if fill:
            self.endface()
        return vertices

    def oblong(self, length, width, fill=False):
        vertices = set()
        if fill:
            self.startface()
        for sides in range(2):
            self.go(length-1)
            self.right(90)
            vertices.add(self.where_is_steve_now())
            self.go(width-1)
            self.right(90)
            vertices.add(self.where_is_steve_now())
        if fill:
            self.endface()
        return vertices


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
        return self.where_is_steve_now()

    def move_x(self, distance):
        self.position.x += distance
        self.positionOut()
        self.delay()
        return self.where_is_steve_now()

    def move_y(self, distance):
        self.position.y += distance
        self.positionOut()
        self.delay()
        return self.where_is_steve_now()

    def move_z(self, distance):
        self.position.z += distance
        self.positionOut()
        self.delay()
        return self.where_is_steve_now()

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
        return self.where_is_steve_now()

    def is_multiple_of(self, x, y):
        return int(x) % int(y) == 0

    def height_multiple_of(self, multiple):
        pos = self.mc.player.getPos()
        return self.is_multiple_of(pos.y, multiple)

    def odd_height(self):
        pos = self.mc.player.getPos()
        return self.is_odd(int(pos.y))

    def even_height(self):
        pos = self.mc.player.getPos()
        return self.is_even(int(pos.y))

    def is_odd(self, number):
        return number % 2 == 1

    def is_even(self, number):
        return not self.is_odd(number)

    def roundposdown(self, pos):
        pos.x = int(pos.x)
        pos.y = int(pos.y)
        pos.z = int(pos.z)
        return pos

    def roundposnearest(self, pos):
        pos.x = int(round(pos.x))
        pos.y = int(round(pos.y))
        pos.z = int(round(pos.z))
        return pos

    def where_is_steve_now(self, rounddown=False, roundnearest=False):
        pos = self.mc.player.getPos()
        pos = self.roundposnearest(pos) if roundnearest else pos
        pos = self.roundposdown(pos) if rounddown else pos
        return pos

    def steve_x(self):
        return self.where_is_steve_now().x

    def steve_y(self):
        return self.where_is_steve_now().y

    def steve_z(self):
        return self.where_is_steve_now().z

    def gotopos(self, pos):
        self.goto(pos.x, pos.y, pos.z)

    def star(self, points, size):
        if self.is_multiple_of(points, 2):
            max_degrees = 360.0
        else:
            max_degrees = 180.0
        for i in range(points):
            self.go(size-1)
            self.right(max_degrees-max_degrees/float(points))

    def drawDot(self):
        pos = self.where_is_steve_now()
        self.mc.setBlock(pos.x, pos.y, pos.z, self.block)
        return pos

    def move_diagonally(self, distance=1, direction='left'):
        # Move steve diagonally (45 degrees) without leaving a block and re-position
        # him to face the same direction as when he started
        direction = direction.lower()
        self.move(distance)
        if direction=='left' or direction=='l':
            self.left(90)
        else:
            self.right(90)
        self.move(distance)
        if direction=='left' or direction=='l':
            self.right(90)
        else:
            self.left(90)
        return self.where_is_steve_now()

    def move_diagonally_left(self, distance=1):
        self.move_diagonally(distance, 'left')
        return self.where_is_steve_now()

    def move_diagonally_right(self, distance=1):
        self.move_diagonally(distance, 'right')
        return self.where_is_steve_now()

    def pick_a_number_between(self, start, stop):
        return randint(start, stop)

    def pick_one(self, list_of_things):
        return choice(list_of_things)

    def cube(self, length, end_at_start=True):
        vertices = set()
        starting_delay = self.delayTime
        self.delayTime = 0
        starting_pos = self.where_is_steve_now()
        for sides in range(2):
            corners = []
            for n in range(4):
                pos = self.where_is_steve_now()
                corners.append(pos)
                vertices.add(pos)
                self.go(length -1)
                self.right(90)
            if sides == 0:
                # Now draw the uprights
                for corner in corners:
                    self.drawLine(
                        corner.x,
                        corner.y,
                        corner.z,
                        corner.x,
                        corner.y + length -1,
                        corner.z
                    )
                self.hover(length -1)
        if end_at_start:
            self.gotopos(starting_pos)
        self.delayTime = starting_delay
        return vertices

    def grid(self, size, length, width, angle=0, return_to_start=True):
        vertices = set()
        self.angle(angle)
        starting_position = self.where_is_steve_now(roundnearest=True)
        self.gotopos(starting_position)

        for n in range(width):
            for i in range(length):
                sub_vertices = self.polygon(4, size)
                for sv in sub_vertices:
                    vertices.add(sv)
                self.move(size-1)
            self.gotopos(starting_position)
            self.penup()
            self.right(90)
            self.go((n + 1) * (size-1))
            self.left(90)
            self.pendown()
        if return_to_start:
            self.gotopos(starting_position)
        return vertices

    def share_position(self, pos, round=False):
        x, y, z = pos.x, pos.y, pos.z
        if round:
            x = int(x)
            y = int(y)
            z = int(z)
        self.chat(
            f"x = {x}, y = {y}, z = {z}"
        )

    def beacon(self, glass_block=None):
        self.angle(0)
        old_block = self.block
        current_pos = self.where_is_steve_now()
        self.penblock(block.DIAMOND_BLOCK)
        self.startface()
        for sides in range(4):
            self.go(2)
            self.right(90)
        self.endface()
        self.penblock(block.BEACON)
        self.drawPoint(
            current_pos.x -1,
            current_pos.y +1,
            current_pos.z +1,
        )
        if glass_block:
            self.penblock(glass_block)
            self.drawPoint(
                current_pos.x - 1,
                current_pos.y + 2,
                current_pos.z + 1,
            )
        self.penblock(old_block)
        self.gotopos(current_pos)

    def drawPoint(self, x, y, z, done=None, fast=False):
        done = set() if not done else done
        if self.pen:
            if self.width == 1 and not self.fan:
                self.mc.setBlock(x,y,z,self.block)
            else:
                for point in self.nib:
                    x0 = x + point[0]
                    y0 = y + point[1]
                    z0 = z + point[2]
                    if (x0,y0,z0) not in done:
                        self.mc.setBlock(x0,y0,z0,self.block)
                        done.add((x0,y0,z0))

        if not fast and self.delayTime > 0:
            self.position.x = x
            self.position.y = y
            self.position.z = z
            self.positionOut()
            self.delay()

    def circle(self, radius, vertical=False, adjust_centre=True):
        """
                draws a circle in the X plane (i.e. horizontally)
                :param int x0:
                    The x position of the centre of the circle.
                :param int y:
                    The y position of the centre of the circle.
                :param int z0:
                    The z position of the centre of the circle.
                :param int radius:
                    The radius of the circle.
                :param int blockType:
                    The block id.
                :param int blockData:
                    The block data value, defaults to ``0``.
                """

        f = 1 - radius
        ddf_x = 1
        if vertical:
            ddf_y = -2 * radius
            relative_x = 0
            relative_y = radius
            steve_pos = self.where_is_steve_now()
            steve_pos.y = steve_pos.y + radius if adjust_centre else steve_pos.y
            self.drawPoint(steve_pos.x, steve_pos.y + radius, steve_pos.z)
            self.drawPoint(steve_pos.x, steve_pos.y - radius, steve_pos.z)
            self.drawPoint(steve_pos.x + radius, steve_pos.y, steve_pos.z)
            self.drawPoint(steve_pos.x - radius, steve_pos.y, steve_pos.z)

            while relative_x < relative_y:
                if f >= 0:
                    relative_y -= 1
                    ddf_y += 2
                    f += ddf_y
                relative_x += 1
                ddf_x += 2
                f += ddf_x
                self.drawPoint(steve_pos.x + relative_x, steve_pos.y + relative_y, steve_pos.z)
                self.drawPoint(steve_pos.x - relative_x, steve_pos.y + relative_y, steve_pos.z)
                self.drawPoint(steve_pos.x + relative_x, steve_pos.y - relative_y, steve_pos.z)
                self.drawPoint(steve_pos.x - relative_x, steve_pos.y - relative_y, steve_pos.z)
                self.drawPoint(steve_pos.x + relative_y, steve_pos.y + relative_x, steve_pos.z)
                self.drawPoint(steve_pos.x - relative_y, steve_pos.y + relative_x, steve_pos.z)
                self.drawPoint(steve_pos.x + relative_y, steve_pos.y - relative_x, steve_pos.z)
                self.drawPoint(steve_pos.x - relative_y, steve_pos.y - relative_x, steve_pos.z)
        else:
            ddf_z = -2 * radius
            relative_x = 0
            relative_z = radius
            steve_pos = self.where_is_steve_now()
            self.drawPoint(steve_pos.x, steve_pos.y, steve_pos.z + radius)
            self.drawPoint(steve_pos.x, steve_pos.y, steve_pos.z - radius)
            self.drawPoint(steve_pos.x + radius, steve_pos.y, steve_pos.z)
            self.drawPoint(steve_pos.x - radius, steve_pos.y, steve_pos.z)

            while relative_x < relative_z:
                if f >= 0:
                    relative_z -= 1
                    ddf_z += 2
                    f += ddf_z
                relative_x += 1
                ddf_x += 2
                f += ddf_x
                self.drawPoint(steve_pos.x + relative_x, steve_pos.y, steve_pos.z + relative_z)
                self.drawPoint(steve_pos.x - relative_x, steve_pos.y, steve_pos.z + relative_z)
                self.drawPoint(steve_pos.x + relative_x, steve_pos.y, steve_pos.z - relative_z)
                self.drawPoint(steve_pos.x - relative_x, steve_pos.y, steve_pos.z - relative_z)
                self.drawPoint(steve_pos.x + relative_z, steve_pos.y, steve_pos.z + relative_x)
                self.drawPoint(steve_pos.x - relative_z, steve_pos.y, steve_pos.z + relative_x)
                self.drawPoint(steve_pos.x + relative_z, steve_pos.y, steve_pos.z - relative_x)
                self.drawPoint(steve_pos.x - relative_z, steve_pos.y, steve_pos.z - relative_x)

    def sphere(self, radius, adjust_centre=True):
        # create sphere
        current_pos = self.where_is_steve_now()
        add_to_y = 0 if not adjust_centre else radius
        for x in range(radius * -1, radius):
            for y in range(radius * -1, radius):
                for z in range(radius * -1, radius):
                    if x ** 2 + y ** 2 + z ** 2 < radius ** 2:
                        self.actual_draw_point(
                            current_pos.x + x,
                            current_pos.y + y + add_to_y,
                            current_pos.z + z
                        )

    def tower_block(self, length, width, height, angle=0):
        self.angle(angle)
        for h in range(height):
            self.oblong(length, width)
            self.hover()
        shortest = min(length, width)
        print("Doing roof")
        for i, l in enumerate(range(shortest, 0, -2)):
            print(f"i = {i}")
            self.move_diagonally_right(1)
            self.oblong(
                length - ( (i+1) * 2),
                width - ( (i+1) * 2)
            )
            self.hover()


if __name__ == "__main__":
    steve = MrGTurtle()
    steve.pendelay(0.001)
    steve.angle(0)
    steve.gridalign()
    current_pos = steve.where_is_steve_now(roundnearest=True)
    steve.penblock(block.SEA_LANTERN)
    steve.countdown(5)

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


    steve.add_block_to_list(block.STAINED_GLASS_BLUE)
    steve.add_block_to_list(block.SEA_LANTERN)
    steve.use_block_list()
    # for n in range(2):
    #     steve.polygon(4,5)
    #     steve.hover()
    # steve.use_single_block()
    # steve.hover(5)
    steve.penblock(block.GLASS)
    steve.use_single_block()

    steve.sphere(30)
    steve.gotopos(current_pos)
    steve.penblock(block.WATER)
    steve.sphere(29)
