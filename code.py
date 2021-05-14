import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

default_delay = 0
previous_line = ''

def press(k):
    if len(k) == 1:
        layout.write(k[0])
    elif k == 'ENTER' or k == 'RETURN':
        kbd.press(Keycode.ENTER)
    elif k == 'ESC' or k == 'ESCAPE':
        kbd.press(Keycode.ESCAPE)
    elif k == 'BACKSPACE':
        kbd.press(Keycode.BACKSPACE)
    elif k == 'TAB':
        kbd.press(Keycode.TAB)
    elif k == 'SPACE' or k == 'SPACEBAR':
        kbd.press(Keycode.SPACEBAR)
    elif k == 'MINUS':
        kbd.press(Keycode.MINUS)
    elif k == 'EQUAL' or k == 'EQUALS':
        kbd.press(Keycode.EQUALS)
    elif k == 'LEFT_BRACKET' or k == 'LEFTBRACKET':
        kbd.press(Keycode.LEFT_BRACKET)
    elif k == 'RIGHT_BRACKET' or k == 'RIGHTBRACKET':
        kbd.press(Keycode.RIGHT_BRACKET)
    elif k == 'BACKSLASH':
        kbd.press(Keycode.BACKSLASH)
    elif k == 'POUND':
        kbd.press(Keycode.POUND)
    elif k == 'SEMICOLON':
        kbd.press(Keycode.SEMICOLON)
    elif k == 'QUOTE':
        kbd.press(Keycode.QUOTE)
    elif k == 'TILDE':
        kbd.press(Keycode.GRAVE_ACCENT)
    elif k == 'COMMA':
        kbd.press(Keycode.COMMA)
    elif k == 'PERIOD':
        kbd.press(Keycode.PERIOD)
    elif k == 'SLASH' or k == 'FORWARD_SLASH' or k == 'FORWARDSLASH':
        kbd.press(Keycode.FORWARD_SLASH)
    elif k == 'CAPS' or k == 'CAPS_LOCK' or k == 'CAPSLOCK':
        kbd.press(Keycode.CAPS_LOCK)
    elif k == 'PRINT' or k == 'PRINT_SCREEN' or k == 'PRINTSCREEN':
        kbd.press(Keycode.PRINT_SCREEN)
    elif k == 'SCROLL' or k == 'SCROLL_LOCK' or k == 'SCROLLLOCK':
        kbd.press(Keycode.SCROLL_LOCK)
    elif k == 'PAUSE' or k == 'BREAK':
        kbd.press(Keycode.PAUSE)
    elif k == 'INSERT':
        kbd.press(Keycode.INSERT)
    elif k == 'HOME':
        kbd.press(Keycode.HOME)
    elif k == 'PAGE_UP' or k == 'PAGEUP':
        kbd.press(Keycode.PAGE_UP)
    elif k == 'DELETE':
        kbd.press(Keycode.DELETE)
    elif k == 'END':
        kbd.press(Keycode.END)
    elif k == 'PAGE_DOWN' or k == 'PAGEDOWN':
        kbd.press(Keycode.PAGE_DOWN)
    elif k == 'RIGHT' or k == 'RIGHT_ARROW' or k == 'RIGHTARROW':
        kbd.press(Keycode.RIGHT_ARROW)
    elif k == 'LEFT' or k == 'LEFT_ARROW' or k == 'LEFTARROW':
        kbd.press(Keycode.LEFT_ARROW)
    elif k == 'DOWN' or k == 'DOWN_ARROW' or k == 'DOWNARROW':
        kbd.press(Keycode.DOWN_ARROW)
    elif k == 'UP' or k == 'UP_ARROW' or k == 'UPARROW':
        kbd.press(Keycode.UP_ARROW)
    elif k == 'NUM' or k == 'NUM_LOCK' or k == 'NUMLOCK':
        kbd.press(Keycode.NUM_LOCK)
    elif k == 'APPLICATION' or k == 'MENU':
        kbd.press(Keycode.APPLICATION)
    elif k == 'LEFT_CONTROL' or k == 'CONTROL' or k == 'CTRL':
        kbd.press(Keycode.LEFT_CONTROL)
    elif k == 'LEFT_SHIFT' or k == 'SHIFT':
        kbd.press(Keycode.LEFT_SHIFT)
    elif k == 'LEFT_GUI' or k == 'GUI':
        kbd.press(Keycode.LEFT_GUI)
    elif k == 'LEFT_WINDOWS' or k == 'WINDOWS':
        kbd.press(Keycode.WINDOWS)
    elif k == 'RIGHT_CONTROL':
        kbd.press(Keycode.RIGHT_CONTROL)
    elif k == 'RIGHT_SHIFT':
        kbd.press(Keycode.RIGHT_SHIFT)
    elif k == 'RIGHT_ALT':
        kbd.press(Keycode.RIGHT_ALT)
    elif k == 'RIGHT_GUI':
        kbd.press(Keycode.RIGHT_GUI)
    elif k == 'F1':
        kbd.press(Keycode.F1)
    elif k == 'F2':
        kbd.press(Keycode.F2)
    elif k == 'F3':
        kbd.press(Keycode.F3)
    elif k == 'F4':
        kbd.press(Keycode.F4)
    elif k == 'F5':
        kbd.press(Keycode.F5)
    elif k == 'F6':
        kbd.press(Keycode.F6)
    elif k == 'F7':
        kbd.press(Keycode.F7)
    elif k == 'F8':
        kbd.press(Keycode.F8)
    elif k == 'F9':
        kbd.press(Keycode.F9)
    elif k == 'F10':
        kbd.press(Keycode.F10)
    elif k == 'F11':
        kbd.press(Keycode.F11)
    elif k == 'F12':
        kbd.press(Keycode.F12)
    elif k == 'F13':
        kbd.press(Keycode.F13)
    elif k == 'F14':
        kbd.press(Keycode.F14)
    elif k == 'F15':
        kbd.press(Keycode.F15)
    elif k == 'F16':
        kbd.press(Keycode.F16)
    elif k == 'F17':
        kbd.press(Keycode.F17)
    elif k == 'F18':
        kbd.press(Keycode.F18)
    elif k == 'F19':
        kbd.press(Keycode.F19)

def process(line):
    args = line.split(' ', 1)
    inst = args[0]

    if inst == 'REM':
        return

    global default_delay
    global previous_line

    if default_delay > 0:
        time.sleep(default_delay / 1000)

    if inst == 'DEFAULT_DELAY' or inst == 'DEFAULTDELAY':
        try:
            default_delay = int(args[1])
        except ValueError:
            return
    elif inst == 'DELAY':
        try:
            time.sleep(int(args[1]) / 1000)
        except ValueError:
            return
    elif inst == 'STRING_DELAY' or inst == 'STRINGDELAY':
        try:
            args_1 = args[1].split(' ', 1)
            for c in args_1[1]:
                layout.write(c)
                time.sleep(int(args_1[0]) / 1000)
        except ValueError:
            return
    elif inst == 'STRING':
        layout.write(args[1])
    elif inst == 'REPEAT':
        try:
            for _ in range(int(args[1])):
                process(previous_line)
        except ValueError:
            return
    else:
        press(inst)
        if len(args) > 1:
            for s in args[1].split(' '):
                press(s)

    previous_line = line

    kbd.release_all()

with open('payload.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        process(line)
