from math import cos, sin, pi

def profile(Rb, deltaR):
    profile_list = []
    for phi in range(0, 360):
        theta = phi*pi/180
        Rx = (Rb+deltaR[phi])*sin(theta)
        Ry = (Rb+deltaR[phi])*cos(theta)
        profile_list += [{'Rx':Rx, 'Ry':-Ry}]
    #print(profile_list)
    return profile_list

def cutterRuote(Rb, deltaR, Rc):
    route_list = []
    for phi in range(0, 360):
        theta = phi*pi/180
        Rx = (Rb+Rc+deltaR[phi])*sin(theta)
        Ry = (Rb+Rc+deltaR[phi])*cos(theta)
        route_list += [{'Rx':Rx, 'Ry':-Ry}]
    return route_list

def harmonic(H):
    deltaR = []
    for phi in range(0, 90):
        deltaR += [0]
    for phi in range(0, 90):
        theta = phi*pi/180
        y = (1-cos(2*theta))*H/2
        deltaR += [y]
    for phi in range(0, 90):
        deltaR += [H]
    for phi in range(0, 90):
        theta = phi*pi/180
        y = H-(1-cos(2*theta))*H/2
        deltaR += [y]
    return deltaR

def cycloidal(H):
    deltaR = []
    for phi in range(0, 90):
        deltaR += [0]
    for phi in range(0, 90):
        theta = phi*pi/180
        y = theta*2/pi-sin(4*theta)*H/2/pi
        deltaR += [y]
    for phi in range(0,90):
        deltaR += [H]
    for phi in range(0, 90):
        theta = phi*pi/180
        y = 1-(theta*2/pi-sin(4*theta)*H/2/pi)
        deltaR += [y]
    return deltaR
