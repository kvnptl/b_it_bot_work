1. In creating Catkin workspace 
while cloning from repo dont clone (youbot_drivers, youbot_description, youbot_driver_ros_interface) from "youbot/", clone it from "mas-group/"

-----

2. In KUKA youbot drivers
while searching for ethernet device id you wont find "eth0"(it is older version) you will find something like Eg:("enp5s0", "eno1") 

-----

3. In KUKA youbot drivers
While builiding out hello_world_demo and youbot_application package you cant do the "make" command - it wont work because that needs some dependencies (error will popup from Cmake file)

-----

4. While building all the packages 
you find some packages are missing like 
(brics_actuators) for this repo clone it from <https://github.com/wnowak/brics_actuator> into src directory
(pr2 msgs) for this repo <sudo apt install ros-noetic-pr2-msgs>

-----

5. while running the launch file <roslaunch youBot youBot_driver.launch> you will get an error similar to this (not exactly): 

<RLException: Invalid <param> tag: Cannot load command parameter [robot_description]: no such command [['/opt/ros/noetic/share/xacro/xacro.py']]. 
Param xml is <param name="robot_description" command="$(find xacro)/xacro.py "/>
The traceback for the exception was written to the log file>

to solve this error remove .py extention from '/opt/ros/noetic/share/xacro/xacro.py' (you can find it in line number 50)
in <youbot_driver_ros_interface/launch/youbot_driver.launch>
after changing:
it should look like "<param name="robot_description" command="$(find xacro)/xacro '$(find youbot_description)/robots/youbot.urdf.xacro'"/>"

-----

6. While doing "Create youBot driver node"

The content you supposed to copy inside youBot_driver.launch file will have <!launch> you have to remove "!" from the line <!launch>
or you will get an error like this :

RLException: Invalid roslaunch XML syntax: not well-formed (invalid token): line 2, column 8
The traceback for the exception was written to the log file

-----

7. Check your <youbot_driver_ros_interface/launch/youbot_driver.launch>

<node pkg="robot_state_publisher" type="state_publisher" name="robot_state_publisher" output="screen"/> (line no 53)
change the "state_publisher" to "robot_state_publisher" 
and the correct line should look like this :
<node pkg="robot_state_publisher" type="robot_state_publisher" name="robot_state_publisher" output="screen"/>

-----

8. After connecting the pc to robot :

you will get error like this 

[ERROR] [1643995390.353038734]: No EtherCAT connection:
[FATAL] [1643995390.353085121]: No socket connection on eth0
Excecute as root

  
