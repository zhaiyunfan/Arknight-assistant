import sys
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

import Window

def init(ui):
    ui.spinBoxHead.maximum = ui.spinBoxMax.value
    input = ui.spinBoxHead.value
    timeLeft = 0
    timeLeft = input * 6
    hourLeft = 0
    hourLeft = timeLeft % 60
    minuiteLeft = timeLeft - 60 * hourLeft
    ui.lcdNumberHour.intValue = int(hourLeft)
    ui.lcdNumbermin.intValue = int(minuiteLeft)
    time = QTime.currentTime()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.spinBoxHead.maximum = ui.spinBoxMax.value
    ui.pushButton.clicked.connect(partial(init, ui))
    # ui.actionExit.triggered.connect(partial(clickExit, app))
    sys.exit(app.exec_())

