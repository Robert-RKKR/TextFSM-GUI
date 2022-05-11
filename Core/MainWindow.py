import textfsm
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QVBoxLayout, QWidget, QAction, QFileDialog

from Core.TextEdit import TextEdit
from Core.FileOperator import FileOperator
from functions.data import language
from functions.data import actionDict


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # MAIN WINDOW CONFIGURATION:
        self.actionsObjectDict = {}
        self.setWindowTitle("- TextFSM tester -")
        self.resize(1100, 800)
        self.setMinimumSize(300, 300)

        # LAYOUTS DEFINITIONS:
        layoutMain = QVBoxLayout()
        layoutTop = QHBoxLayout()

        # TEXT:
        self.textExample = TextEdit()
        self.textExample.setPlaceholderText(language("textExample"))

        self.textTemplate = TextEdit()
        self.textTemplate.setPlaceholderText(language("textTemplate"))

        self.textOutput = TextEdit()
        self.textOutput.setPlaceholderText(language("textOutput"))
        self.textOutput.setReadOnly(True)

        # ACTIONS:
        self.textExample.textChanged.connect(self.combain)
        self.textTemplate.textChanged.connect(self.combain)

        # ADD TEXT TO LAYOUTS:
        layoutTop.addWidget(self.textExample)
        layoutTop.addWidget(self.textOutput)
        layoutMain.addLayout(layoutTop)
        layoutMain.addWidget(self.textTemplate)

        # ADD WIDGET TO MAIN WINDOW:
        mainWidget = QWidget()
        mainWidget.setLayout(layoutMain)
        self.setCentralWidget(mainWidget)

        # ACTIONS:
        self.createActions()

        # MAIN MENU:
        menu = self.menuBar()
        fileMenu = menu.addMenu(language("file"))
        fileMenu.addAction(self.actionsObjectDict["openAction"])

        optionsMenu = menu.addMenu(language("options"))
        optionsMenu.addAction(self.actionsObjectDict["openAction"])

    def createActions(self):
        openAction = QAction(QIcon("icon/newspaper--plus.png"), language("action_open"), self)
        openAction.triggered.connect(self.openFileM)
        self.actionsObjectDict["openAction"] = openAction

    def openFileM(self):
        openFile = QFileDialog.getOpenFileName(self, "Open File")
        file = open(openFile[0], "r")
        self.textTemplate.setText(file.read())


    def combain(self):
        self.saveTemplate()

        output = []
        try:
            with open("template.temp") as template:
                fsm = textfsm.TextFSM(template)
                fsmResult = fsm.ParseText(self.textExample.toPlainText())

            for row in fsmResult:
                output.append(dict(zip(fsm.header, row)))
        except:
            output = "Error"

        print(output)

        outputString = ""
        for outputDict in output:
            if type(outputDict) is dict:
                for row in outputDict:
                    if type(outputDict[row]) is list:
                        for i in outputDict[row]:
                            outputString = outputString + f"    {i}\n"
                    else:
                        outputString = outputString + f"{row}: {outputDict[row]}\n"
                outputString = outputString + "\n------------------------\n\n"
        self.textOutput.setText(str(outputString))

    def saveTemplate(self):
        template = self.textTemplate.toPlainText()
        try:
            file = open("template.temp", "w")
            try:
                file.write(template)
            finally:
                file.close()
        except:
            print("Error file write!")
