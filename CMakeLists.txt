cmake_minimum_required(VERSION 3.0.2)
project(gazebo_simulation_ros)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  tf
  gazebo_plugins
)
find_package(gazebo REQUIRED)

catkin_package(

)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

link_directories(
  ${Boost_LIBRARY_DIRS}
  ${GAZEBO_LIBRARY_DIRS}
)
