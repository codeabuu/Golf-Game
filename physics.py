import math

def ballpath(startx, starty, power, ang, time):
    '''
    calculates the new position of a ball in 2D space after a given time,
    given its initial position, launch power (velocity), launch angle, and the time elapsed
    '''
    angle = ang
    velx = math.cos(angle) * power
    vely = math.sin(angle) * power

    distX = velx * time
    distY = (velx * time) + ((-9.8 * (time ** 2)) / 2)

    newx = round(distX + startx)
    newy = round(starty - distY)

    return (newx, newy)

def findPower(power, angle, time):
    '''
    calculates the final speed of the ball after a given time, given its initial speed and angle
    '''
    velx = math.cos(angle) * power
    vely = math.sin(angle) * power

    vfy = vely + (-9.8 * time)
    vf = math.sqrt((vfy**2) + (velx**2))

    return vf

def findAngle(power, angle):
    '''
    recalculates the angle of the velocity vector.
    '''
    velx = math.cos(angle) * power
    vely = math.sin(angle) * power

    ang = math.atan(abs(vely) / abs(velx))

    return ang

def maxTime(power, angle):
    '''
    calculates the maximum time of flight for the projectile to reach its highest point 
    '''
    vely = math.sin(angle) * power
    time = ((power * -1) - (math.sqrt(power**2))) / -9.8

    return time / 2