# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy import signal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("RLC Circuit")
        MainWindow.resize(850, 637)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(850, 200))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line_R = QtWidgets.QLineEdit(self.frame_2)
        self.line_R.setGeometry(QtCore.QRect(80, 70, 113, 38))
        self.line_R.setObjectName("line_R")
        self.line_L = QtWidgets.QLineEdit(self.frame_2)
        self.line_L.setGeometry(QtCore.QRect(370, 70, 113, 38))
        self.line_L.setObjectName("line_L")
        self.line_C = QtWidgets.QLineEdit(self.frame_2)
        self.line_C.setGeometry(QtCore.QRect(670, 70, 113, 38))
        self.line_C.setObjectName("line_C")
        self.radio_Step = QtWidgets.QRadioButton(self.frame_2)
        self.radio_Step.setGeometry(QtCore.QRect(310, 150, 116, 28))
        self.radio_Step.setObjectName("radio_Step")
        self.radio_Impulse = QtWidgets.QRadioButton(self.frame_2)
        self.radio_Impulse.setGeometry(QtCore.QRect(450, 150, 116, 28))
        self.radio_Impulse.setObjectName("radio_Impulse")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(80, 50, 68, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(370, 50, 68, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(670, 50, 68, 22))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(350, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(350, 16777215))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.canvas)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.draw)
        self.radio_Step.setChecked(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RLC Circuit"))
        self.radio_Step.setText(_translate("MainWindow", "Step"))
        self.radio_Impulse.setText(_translate("MainWindow", "Impulse"))
        self.label.setText(_translate("MainWindow", "R (Ohms"))
        self.label_2.setText(_translate("MainWindow", "L (H)"))
        self.label_3.setText(_translate("MainWindow", "C (F)"))
        self.pushButton.setText(_translate("MainWindow", "Calcular"))
        
    def draw(self):
        R = float(self.line_R.text())
        L = float(self.line_L.text())
        C = float(self.line_C.text())
        
        A = [[-R/L, -1./L], [1./C, 0.]]
        B = [[1/L], [0.]]
        C = [1., 0.]
        D = [0.]

        sys = signal.StateSpace(A,B,C,D)
        
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        if self.radio_Step.isChecked():
            t, y = signal.step(sys)
            plt.title('Step response')
        elif self.radio_Impulse.isChecked():
            t, y = signal.impulse(sys)
            plt.title('Impulse response')
        
        plt.ylabel('Amplitude')
        plt.xlabel('t(s)')
        ax.plot(t,y)
        self.canvas.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

