import sys
import textfsm
from PyQt5.QtWidgets import QApplication
from Core.MainWindow import MainWindow


def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()
