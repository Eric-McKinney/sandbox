# To make a sprite or a drawing in pygame rgb, simply make the color a variable in the function that draws them,
# next instantiate the RGB class, and draw the first time with the rgb_get method for the rgb tuple.
# Then on every loop/frame, call the increment_rgb method and the update_cycle method together.
# Make sure to draw after calling those methods, again using the get_rgb method as the color tuple.
# It is best practice to add a delay between each loop/frame or at least I think it looks better.
# There is an attribute named DELAY which can be used for this very purpose.
#
# ex:
# rgb = rgb_oop.RGB()
# your_draw_func(rgb.get_rgb())
# run = True
#
# while run:
#   for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#          run = False
#          break
#
#   rgb.increment_rgb()
#   rgb.update_cycle()
#   your_draw_func(rgb.get_rgb())
#
#   sleep(rgb.DELAY)


def increment_color(color, increase):
    if increase and color < 255:
        color += 1
    elif not increase and color > 0:
        color -= 1

    return color


class RGB:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.cycle = 0
        self.DELAY = 0.0035

    def get_rgb(self):
        return self.r, self.g, self.b

    def update_cycle(self):
        rgb = (self.r, self.g, self.b)

        if rgb == (255, 0, 0):
            self.cycle = 1
        elif rgb == (255, 255, 0):
            self.cycle = 2
        elif rgb == (0, 255, 0):
            self.cycle = 3
        elif rgb == (0, 255, 255):
            self.cycle = 4
        elif rgb == (0, 0, 255):
            self.cycle = 5
        elif rgb == (255, 0, 255):
            self.cycle = 6

    def increment_rgb(self):
        order = [
            (self.r, True),
            (self.g, True),
            (self.r, False),
            (self.b, True),
            (self.g, False),
            (self.r, True),
            (self.b, False)
        ]

        current_cycle = order[self.cycle]
        color = current_cycle[0]
        increase = current_cycle[1]

        color = increment_color(color, increase)

        if self.cycle in [0, 2, 5]:
            self.r = color
        elif self.cycle in [1, 4]:
            self.g = color
        elif self.cycle in [3, 6]:
            self.b = color
