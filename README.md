# **PYmacro**

## **a macro system in python**

remember to `python.exe -m pip -r requirements.txt`
---
### __**How to use**__:
for using macro: run the program and press the bind key

For macro makers:
You need to know basics of json.\
Template for a macro:
```json
{
    "bind": "your_bind_key",
    "macro": "your_macro"
}
```
These are the bind for macro:
```python
[
    "lshift","shift",
    "rshift","shift_r",
    "lctrl","ctrl_l",
    "rctrl","ctrl_r",
    "lalt","alt_l",
    "ralt","alt_gr",
    "backspace",
    "tab",
    "enter",
    "esc",
    "insert",
    "delete",
    "home",
    "end",
    "pageup","pagedown",
    "up",
    "down",
    "left",
    "right",
    "f1",
    "f2",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "f10",
    "f11",
    "f12",
    "capslock""caps_lock",
    "numlock","num_lock",
    "scrolllock","scroll_lock",
    "printscreen","print_screen",
    "pause",
    "menu",
    "space",
    "quote","'",
    "backquote","`",
    "tilde","~",
    "comma", "," ,
    "period",".",
    "slash","/",
    "backslash","\\",
    "semicolon",";",
    "lbracket","(",
    "rbracket",")",
    "minus","-",
    "equals","=",
    "underscore","_",
    "plus","+",
    "asterisk","*",
    "ampersand","&",
    "caret","^",
    "percent","%",
    "dollar","$",
    "hash","#",
    "at","@",
    "exclamation","!",
    "colon",":",
    "question","?",
    "bar","|",
    "greater",">",
    "less","<",
    "doublequote","\"",
    "backtick","`",
    "braceleft","{",
    "braceright","}",
    "bracketleft","(",
    "bracketright",")",
    "pipe","|",
    "singlequote","'"
]
```

These are the commands for the macro:
```
    move_mouse [left,up,right,down][pixels]
    move_mouse [position in pixels]
    keydown [key]
    keyup [key]
    delay [amount in seconds, can be float]
    type [text]
    (or just the character for the key to press, but every  
     single character will be separated by a semicolon)
```

You can have multiple commands, you need to seperate them using semicolons