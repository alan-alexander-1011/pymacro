import pyautogui
import time
from pynput import keyboard
import json
import os

special_keys = {
    "lshift": "shift",
    "rshift": "shift_r",
    "lctrl": "ctrl_l",
    "rctrl": "ctrl_r",
    "lalt": "alt_l",
    "ralt": "alt_gr",
    "backspace": "backspace",
    "tab": "tab",
    "enter": "enter",
    "esc": "esc",
    "insert": "insert",
    "delete": "delete",
    "home": "home",
    "end": "end",
    "pageup": "pageup",
    "pagedown": "pagedown",
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "f1": "f1",
    "f2": "f2",
    "f3": "f3",
    "f4": "f4",
    "f5": "f5",
    "f6": "f6",
    "f7": "f7",
    "f8": "f8",
    "f9": "f9",
    "f10": "f10",
    "f11": "f11",
    "f12": "f12",
    "capslock": "caps_lock",
    "numlock": "num_lock",
    "scrolllock": "scroll_lock",
    "printscreen": "print_screen",
    "pause": "pause",
    "menu": "menu",
    "space": "space",
    "quote": "quote",
    "backquote": "backquote",
    "tilde": "~",
    "comma": ",",
    "period": ".",
    "slash": "/",
    "backslash": "\\",
    "semicolon": ";",
    "lbracket": "(",
    "rbracket": ")",
    "minus": "-",
    "equals": "=",
    "lparen": "(",
    "rparen": ")",
    "underscore": "_",
    "plus": "+",
    "asterisk": "*",
    "ampersand": "&",
    "caret": "^",
    "percent": "%",
    "dollar": "$",
    "hash": "#",
    "at": "@",
    "exclamation": "!",
    "colon": ":",
    "question": "?",
    "bar": "|",
    "greater": ">",
    "less": "<",
    "doublequote": "\"",
    "backtick": "`",
    "braceleft": "{",
    "braceright": "}",
    "bracketleft": "(",
    "bracketright": ")",
    "pipe": "|",
    "singlequote": "'",
}

err_flag = False
print("macros:")
for macrofile in os.listdir("./macros"):
    with open(f"./macros/{macrofile}", "r") as f:
        try:
            bind = json.load(f)["bind"]
            print(f"macro \"{os.path.splitext(macrofile)[0]}\" binded to {bind}")
        except IndexError:
            err_flag = not err_flag
            pyautogui.alert(f"macro \"{os.path.splitext(macrofile)[0]}\" doesnt have a bind")
        except json.JSONDecodeError:
            err_flag = not err_flag
            pyautogui.alert(f"macro \"{os.path.splitext(macrofile)[0]}\" doesnt have anything in it.")

if err_flag:
    exit(-1)

pyautogui.FAILSAFE = True

def on_click(key):
    for macrofile in os.listdir("./macros"):
        with open(f"./macros/{macrofile}", "r") as f:
            data = json.load(f)
        
        # Extract key without single quotes if present
        if isinstance(key, keyboard.KeyCode) and str(key).startswith("'") and str(key).endswith("'"):
            pressed_key = str(key).split("'")[-2]
        else:
            pressed_key = special_keys.get(str(key).split(".")[-1], str(key).split(".")[-1])
        if special_keys.get(data["bind"], data["bind"]) == pressed_key:
            macros:list[str] = data["macro"].lower().split(";")
            for macro in macros:
                macro = macro.strip()
                if macro.find("move_mouse") != -1:
                    arg = macro.split("move_mouse")[-1]
                    if arg.find("left") != -1 or arg.find("right") != -1 or arg.find("up") != -1 or arg.find("down") != -1:
                        if arg.find("up") != -1:
                            yoff = -int(arg.split("up")[1])
                        elif arg.find("down") != -1:
                            yoff = int(arg.split("down")[1])
                        else:
                            yoff=0

                        if arg.find("left") != -1:
                            xoff = -int(arg.split("left")[1])
                        elif arg.find("right") != -1:
                            xoff = int(arg.split("right")[1])
                        else:
                            xoff=0

                        pyautogui.moveRel(xoff, yoff)
                    else:
                        pyautogui.moveTo(int(arg.split(",")[0]), int(arg.split(",")[-1]))
                elif macro.find("keydown ") != -1:
                    arg = macro.split("keydown ")[-1]
                    pyautogui.keyDown(special_keys.get(arg, arg))
                elif macro.find("keyup ") != -1:
                    arg = macro.split("keyup ")[-1]
                    pyautogui.keyUp(special_keys.get(arg, arg))
                elif macro.find("delay ") != -1:
                    arg = macro.split("delay ")[-1]
                    time.sleep(float(arg))
                elif macro.find("type ") != -1:
                    arg = macro.split("type ")[-1]
                    pyautogui.typewrite(arg,0.009)
                else:
                    k=special_keys.get(macro, macro)
                    pyautogui.keyDown(k)
                    #time.sleep(0.098)
                    pyautogui.keyUp(k)

with keyboard.Listener(on_press=on_click) as listener:
    listener.join()
