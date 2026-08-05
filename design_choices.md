# Design Choices

## Robot

A SimReady Husky A300 model was used because it already contains wheel joints, rigid bodies and articulation information compatible with Isaac Sim.

## ROS Communication

ROS2 Bridge was used to connect Isaac Sim with ROS2 Humble.

FastDDS (rmw_fastrtps_cpp) was selected because it is the middleware recommended by Isaac Sim.

## Teleoperation

Teleoperation is implemented using:

teleop_twist_keyboard
    ->
/cmd_vel
    ->
ROS2 Subscribe Twist
    ->
Differential Controller
    ->
Articulation Controller

This follows a standard differential drive architecture.

## State Publishing

The following topics are published:

- /clock
- /tf
- /joint_states
- /odom

Odometry is computed using Isaac Compute Odometry.

Transforms are published using ROS2 Transform Tree nodes.

## Visualization

RViz is used to visualize:

- TF frames
- Odometry
- Robot motion

Fixed frame is set to odom.

# Challenges Encountered

1. Imported USD articulation root was not obvious and required inspection of the USD hierarchy.

2. Wheel joints existed but direct DriveAPI velocity commands did not move the robot.

3. Isaac Sim 6.0.1 API differs from older tutorials, causing articulation API mismatches.

4. ROS2 discovery initially failed because ROS environment variables were not sourced.

5. Action Graph nodes for odometry and joint states required manual configuration before topics became visible.

6. RViz visualization required verification of TF frames and fixed frame configuration.