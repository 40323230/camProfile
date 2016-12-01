# -*- coding: utf-8 -*-
'''
Copyright (C) 2016 Yuan Chang
E-mail: daan0014119@gmail.com
'''
from sys import exit, argv
from PyQt5.QtWidgets import QApplication
from core.main import MainWindow

#Start Cam
if __name__=="__main__":
    QApplication.setStyle("fusion")
    app = QApplication(argv)
    run  = MainWindow()
    run.show()
    exit(app.exec())
