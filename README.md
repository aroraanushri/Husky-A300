# Husky-A300
Bring the Clearpath Husky A300 into NVIDIA Isaac Sim 6.0.1 as a physically correct articulated robot, place it in NVIDIA's official warehouse environment, drive it with differential drive teleoperation. The Husky A300 has no ready made USD asset. Building it correctly from the provided URDF is the core of this project.

# Isaac Sim ROS2 Teleoperation of Husky A300

## Overview

This project integrates a Husky A300 robot in NVIDIA Isaac Sim 6.0.1 with ROS 2 Humble.

Implemented functionality:

- ROS 2 Bridge
- Teleoperation using /cmd_vel
- /clock publishing
- /tf publishing
- /joint_states publishing
- /odom publishing
- RViz visualization
- Warehouse environment simulation

---

## Software Versions

Ubuntu 22.04

ROS 2 Humble

Isaac Sim 6.0.1

RMW Implementation:
rmw_fastrtps_cpp

---

## Setup

### ROS

source /opt/ros/humble/setup.bash

export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

### Isaac Sim

Launch Isaac Sim 6.0.1

Open warehouse environment.

Load Husky A300 USD.

Press Play.

---

## Verify Topics

ros2 topic list

Expected:

/clock
/cmd_vel
/joint_states
/odom
/tf

---

## Teleoperation

ros2 run teleop_twist_keyboard teleop_twist_keyboard

Controls:

i = forward

j = left

l = right

k = stop

, = reverse

---

## RViz

rviz2

Fixed Frame:

odom

Displays:

TF

Odometry

Grid

---

## What Works

- Robot loads in Isaac Sim
- Robot remains stable in warehouse
- ROS2 Bridge communication
- /cmd_vel teleoperation
- /clock publishing
- /tf publishing
- /joint_states publishing
- /odom publishing
- RViz visualization

---

## Known Limitations

- Robot model is visualized through TF and odometry only.
- RobotModel display in RViz requires a robot_description publisher which is not currently provided by Isaac Sim.
