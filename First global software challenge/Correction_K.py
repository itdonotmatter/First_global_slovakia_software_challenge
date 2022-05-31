def Correction():
    global Rychlost, Speed, Angle, Uhol
    left_motor.position = 0
    right_motor.position = 0
    tank_drive.on((-10), (-10))
    while motorA.position > -270:
        if motorA.position <= -270:
            tank_drive.on(30, 30)
        elif motorB.position <= -270:
            tank_drive.on(30, 30)
