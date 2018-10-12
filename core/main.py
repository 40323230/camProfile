# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .Ui_main import Ui_MainWindow
from .canvas import CamProfile


class MainWindow(QMainWindow, Ui_MainWindow):

    """Main window."""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.cam_profile = CamProfile()
        self.canvas_layout.addWidget(self.cam_profile)

    @pyqtSlot(name='on_harmonic_mode_clicked')
    def __set_harmonic(self):
        self.cam_profile.change_type(0)

    @pyqtSlot(name='on_cycloidal_mode_clicked')
    def __set_cycloidal(self):
        self.cam_profile.change_type(1)

    @pyqtSlot(bool, name='on_show_base_clicked')
    def __set_show_base(self, checked: bool):
        self.cam_profile.set_show_base(checked)

    @pyqtSlot(bool, name='on_show_route_clicked')
    def __set_show_route(self, checked: bool):
        self.cam_profile.set_show_cutter_route(checked)

    @pyqtSlot(int, name='on_zoom_bar_valueChanged')
    def __set_zoom(self, value: int):
        self.cam_profile.set_rate(value)

    @pyqtSlot(float, name='on_lift_valueChanged')
    def __set_lift(self, p0: float):
        self.cam_profile.set_h(p0)

    @pyqtSlot(float, name='on_cutter_radius_valueChanged')
    def __set_cutter_radius(self, p0: float):
        self.cam_profile.set_rc(p0)

    @pyqtSlot(float, name='on_baseVal_valueChanged')
    def __set_base(self, p0: float):
        self.cam_profile.set_base(p0)

    @pyqtSlot(int, name='on_rotate_angle_valueChanged')
    def __set_rotate_angle(self, p0: int):
        self.rotate_bar.setValue(p0)

    @pyqtSlot(int, name='on_rotate_bar_valueChanged')
    def __set_rotate(self, value: int):
        self.rotate_angle.setValue(value)
        self.cam_profile.set_angle(value)
