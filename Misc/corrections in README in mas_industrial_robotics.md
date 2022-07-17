# 1. 

#### Errors: 

```
Cloning into 'mas_industrial_robotics'...
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

```

While cloning the mas_insudtrial_robotics the command given below wont work: 

```
git clone git@github.com:b-it-bots/mas_industrial_robotics.git
```


#### Solution:  

- so clone the repo directly using this command  
`git clone https://github.com/b-it-bots/mas_industrial_robotics.git`


-----

# 2.

#### Error:

```
ERROR: the following packages/stacks could not have their rosdep keys resolved
to system dependencies:
rosplan_planning_system: No definition of [python-yaml] for OS version [focal]
atwork_commander_com: Cannot locate rosdep definition for [master_sync_fkie]
mcr_leg_detection: Cannot locate rosdep definition for [bfl]
```

#### Solution:

Reference: [Official ROS Noetic Migration webpage](http://wiki.ros.org/action/fullsearch/noetic/Migration?action=fullsearch&context=180&value=linkto%3A%22noetic%2FMigration%22)

- 2.1   
For mcr_leg_detection error -- go to package.xml file in `catkin_ws/src/mas_perception/mcr_leg_detection/package.xml` 

replace the below line: 

```
<build_depend>bfl</build_depend>
``` 

with these lines,  
```
<build_depend>liborocos-bfl-dev</build_depend>
<build_depend>liborocos-bfl</build_depend>
```

- 2.2  
For rosplan_planning_com error -- modify the package.xml file in 
`catkin_ws/src/ROSplan/ros_planning_system/package.xml` 

change the last line from 

```
 <run_depend>python-yaml</run_depend> 
 ```
 
 to 

 ```
  <run_depend>python3-yaml</run_depend> 
```
- 2.3  
For atwork_commander_com error -- go to package.xml file in 
`catkin_ws/src/atwork-commander/atwork_commander_com/package.xml` 

change these lines
```
<exec_depend>master_discovery_fkie</exec_depend>
<exec_depend>master_sync_fkie</exec_depend>
```
to these lines,
```
<exec_depend>fkie_master_discovery</exec_depend>
<exec_depend>fkie_master_sync</exec_depend>
```

-----

# 3.

#### Errors:
```
<< gazebo_version_helpers:cmake /home/tharun/Desktop/temp/catkin_ws_mas_industrial/logs/gazebo_version_helpers/build.cmake.000.log
CMake Error at /usr/share/cmake-3.16/Modules/CMakeFindDependencyMacro.cmake:47 (find_package):
  Could not find a configuration file for package "ignition-common3-graphics"
  that exactly matches requested version "3.14.0".

  The following configuration files were considered but not accepted:

    /usr/lib/x86_64-linux-gnu/cmake/ignition-common3-graphics/ignition-common3-graphics-config.cmake, version: 3.13.1
    /lib/x86_64-linux-gnu/cmake/ignition-common3-graphics/ignition-common3-graphics-config.cmake, version: 3.13.1

Call Stack (most recent call first):
  /usr/lib/x86_64-linux-gnu/cmake/ignition-common3/ignition-common3-config.cmake:203 (find_dependency)
  /usr/lib/x86_64-linux-gnu/cmake/gazebo/gazebo-config.cmake:250 (find_package)
  CMakeLists.txt:15 (find_package)
```

#### Solution: 

Reference: NA

`sudo apt install libignition-common3-dev`

-----

# 4.

#### Errors:
```
<< mcr_background_change_detection:cmake /home/tharun/Desktop/temp/catkin_ws_mas_industrial/logs/mcr_background_change_detection/build.cmake.000.log
CMake Error at /home/tharun/Desktop/temp/catkin_ws_mas_industrial/src/mas_perception/mcr_background_change_detection/CMakeLists.txt:13 (find_package):
  Could not find a configuration file for package "OpenCV" that is compatible
  with requested version "3".

  The following configuration files were considered but not accepted:

    /usr/lib/x86_64-linux-gnu/cmake/opencv4/OpenCVConfig.cmake, version: 4.2.0
    /lib/x86_64-linux-gnu/cmake/opencv4/OpenCVConfig.cmake, version: 4.2.0
```

#### Solution:

Reference: NA

- Change in the files `catkin_ws/src/gazebo-pkgs/gazebo_grasp_plugin/CMakeLists.txt` 
and 
`catkin_ws/src/gazebo-pkgs/gazebo_version_helpers/CMakeLists.txt` 

FROM `DEPENDS gazebo`  TO  `DEPENDS GAZEBO`

-----

# 5.

#### Errors:

```
<< mcr_image_filter:make /home/tharun/Desktop/temp/catkin_ws_mas_industrial/logs/mcr_image_filter/build.make.000.log             
In file included from /home/tharun/Desktop/temp/catkin_ws_mas_industrial/src/mas_perception/mcr_image_filter/ros/src/image_filter_node.cpp:1:
/home/tharun/Desktop/temp/catkin_ws_mas_industrial/src/mas_perception/mcr_image_filter/ros/include/mcr_image_filter/image_filter_node.h:11:10: fatal error: opencv/cv.h: No such file or directory
   11 | #include <opencv/cv.h>
      |          ^~~~~
compilation terminated.
make[2]: * [CMakeFiles/image_filter_node.dir/build.make:63: CMakeFiles/image_filter_node.dir/ros/src/image_filter_node.cpp.o] Error 1
make[1]: * [CMakeFiles/Makefile2:347: CMakeFiles/image_filter_node.dir/all] Error 2
make: * [Makefile:141: all] Error 2
```

#### Solution:

Reference: NA

- Go to this path,
`catkin_ws/src/mas_perception/mcr_image_filter/ros/include/image_filter_node.h`,   
remove : 
`#include <opencv/cv.h>`  
and change: 
`#include <opencv/highgui.h>` to 
`#include <opencv2/highgui.hpp>`

-----

# 6. 

#### Erros: 
to avoid cmake warnings
#### Solution: 
Reference: [Official ROS Noetic Migration webpage](http://wiki.ros.org/action/fullsearch/noetic/Migration?action=fullsearch&context=180&value=linkto%3A%22noetic%2FMigration%22)

- Change all `cmake_minimum_required(VERSION 2.8.3)` to `cmake_minimum_required(VERSION 3.0.2)` in CMakeLists.txt files

- Change all `xacro.py` to `xacro` in launch files 

- Change in all `setup.py` files,
from
`from distutils.core import setup`  
to
`from setuptools import setup`

-----

# 7. 


#### Warnings:

```
Warnings   << gazebo_version_helpers:cmake /home/ravi/catkin_ws/logs/gazebo_version_helpers/build.cmake.000.log
CMake Warning at /opt/ros/noetic/share/catkin/cmake/catkin_package.cmake:166 (message):
  catkin_package() DEPENDS on 'gazebo' but neither 'gazebo_INCLUDE_DIRS' nor
  'gazebo_LIBRARIES' is defined.
Call Stack (most recent call first):
  /opt/ros/noetic/share/catkin/cmake/catkin_package.cmake:102 (_catkin_package)
  CMakeLists.txt:26 (catkin_package)
```

#### Solution:

Reference: [Link](https://programmerah.com/catkin_make-warninggazebo_libraries-is-defined-22471/)

- Change in the files `catkin_ws/src/gazebo-pkgs/gazebo_grasp_plugin/CMakeLists.txt` and `catkin_ws/src/gazebo-pkgs/gazebo_version_helpers/CMakeLists.txt`, from `DEPENDS gazebo` to `DEPENDS GAZEBO`


# 8.

#### Errors:

```
error: #error PCL requires C++14 or above
```

#### Solution:

Reference: [Link](https://github.com/PointCloudLibrary/pcl/issues/2968)

- In files,   
`catkin_ws/src/mas_perception/mcr_pose_estimation/CMakeLists.txt`, `catkin_ws/src/mas_perception/mcr_contour_matching/CMakeLists.txt`, `catkin_ws/src/mas_perception/mcr_object_recognition_bounding_box/CMakeLists.txt` add line `set(CMAKE_CXX_STANDARD 14)` after `project(***)` line

- In files `catkin_ws/src/mas_perception/mas_perception_libs/CMakeLists.txt`, and `catkin_ws/src/mas_industrial_robotics/mir_perception/mir_ppt_detection/CMakeLists.txt`, change C++ version, from `add_compile_options(-std=c++11)` to `add_compile_options(-std=c++14)`. In same file, change `find_package(Boost REQUIRED COMPONENTS python)` to `find_package(Boost REQUIRED COMPONENTS python38)`

# 9. 

#### Erros:

```
fatal error: opencv/cv.h: No such file or directory
```

#### Solution:

- In file `catkin_ws/src/mas_perception/ mas_perception_libs/common/src/bounding_box.cpp`, remove line `#include <opencv/cv.h>`

#### Errors:

```
error: ‘CvMemStorage’ was not declared in this scope
   34 |     CvMemStorage* storage = cvCreateMemStorage(0);
```

```
error: ‘CV_BGR2GRAY’ was not declared in this scope
   20 |     cv::cvtColor(image, gray_image, CV_BGR2GRAY);
```

#### Solution: Not sure about this one

Reference: [Link](https://stackoverflow.com/a/11604986/6920365)

- In files `catkin_ws/src/mas_perception/mas_perception_libs/common/src/bounding_box.h`,  `catkin_ws/src/mas_perception/mcr_contour_matching/common/src/contour_finder.cpp`, `catkin_ws/src/mas_industrial_robotics/mir_perception/mir_cavity_detector/common/src/cavity_finder.cpp`, `catkin_ws/src/mas_perception/mcr_people_tracking/ros/src/waist_tracking_node.cpp`        

  add line `#include <opencv2/imgproc/imgproc_c.h>`


# 10.

#### Errors:

For mercury_planner,
```
fatal error: bits/c++config.h: No such file or directory
   38 | #include <bits/c++config.h>
```

For mir_2dnav,
```
CMake Error at /opt/ros/noetic/share/catkin/cmake/test/tests.cmake:163 (add_custom_target):
  The target name
  "run_tests_mir_2dnav_roslaunch-check_launch__robot_youbot-brsu-1
  robot_env_brsu-c025" is reserved or not valid for certain CMake features,
  such as generator expressions, and may result in undefined behavior.
Call Stack (most recent call first):
  /opt/ros/noetic/share/roslaunch/cmake/roslaunch-extras.cmake:66 (catkin_run_tests_target)
  CMakeLists.txt:12 (roslaunch_add_file_check)


CMake Error at /opt/ros/noetic/share/catkin/cmake/test/tests.cmake:177 (add_custom_target):
  The target name
  "_run_tests_mir_2dnav_roslaunch-check_launch__robot_youbot-brsu-1
  robot_env_brsu-c025" is reserved or not valid for certain CMake features,
  such as generator expressions, and may result in undefined behavior.
Call Stack (most recent call first):
  /opt/ros/noetic/share/roslaunch/cmake/roslaunch-extras.cmake:66 (catkin_run_tests_target)
  CMakeLists.txt:12 (roslaunch_add_file_check)
```

For python_orocos_kdl,
```
CMake Error at /opt/ros/noetic/share/catkin/cmake/empy.cmake:30 (message):
  Unable to find either executable 'empy' or Python module 'em'...  try
  installing the package 'python3-empy'
```

#### Solution:

Reference: [Mercury github repo](https://github.com/b-it-bots/mercury_planner)

- For `mercury_planner`, install dependencies

  `sudo apt-get install bison flex gawk g++-multilib pypy`

- For `mir_2dnav`, comment TEST cases,
```
# TESTS
# if(CATKIN_ENABLE_TESTING)
#   find_package(roslaunch REQUIRED)

#   roslaunch_add_file_check(ros/launch "robot:=youbot-brsu-1 robot_env:=brsu-c025")
# endif()
```

- For `python_orocos_kdl`, pull latest changes from the official git repo

  1. Go to `catkin_ws/src/orocos_kinematics_dynamics/python_orocos_kdl`, then run

      - `git remote add upstream https://github.com/orocos/orocos_kinematics_dynamics.git`

      - `git pull upstream master`

      - go to `pybind11` directory, run `git submodule update --init --recursive`

      - Build the package, if error comes up then do `catkin clean` and build again






# 11.

#### Errors:

```
Errors     << youbot_driver_ros_interface:make /home/kvnptl/catkin_ws/logs/youbot_driver_ros_interface/build.make.000.log     
make[2]: gksudo: Command not found
make[2]: *** [CMakeFiles/youbot_driver_ros_interface.dir/build.make:160: /home/kvnptl/catkin_ws/devel/.private/youbot_driver_ros_interface/lib/youbot_driver_ros_interface/youbot_driver_ros_interface] Error 127
make[2]: *** Deleting file '/home/kvnptl/catkin_ws/devel/.private/youbot_driver_ros_interface/lib/youbot_driver_ros_interface/youbot_driver_ros_interface'
make[1]: *** [CMakeFiles/Makefile2:303: CMakeFiles/youbot_driver_ros_interface.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
```

#### Solution:

In file `catkin_ws/src/youbot_driver_ros_interface/CMakeLists.txt`, change line 44, `set(SUDO_COMMAND gksudo)`, to `set(SUDO_COMMAND pkexec)`

==========================================

OLD Errors  

==========================================

3. If you get this error msg

Error: There already is a workspace config file .rosinstall at "/home/ravi/Desktop/mas_simulation/src". Use wstool install/modify.

This is due to running the setup.sh file more than once..
you can find .rosinstall and a .bak file in the src folder of your workspace in hidden files 
delete them and run the script again and it will work

----

3. if you get an error msg like this :

Copy "" mas industrial robotics "" to src
cp: cannot create regular file '/home/ravi/Desktop/mas_simulation/src/mas_industrial_robotics/.git/objects/pack/pack-fd7f9937c2e75d92214f26e0f03272ce92b9ddf2.pack': Permission denied
cp: cannot create regular file '/home/ravi/Desktop/mas_simulation/src/mas_industrial_robotics/.git/objects/pack/pack-fd7f9937c2e75d92214f26e0f03272ce92b9ddf2.idx': Permission denied

delete the corresponding folder in src and also delete .rosinstall and .bak file from hidden files 
in this case delete "mas industrial robotics" folder in src

-----

4. if you get this error msg:

ERROR: the following packages/stacks could not have their rosdep keys resolved
to system dependencies:
mir_atwork_commander_client: Cannot locate rosdep definition for [atwork_commander_msgs]

Just add plain "CATKIN_IGNORE" file without extention to the mir_atwork_commander_client folder in your cloned "/mas_industrial_robotics/mir_planning/" not in workspace ==> SRC folder

-----

5. if you get error related to lama_planner package then Just add plain "CATKIN_IGNORE" file without extention to src/lama_planner foler

----

6. if you ger this error :

CMake Error at /home/ravi/Desktop/mas_simulation/src/mas_perception/mcr_background_change_detection/CMakeLists.txt:13 (find_package):
  Could not find a configuration file for package "OpenCV" that is compatible
  with requested version "3".


go to <src/mas_perception/mcr_background_change_detection/CMakeLists.txt> file and change the 
line 13 from 
find_package(OpenCV 3 REQUIRED) 
to 
find_package(OpenCV REQUIRED)

-----

7. when you get an error like this :

Errors     << mcr_image_filter:make /home/ravi/Desktop/mas_simulation/logs/mcr_image_filter/build.make.001.log
In file included from /home/ravi/Desktop/mas_simulation/src/mas_perception/mcr_image_filter/ros/src/image_filter_node.cpp:1:
/home/ravi/Desktop/mas_simulation/src/mas_perception/mcr_image_filter/ros/include/mcr_image_filter/image_filter_node.h:11:10: fatal error: opencv/cv.h: No such file or directory
   11 | #include <opencv/cv.h>

do this :

remove line 11 "#include <opencv/cv.h>" from the file below:
/src/mas_perception/mcr_image_filter/ros/include/mcr_image_filter.h

-----

8. if you get an error like this :

In file included from /home/ravi/Desktop/mas_simulation/src/mas_perception/mcr_image_filter/ros/src/image_filter_node.cpp:1:
/home/ravi/Desktop/mas_simulation/src/mas_perception/mcr_image_filter/ros/include/mcr_image_filter/image_filter_node.h:12:10: fatal error: opencv/highgui.h: No such file or directory
   12 | #include <opencv/highgui.h>
      |          ^~~~~~~~~~~~~~~~~~

do this:

change line 12 "#include <opencv/highgui.h>" to "<opencv2/highgui.hpp>" from the file below:
/src/mas_perception/mcr_image_filter/ros/include/mcr_image_filter.h

-----

9. For this error:

CMake Error at /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find Boost (missing: python) (found version "1.71.0")

Do this:

Just add plain "CATKIN_IGNORE" file without extention to the below path
/src/mas_perception/mas_perception_libs/ 

-----

10. error like this:

CMake Error at /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by
  "mas_perception_libs" with any of the following names:

    mas_perception_libsConfig.cmake
    mas_perception_libs-config.cmake

  Add the installation prefix of "mas_perception_libs" to CMAKE_PREFIX_PATH
  or set "mas_perception_libs_DIR" to a directory containing one of the above
  files.  If "mas_perception_libs" provides a separate development package or
  SDK, be sure it has been installed.
Call Stack (most recent call first):
  CMakeLists.txt:4 (find_package)


