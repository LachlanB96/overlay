import pyHook,pythoncom,pygame

def OnKeyboardEvent(event):
    try:
        print (event.Ascii)
    except:
        print ("ERROR")

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

# initialize pygame and start the game loop
pygame.init()
while True:
    pygame.event.pump()