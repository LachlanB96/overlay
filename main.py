import pyglet

import time

window1 = pyglet.window.Window(style='borderless')
window1.set_location(-1920, 0)
window1.set_size(1920, 1250)

window2 = pyglet.window.Window()
window2.set_location(1920, 0)
window2.set_size(1920, 1250)

pyglet.app.run()

time.sleep(2)
