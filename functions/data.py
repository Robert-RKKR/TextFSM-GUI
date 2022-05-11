
languageDict = {
    "textExample": "String text",
    "textTemplate": "FSM template string",
    "textOutput": "FSM Output",
    "action_open": "Open template",
    "file": "Templates",
    "options": "Options"
}

actionDict = {
    "File": {
        "name": "File",
        #"action": "self.myToolBarClick1",
        "icon": "application--plus.png",
        "description": "Opis przycisku File",
        #"keyShortcut": "QKeySequence.Copy",
        "toolBar": True,
        "checkable": True
    }
}


def language(key):
    return languageDict.get(key, "None")