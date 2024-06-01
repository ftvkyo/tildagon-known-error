import math
from random import random, randint

import app

from events.input import Buttons, BUTTON_TYPES


MIN = -120
MAX = 120
SIDE = MAX - MIN

CENTER = (MIN + MAX) / 2
RADIUS = (MAX - MIN) / 2
AREA = math.pi * RADIUS * RADIUS


TEXTS = [
    "Known Error",
    "Unknown Error",
]


def polar2cartesian(a, d):
    x = CENTER + math.cos(a) * d
    y = CENTER + math.sin(a) * d
    return int(x), int(y)


def random_polar():
    a = random() * math.pi * 2

    # As with the same `a`, points get closer with reduction of `d`,
    # the points are redistributed
    d = math.sqrt(random()) * RADIUS

    return a, d


def random_cartesian():
    x = MIN + random() * SIDE
    y = MIN + random() * SIDE

    return x, y


class KnownErrorApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

        # Selected display text
        self.text_index = 0

        # Glitch effect
        self.glitch_enabled = False
        self.glitch_timing = 0
        self.glitch_period_ms = 2000
        self.glitch_stripes = []

    #############
    # Overrides #
    #############

    def update(self, delta):
        if self.glitch_enabled:
            self.glitch_timing += delta
            if self.glitch_timing > self.glitch_period_ms:
                self.glitch_timing = 0
                self.update_glitch()

        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            print("Closing")
            self.minimise()

        elif self.button_states.get(BUTTON_TYPES["CONFIRM"]):
            self.button_states.clear()
            self.glitch_enabled = not self.glitch_enabled
            print(f"Glitch enabled: {self.glitch_enabled}")

        elif self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.text_index += 1
            self.text_index %= len(TEXTS)

        elif self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.button_states.clear()
            self.text_index -= 1
            self.text_index %= len(TEXTS)

    def draw(self, ctx):
        ctx.save()
        self.clear(ctx)
        self.text(ctx, TEXTS[self.text_index])
        if self.glitch_enabled:
            self.glitch(ctx)
        ctx.restore()

    ########
    # User #
    ########

    def update_glitch(self):
        self.glitch_stripes = []
        for _ in range(randint(0, 32)):
            x = MIN + random() * SIDE
            r, g, b = random(), random(), random()
            self.glitch_stripes.append((x, r, g, b))

    def clear(self, ctx):
        ctx.rgb(0, 0, 0).rectangle(MIN, MIN, SIDE, SIDE).fill()

    def text(self, ctx, text):
        width = ctx.text_width(text)
        left_edge = CENTER - width / 2
        ctx.rgb(1, 1, 1).move_to(left_edge, 0).text(text)

    def glitch(self, ctx):
        for (x, r, g, b) in self.glitch_stripes:
            ctx.rgb(r, g, b).rectangle(x, MIN, 1, SIDE).fill()
