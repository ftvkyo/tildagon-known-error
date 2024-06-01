import math

import app

from events.input import Buttons, BUTTON_TYPES


MIN = -120
MAX = 120
SIDE = MAX - MIN

CENTER = MIN + MAX / 2
RADIUS = (MAX - MIN) / 2


TEXTS = [
    "Known Error",
    "Unknown Error",
]


def polar2cartesian(a, d):
    x = CENTER + math.cos(a) * d
    y = CENTER + math.sin(a) * d
    return (x, y)


class KnownErrorApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

        self.text_index = 0
        self.glitch_percent = 0

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()

            self.text_index += 1
            self.text_index %= len(TEXTS)

        if self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()

            self.text_index = self.text_index - 1
            self.text_index %= len(TEXTS)

    def draw(self, ctx):
        ctx.save()
        self.clear_background(ctx)
        ctx.rgb(1,1,1).move_to(-80,0).text(TEXTS[self.text_index])
        ctx.restore()

    def clear_background(self, ctx):
        ctx.rgb(0,0,0).rectangle(MIN, MIN, SIDE, SIDE).fill()

    def glitch(self, ctx):
        pass
