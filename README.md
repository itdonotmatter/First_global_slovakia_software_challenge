# First_global_slovakia_software_challenge
code for competition called first global slovakia 
it is suppose to move some kind of imaginary robot autonomously around 
8x8 grid map :)

1. spraviť F. move f
2. otáčanie l, r
3. zapnúť magnet na R B
4. move B (S. ulička)

    left_motor.position = 0
    right_motor.position = 0
    tank_drive.on((-10), (-10))
    while motorA.position > -270:
        if motorA.position <= -270:
            tank_drive.on(30, 30)
        elif motorB.position <= -270:
            tank_drive.on(30, 30)
