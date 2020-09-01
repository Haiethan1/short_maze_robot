from robot_control_class import RobotControl

rc = RobotControl()

def move_until_wall():
    rc.stop_robot()

    while(1):
        dis = rc.get_laser(360)
        if(dis < 1):
            rc.stop_robot()
            break
        else:
            rc.move_straight()

def change_direction():
    rc.stop_robot()
    rnge = rc.get_laser_full()

    if(rnge[0] > rnge [719]):
        rc.rotate(270)
    else:
        rc.rotate(90)

while(1):
    move_until_wall()
    change_direction()

