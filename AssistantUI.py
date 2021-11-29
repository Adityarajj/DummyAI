from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AssistantUI(object):
    def setupUi(self, AssistantUI):
        AssistantUI.setObjectName("AssistantUI")
        AssistantUI.resize(1050, 722)
        self.centralwidget = QtWidgets.QWidget(AssistantUI)
        self.centralwidget.setObjectName("centralwidget")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(40, 590, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.StartButton.setCheckable(False)
        self.StartButton.setObjectName("StartButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(250, 590, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("background-color: rgb(255, 0, 4);")
        self.ExitButton.setCheckable(False)
        self.ExitButton.setObjectName("ExitButton")
        self.Bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.Bg_1.setGeometry(QtCore.QRect(0, 0, 1051, 721))
        self.Bg_1.setText("")
        self.Bg_1.setPixmap(QtGui.QPixmap("../../../../Downloads/VFmTa6.png"))
        self.Bg_1.setScaledContents(True)
        self.Bg_1.setObjectName("Bg_1")
        self.gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(0, 10, 1041, 701))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap("Gif1.gif"))
        self.gif_1.setScaledContents(True)
        self.gif_1.setObjectName("gif_1")
        self.Bg_1.raise_()
        self.gif_1.raise_()
        self.StartButton.raise_()
        self.ExitButton.raise_()
        AssistantUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(AssistantUI)
        QtCore.QMetaObject.connectSlotsByName(AssistantUI)

    def retranslateUi(self, AssistantUI):
        _translate = QtCore.QCoreApplication.translate
        AssistantUI.setWindowTitle(_translate("AssistantUI", "MainWindow"))
        self.StartButton.setText(_translate("AssistantUI", "START"))
        self.ExitButton.setText(_translate("AssistantUI", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AssistantUI = QtWidgets.QMainWindow()
    ui = Ui_AssistantUI()
    ui.setupUi(AssistantUI)
    AssistantUI.show()
    sys.exit(app.exec_())
