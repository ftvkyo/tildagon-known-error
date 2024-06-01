import asyncio
import app

from events.input import Buttons, BUTTON_TYPES


class KnownErrorApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        ctx.save()
        ctx.rgb(0,0,0).rectangle(-120,-120,240,240).fill()
        ctx.rgb(1,1,1).move_to(-80,0).text("Known Error")
        ctx.restore()
