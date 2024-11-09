cmake_minimum_required(VERSION 3.0.2)
project(ros_session)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(move_turtle_node src/move_turtle.cpp)
target_link_libraries(move_turtle_node ${catkin_LIBRARIES})
