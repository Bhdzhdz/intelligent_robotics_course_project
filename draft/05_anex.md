# Move module

```python2
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def set_speed(linear, angular, duration):

    """
    Set the speed of the robot.
    linear: float
        Linear speed in m/s.
    angular: float
        Angular speed in rad/s.
    duration: float
        Duration of the movement in seconds.
    """

    assert(-0.5 <= linear <= 0.5)
    assert(-4.25 <= angular <= 4.25)


    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    rospy.init_node('move', anonymous=True)
    
    move_cmd = Twist()
    move_cmd.linear.x = linear
    move_cmd.angular.z = angular

    now = rospy.Time.now()
    rate = rospy.Rate(10)

    while rospy.Time.now() < now + rospy.Duration.from_sec(duration):
        pub.publish(move_cmd)
        rate.sleep()

def linear_move(meters):
    """
    Move the robot forward for a certain distance.
    meters: float
        Distance in meters.
    """
    linear_speed = 0.2
    if meters < 0:
        linear_speed = -linear_speed
    ANGULAR_SPEED = 0.0
    duration = abs(meters / linear_speed)

    set_speed(linear_speed, ANGULAR_SPEED, duration)


def main():
    try:
        linear_move(1.0)
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()

```