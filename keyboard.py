from adafruit_hid.keycode import Keycode

keycode_dict = {
    # Letters
    "A": Keycode.A,
    "B": Keycode.B,
    "C": Keycode.C,
    "D": Keycode.D,
    "E": Keycode.E,
    "F": Keycode.F,
    "G": Keycode.G,
    "H": Keycode.H,
    "I": Keycode.I,
    "J": Keycode.J,
    "K": Keycode.K,
    "L": Keycode.L,
    "M": Keycode.M,
    "N": Keycode.N,
    "O": Keycode.O,
    "P": Keycode.P,
    "Q": Keycode.Q,
    "R": Keycode.R,
    "S": Keycode.S,
    "T": Keycode.T,
    "U": Keycode.U,
    "V": Keycode.V,
    "W": Keycode.W,
    "X": Keycode.X,
    "Y": Keycode.Y,
    "Z": Keycode.Z,
    # Numbers
    "1": Keycode.ONE,
    "2": Keycode.TWO,
    "3": Keycode.THREE,
    "4": Keycode.FOUR,
    "5": Keycode.FIVE,
    "6": Keycode.SIX,
    "7": Keycode.SEVEN,
    "8": Keycode.EIGHT,
    "9": Keycode.NINE,
    "0": Keycode.ZERO,
    # Alt Numbers
    "!": Keycode.ONE,
    "@": Keycode.TWO,
    "#": Keycode.THREE,
    "$": Keycode.FOUR,
    "%": Keycode.FIVE,
    "^": Keycode.SIX,
    "&": Keycode.SEVEN,
    "*": Keycode.EIGHT,
    "(": Keycode.NINE,
    ")": Keycode.ZERO,
    # Symbols
    "`": Keycode.GRAVE_ACCENT,
    "=": Keycode.EQUALS,
    "-": Keycode.MINUS,
    "'": Keycode.QUOTE,
    ";": Keycode.SEMICOLON,
    ",": Keycode.COMMA,
    ".": Keycode.PERIOD,
    "/": Keycode.FORWARD_SLASH,
    "\\": Keycode.BACKSLASH,
    # Alt Symbols
    "~": Keycode.GRAVE_ACCENT,
    "+": Keycode.EQUALS,
    "_": Keycode.MINUS,
    "\"": Keycode.QUOTE,
    ":": Keycode.SEMICOLON,
    "<": Keycode.COMMA,
    ">": Keycode.PERIOD,
    "?": Keycode.FORWARD_SLASH,
    "|": Keycode.BACKSLASH,
    # Special
    "ENTER": Keycode.ENTER,
    "RETURN": Keycode.RETURN,
    "ESCAPE": Keycode.ESCAPE,
    "ESC": Keycode.ESCAPE,
    "BACKSPACE": Keycode.BACKSPACE,
    "TAB": Keycode.TAB,
    "SPACEBAR": Keycode.SPACEBAR,
    "SPACE": Keycode.SPACE,
    "INSERT": Keycode.INSERT,
    "HOME": Keycode.HOME,
    "PAGEUP": Keycode.PAGE_UP,
    "PAGEDOWN": Keycode.PAGE_DOWN,
    "DELETE": Keycode.DELETE,
    "END": Keycode.END,
    "RIGHTARROW": Keycode.RIGHT_ARROW,
    "LEFTARROW": Keycode.LEFT_ARROW,
    "DOWNARROW": Keycode.DOWN_ARROW,
    "UPARROW": Keycode.UP_ARROW,
    "GUI": Keycode.WINDOWS,
    "WINDOWS": Keycode.WINDOWS,
    "COMMAND": Keycode.WINDOWS,
    "PAUSE": Keycode.PAUSE,
    "BREAK": Keycode.PAUSE,
    # Function Keys
    "F1": Keycode.F1,
    "F2": Keycode.F2,
    "F3": Keycode.F3,
    "F4": Keycode.F4,
    "F5": Keycode.F5,
    "F6": Keycode.F6,
    "F7": Keycode.F7,
    "F8": Keycode.F8,
    "F9": Keycode.F9,
    "F10": Keycode.F10,
    "F11": Keycode.F11,
    "F12": Keycode.F12,
    # Alt Function Keys (CircuitPython no F20+)
    "F13": Keycode.F13,
    "F14": Keycode.F14,
    "F15": Keycode.F15,
    "F16": Keycode.F16,
    "F17": Keycode.F17,
    "F18": Keycode.F18,
    "F19": Keycode.F19,
}
