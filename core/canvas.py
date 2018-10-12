# -*- coding: utf-8 -*-

from core.QtModules import (
    Qt,
    QWidget,
    QPainter,
    QBrush,
    QPen,
    QPoint,
    QPointF,
    QTransform,
    QPainterPath,
)
from .formula import profile, cutter_route, harmonic, cycloidal


class CamProfile(QWidget):

    """Main widget of cam."""

    def __init__(self, parent: QWidget = None):
        super(CamProfile, self).__init__(parent)
        self.parama = {
            'rb': 3,
            'h': 1,
            'rc': 0.5,
            'rate': 50,
            'profile': [],
            'cutter_route': [],
        }
        self.show_base = True
        self.show_cutter_route = True
        self.rotate = 0
        self.mode = 0
        self.reload()

    def set_base(self, base):
        self.parama['rb'] = base
        self.reload()

    def set_h(self, h):
        self.parama['h'] = h
        self.reload()

    def set_rc(self, rc):
        self.parama['rc'] = rc
        self.reload()

    def set_rate(self, rate: float):
        self.parama['rate'] = rate + 20
        self.update()

    def set_angle(self, angle: float):
        self.rotate = angle
        self.update()

    def set_show_base(self, is_show: bool):
        self.show_base = is_show
        self.update()

    def set_show_cutter_route(self, is_show: bool):
        self.show_cutter_route = is_show
        self.update()

    def set_mode(self, type_i: int):
        self.mode = type_i
        self.reload()

    def reload(self):
        rb = self.parama['rb']
        rc = self.parama['rc']
        if self.mode == 0:
            h = harmonic(self.parama['h'])
            self.parama['profile'] = profile(rb, h)
            self.parama['cutter_route'] = cutter_route(rb, h, rc)
        elif self.mode == 1:
            h = cycloidal(self.parama['h'])
            self.parama['profile'] = profile(rb, h)
            self.parama['cutter_route'] = cutter_route(rb, h, rc)
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), QBrush(Qt.white))
        painter.translate(self.width() / 2, self.height() / 2)

        if not self.parama['profile']:
            painter.end()
            return

        pen = QPen()

        # center circle
        pen.setColor(Qt.red)
        pen.setWidth(3)
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        r = 10
        painter.drawEllipse(QPointF(0, 0), r, r)

        # Base circle
        if self.show_base:
            pen.setColor(Qt.cyan)
            pen.setWidth(3)
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
            r = self.parama['rb'] * self.parama['rate']
            painter.drawEllipse(QPointF(0, 0), r, r)

        # rotate
        rotate = QTransform()
        rotate.translate(0, 0)
        rotate.rotate(self.rotate)

        # profile
        pen.setColor(Qt.blue)
        pen.setWidth(5)
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        path_profile = QPainterPath()
        path_profile.moveTo(QPoint(
            self.parama['profile'][0]['Rx'] * self.parama['rate'],
            self.parama['profile'][0]['Ry'] * self.parama['rate'])
        )
        for i in range(len(self.parama['profile'])):
            e = self.parama['profile'][i]
            x = e['Rx'] * self.parama['rate']
            y = e['Ry'] * self.parama['rate']
            path_profile.lineTo(QPointF(x, y))
        painter.drawPath(rotate.map(path_profile))
        # route
        if self.show_cutter_route:
            pen.setColor(Qt.green)
            pen.setWidth(3)
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
            painterpath_route = QPainterPath()
            painterpath_route.moveTo(QPoint(
                self.parama['cutter_route'][0]['Rx']*self.parama['rate'],
                self.parama['cutter_route'][0]['Ry']*self.parama['rate']))
            for i in range(len(self.parama['cutter_route'])-self.rotate):
                e = self.parama['cutter_route'][i]
                x = e['Rx']*self.parama['rate']
                y = e['Ry']*self.parama['rate']
                painterpath_route.lineTo(QPointF(x, y))
            painter.drawPath(rotate.map(painterpath_route))
        # roll
        pen.setColor(Qt.darkGray)
        pen.setWidth(3)
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        r = self.parama['rc']*self.parama['rate']
        last_point = QPointF(
            self.parama['cutter_route'][-self.rotate]['Rx']*self.parama['rate'],
            self.parama['cutter_route'][-self.rotate]['Ry']*self.parama['rate'])
        path_roll = QPainterPath()
        path_roll.addEllipse(last_point, r, r)
        painter.drawPath(rotate.map(path_roll))
        painter.end()
