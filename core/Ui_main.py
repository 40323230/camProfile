# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kmol/桌面/camProfile/core/main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toHar = QtWidgets.QRadioButton(self.centralWidget)
        self.toHar.setChecked(True)
        self.toHar.setObjectName("toHar")
        self.horizontalLayout_2.addWidget(self.toHar)
        self.toCy = QtWidgets.QRadioButton(self.centralWidget)
        self.toCy.setObjectName("toCy")
        self.horizontalLayout_2.addWidget(self.toCy)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.showBase = QtWidgets.QCheckBox(self.centralWidget)
        self.showBase.setChecked(True)
        self.showBase.setObjectName("showBase")
        self.horizontalLayout.addWidget(self.showBase)
        self.showRoute = QtWidgets.QCheckBox(self.centralWidget)
        self.showRoute.setChecked(True)
        self.showRoute.setObjectName("showRoute")
        self.horizontalLayout.addWidget(self.showRoute)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.liftVal = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.liftVal.setMinimum(0.01)
        self.liftVal.setMaximum(10.0)
        self.liftVal.setProperty("value", 1.0)
        self.liftVal.setObjectName("liftVal")
        self.horizontalLayout.addWidget(self.liftVal)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cutterRadiusVal = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.cutterRadiusVal.setMinimum(0.01)
        self.cutterRadiusVal.setMaximum(10.0)
        self.cutterRadiusVal.setProperty("value", 0.5)
        self.cutterRadiusVal.setObjectName("cutterRadiusVal")
        self.horizontalLayout.addWidget(self.cutterRadiusVal)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_3.addWidget(self.horizontalSlider_2)
        self.spinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.canvasLayout = QtWidgets.QVBoxLayout()
        self.canvasLayout.setObjectName("canvasLayout")
        self.horizontalLayout_4.addLayout(self.canvasLayout)
        self.verticalSlider = QtWidgets.QSlider(self.centralWidget)
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(10)
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_4.addWidget(self.verticalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toHar.setText(_translate("MainWindow", "Harmonic"))
        self.toCy.setText(_translate("MainWindow", "Cycloidal"))
        self.showBase.setText(_translate("MainWindow", "Base circle"))
        self.showRoute.setText(_translate("MainWindow", "Cutter Route"))
        self.label_2.setText(_translate("MainWindow", "Lift (inch):"))
        self.label.setText(_translate("MainWindow", "Cutter radius:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

