import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from keyboard import char_to_keycode

debug = True

if debug: print("Starting...")

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

with open("payload.txt") as file:
    lines = file.read().splitlines()

if debug: print("Printing lines of payload", lines)

default_delay = 0
previous_line = ""
def process_line(line):
        if debug: print("LINE:", line)

        args = line.split(" ", 1)
        if debug: print("ARGS:", args)

        inst = args[0]
        if debug: print("INST:", inst)

        if inst == "REM":
            return;

        global default_delay
        if inst == "DEFAULT_DELAY" or inst == "DEFAULTDELAY":
            try:
                default_delay = int(args[1])
            except ValueError:
                print("Invalid integer")
                return

        if default_delay > 0:
            time.sleep(default_delay / 1000)

        if inst == "DELAY":
            try:
                time.sleep(int(args[1]) / 1000)
            except ValueError:
                print("Invalid integer")
                return

        if inst == "STRING":
            layout.write(args[1])

        if inst == "GUI" or inst == "WINDOWS":
            kbd.send(Keycode.WINDOWS, char_to_keycode(args[1]))

        if inst == "APP" or inst == "MENU":
            kbd.send(Keycode.APPLICATION)

        if inst == "SHIFT":
            kbd.send(Keycode.SHIFT, char_to_keycode(args[1]))

        if inst == "ALT":
            kbd.send(Keycode.ALT, char_to_keycode(args[1]))

        if inst == "CONTROL" or inst == "CTRL":
            kbd.send(Keycode.CONTROL, char_to_keycode(args[1]))

        if inst == "DOWNARROW" or inst == "DOWN":
            kbd.send(Keycode.DOWN_ARROW)

        if inst == "LEFTARROW" or inst == "LEFT":
            kbd.send(Keycode.LEFT_ARROW)

        if inst == "RIGHTARROW" or inst == "RIGHT":
            kbd.send(Keycode.RIGHT_ARROW)

        if inst == "UPARROW" or inst == "UP":
            kbd.send(Keycode.UP_ARROW)

        if inst == "BREAK" or inst == "PAUSE":
            kbd.send(Keycode.PAUSE)

        if inst == "CAPSLOCK":
            kbd.send(Keycode.CAPS_LOCK)

        if inst == "DELETE":
            kbd.send(Keycode.DELETE)

        if inst == "ESC" or inst == "ESCAPE":
            kbd.send(Keycode.ESCAPE)

        if inst == "HOME":
            kbd.send(Keycode.HOME)

        if inst == "INSERT":
            kbd.send(Keycode.INSERT)

        if inst == "NUMLOCK":
            kbd.send(Keycode.KEYPAD_NUMLOCK)

        if inst == "PAGEUP":
            kbd.send(Keycode.PAGE_UP)

        if inst == "PAGEDOWN":
            kbd.send(Keycode.PAGE_DOWN)

        if inst == "PRINTSCREEN":
            kbd.send(Keycode.PRINT_SCREEN)

        if inst == "SCROLLLOCK":
            kbd.send(Keycode.SCROLL_LOCK)

        if inst == "SPACE":
            kbd.send(Keycode.SPACEBAR)

        if inst == "TAB":
            kbd.send(Keycode.TAB)

        if inst == "FN":
            print("FN Instruction can't be implimented, CircuitPython doesn't provide the macOS FN keycode, this is pretty useless anyway")

        global previous_line
        if inst == "REPEAT":
            try:
                for _ in range(int(args[1])):
                    process_line(previous_line)
            except ValueError:
                print("Invalid integer")
                return
        else:
            previous_line = line

for line in lines:
    process_line(line)
