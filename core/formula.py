# -*- coding: utf-8 -*-

from typing import List, Sequence, Dict
from math import (
    pi,
    radians,
    cos,
    sin,
)


def profile(rb: float, delta_r: Sequence[float]) -> List[Dict[str, float]]:
    profile_list = []
    for phi in range(0, 360):
        profile_list.append({
            'Rx': (rb + delta_r[phi]) * sin(radians(phi)),
            'Ry': -(rb + delta_r[phi]) * cos(radians(phi)),
        })
    return profile_list


def cutter_route(
    rb: float,
    delta_r: Sequence[float],
    rc: float
) -> List[Dict[str, float]]:
    route_list = []
    for phi in range(0, 360):
        route_list.append({
            'Rx': (rb + rc + delta_r[phi]) * sin(radians(phi)),
            'Ry': -(rb + rc + delta_r[phi]) * cos(radians(phi)),
        })
    return route_list


def harmonic(h: float) -> List[float]:
    delta_r = []
    for phi in range(0, 90):
        delta_r.append(0.)
    for phi in range(0, 90):
        delta_r.append((1 - cos(2 * radians(phi))) * h / 2)
    for phi in range(0, 90):
        delta_r.append(h)
    for phi in range(0, 90):
        delta_r.append(h - (1 - cos(2 * radians(phi))) * h / 2)
    return delta_r


def cycloidal(h: float) -> List[float]:
    delta_r = []
    for phi in range(0, 90):
        delta_r.append(0.)
    for phi in range(0, 90):
        delta_r.append((radians(phi) * 2 - sin(4 * radians(phi)) / 2) / pi * h)
    for phi in range(0, 90):
        delta_r.append(h)
    for phi in range(0, 90):
        delta_r.append(h - (radians(phi) * 2 - sin(4 * radians(phi)) / 2) / pi * h)
    return delta_r
