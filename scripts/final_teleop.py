import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import numpy as np
import omni.kit.app

from isaacsim.core.prims import SingleArticulation

"""
This node takes keypresses from the keyboard and publishes them
as Twist/TwistStamped messages. It works best with a US keyboard layout.
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
"""

ART_ROOT = "/tn__a30000000_pD/Geometry/base_link"

try:
    rclpy.init()
except:
    pass

robot = SingleArticulation(prim_path=ART_ROOT)
robot.initialize()

print("DOFs:", robot.dof_names)

FL = robot.get_dof_index("front_left_wheel_joint")
FR = robot.get_dof_index("front_right_wheel_joint")
RL = robot.get_dof_index("rear_left_wheel_joint")
RR = robot.get_dof_index("rear_right_wheel_joint")

print("Wheel indices:", FL, FR, RL, RR)


class CmdVelNode(Node):

    def __init__(self):
        super().__init__("husky_teleop")

        self.create_subscription(
            Twist,
            "/cmd_vel",
            self.callback,
            10
        )

    def callback(self, msg):

        v = msg.linear.x
        w = msg.angular.z

        # Differential drive mixing
        left = (v - w) * 10.0
        right = (v + w) * 10.0

        vel = np.zeros(robot.num_dof)

        vel[FL] = left
        vel[RL] = left

        vel[FR] = right
        vel[RR] = right

        robot.set_joint_velocities(vel)

        print(
            f"v={v:.2f} "
            f"w={w:.2f} "
            f"L={left:.2f} "
            f"R={right:.2f}"
        )


node = CmdVelNode()


def update(_):
    rclpy.spin_once(node, timeout_sec=0)


sub = (
    omni.kit.app.get_app()
    .get_update_event_stream()
    .create_subscription_to_pop(update)
)

print("Listening on /cmd_vel")