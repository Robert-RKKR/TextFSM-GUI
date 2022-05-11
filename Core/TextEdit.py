from PyQt5.QtWidgets import QTextEdit


class TextEdit(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("border: 1px solid gray;")