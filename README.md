To modify these instructions to move the turtle in a rectangle, you need to replace the `move_straight.py` script with the `move_turtle_rectangle.py` script. Below is the updated guide:

---

# About

This ROS package controls the movement of a bot inside the `turtlesim` package in a rectangular path.

# Installation

- Install the `turtlesim` package

  ```bash
  sudo apt-get install ros-noetic-turtlesim
  ```

- Compile the code and source the workspace

  ```bash
  catkin_make
  source devel/setup.bash
  ```

# Instructions to run the code

- In terminal 1

  ```bash
  roscore
  ```

- In terminal 2

  ```bash
  rosrun turtlesim turtlesim_node
  ```

- In terminal 3

  ```bash
  rosrun ros_session move_turtle_rectangle.py
  ```

---

This guide assumes the script to move the turtle in a rectangle is named `move_turtle_rectangle.py`. Make sure that this script exists in the `ros_session` package and contains the appropriate code to make the turtle move in a rectangle.
