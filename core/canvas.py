# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .formula import profile, cutterRuote, harmonic, cycloidal

class camProfile(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setParent(parent)
        self.parama = {
            'Rb':3, 'H':1, 'Rc':0.5, 'rate':50,
            'profile':[], 'cutterRoute':[],
            }
        self.showBase = True
        self.showCutterRoute = True
        self.rotate = 0
    
    def setRate(self, rate):
        self.parama['rate'] = rate+50
        self.update()
    def setAngle(self, angle):
        self.rotate = angle
        self.update()
    def setShowBase(self, isShow):
        self.showBase = isShow
        self.update()
    def setShowCutterRoute(self, isShow):
        self.showCutterRoute = isShow
        self.update()
    def changeType(self, isHarmonic):
        if isHarmonic:
            H = harmonic(self.parama['H'])
            Rb = self.parama['Rb']
            Rc = self.parama['Rc']
            self.parama['profile'] = profile(Rb, H)
            self.parama['cutterRoute'] = cutterRuote(Rb, H, Rc)
        else:
            self.parama['profile'] = profile(self.parama['Rb'], cycloidal(self.parama['H']))
            self.parama['cutterRoute'] = cutterRuote(self.parama['Rb'], cycloidal(self.parama['H']), self.parama['Rc'])
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), QBrush(Qt.white))
        painter.translate(self.width()/2, self.height()/2)
        pen = QPen()
        #center circle
        pen.setColor(Qt.red)
        pen.setWidth(3)
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        r = 10
        painter.drawEllipse(QPointF(0, 0), r, r)
        #Base circle
        if self.showBase:
            pen.setColor(Qt.cyan)
            pen.setWidth(3)
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
            r = self.parama['Rb']*self.parama['rate']
            painter.drawEllipse(QPointF(0, 0), r, r)
        #rotate
        rotate = QTransform()
        rotate.translate(0, 0)
        rotate.rotate(self.rotate)
        #profile
        pen.setColor(Qt.blue)
        pen.setWidth(5)
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)
        painterpath_profile = QPainterPath()
        painterpath_profile.moveTo(QPoint(
            self.parama['profile'][0]['Rx']*self.parama['rate'],
            self.parama['profile'][0]['Ry']*self.parama['rate']))
        for i in range(len(self.parama['profile'])):
            e = self.parama['profile'][i]
            x = e['Rx']*self.parama['rate']
            y = e['Ry']*self.parama['rate']
            print(x, y)
            painterpath_profile.lineTo(QPointF(x, y))
        painter.drawPath(rotate.map(painterpath_profile))
        #route
        if self.showCutterRoute:
            pen.setColor(Qt.green)
            pen.setWidth(3)
            pen.setStyle(Qt.DashLine)
            painter.setPen(pen)
            painterpath_route = QPainterPath()
            painterpath_route.moveTo(QPoint(
                self.parama['cutterRoute'][0]['Rx']*self.parama['rate'],
                self.parama['cutterRoute'][0]['Ry']*self.parama['rate']))
            for i in range(len(self.parama['cutterRoute'])):
                e = self.parama['cutterRoute'][i]
                x = e['Rx']*self.parama['rate']
                y = e['Ry']*self.parama['rate']
                painterpath_route.lineTo(QPointF(x, y))
            painter.drawPath(rotate.map(painterpath_route))
