import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from keyboard import keycode_dict

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
            return
        
        global default_delay
        global previous_line

        if default_delay > 0:
            time.sleep(default_delay / 1000)

        if inst == "DEFAULT_DELAY" or inst == "DEFAULTDELAY":
            try:
                default_delay = int(args[1])
            except ValueError:
                print("Invalid integer")
                return
        elif inst == "DELAY":
            try:
                time.sleep(int(args[1]) / 1000)
            except ValueError:
                print("Invalid integer")
                return
        elif inst == "STRING":
            layout.write(args[1])
        elif inst == "GUI" or inst == "WINDOWS":
            kbd.send(Keycode.WINDOWS, keycode_dict.get(args[1].upper()))
        elif inst == "APP" or inst == "MENU":
            kbd.send(Keycode.APPLICATION)
        elif inst == "SHIFT":
            kbd.send(Keycode.SHIFT, keycode_dict.get(args[1].upper()))
        elif inst == "ALT":
            kbd.send(Keycode.ALT, keycode_dict.get(args[1].upper()))
        elif inst == "CONTROL" or inst == "CTRL":
            kbd.send(Keycode.CONTROL, keycode_dict.get(args[1].upper()))
        elif inst == "DOWNARROW" or inst == "DOWN":
            kbd.send(Keycode.DOWN_ARROW)
        elif inst == "LEFTARROW" or inst == "LEFT":
            kbd.send(Keycode.LEFT_ARROW)
        elif inst == "RIGHTARROW" or inst == "RIGHT":
            kbd.send(Keycode.RIGHT_ARROW)
        elif inst == "UPARROW" or inst == "UP":
            kbd.send(Keycode.UP_ARROW)
        elif inst == "BREAK" or inst == "PAUSE":
            kbd.send(Keycode.PAUSE)
        elif inst == "CAPSLOCK":
            kbd.send(Keycode.CAPS_LOCK)
        elif inst == "DELETE":
            kbd.send(Keycode.DELETE)
        elif inst == "ENTER" or inst == "RETURN":
            kbd.send(Keycode.ENTER) 
        elif inst == "ESC" or inst == "ESCAPE":
            kbd.send(Keycode.ESCAPE)
        elif inst == "HOME":
            kbd.send(Keycode.HOME)
        elif inst == "INSERT":
            kbd.send(Keycode.INSERT)
        elif inst == "NUMLOCK":
            kbd.send(Keycode.KEYPAD_NUMLOCK)
        elif inst == "PAGEUP":
            kbd.send(Keycode.PAGE_UP)
        elif inst == "PAGEDOWN":
            kbd.send(Keycode.PAGE_DOWN)
        elif inst == "PRINTSCREEN":
            kbd.send(Keycode.PRINT_SCREEN)
        elif inst == "SCROLLLOCK":
            kbd.send(Keycode.SCROLL_LOCK)
        elif inst == "SPACE":
            kbd.send(Keycode.SPACEBAR)
        elif inst == "TAB":
            kbd.send(Keycode.TAB)
        elif inst == "FN":
            print("FN Instruction can't be implimented, CircuitPython doesn't provide the macOS FN keycode, this is pretty useless anyway")
        elif inst == "REPEAT":
            try:
                for _ in range(int(args[1])):
                    process_line(previous_line)
            except ValueError:
                print("Invalid integer")

        previous_line = line

for line in lines:
    process_line(line)

