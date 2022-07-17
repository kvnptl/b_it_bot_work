# GIT Tutorial
- git tutorial link not found

# Docker
- After `docker pull ...` command, where to find start-container.yaml file?
    - I found it under `/var/lib/docker/overlay2` with date and time filter
- Docker compose command `docker-compose -f start-container.yaml up <industrial_kinetic|industrial_melodic>`
    - YAML file extension is `start-container.yml` not `start-container.yaml` 
    
# Simulation
- node died
    - Error: `[gazebo-2] process has died [pid 29662, exit code 134, cmd /opt/ros/melodic/lib/gazebo_ros/gzserver -e ode worlds/empty.world __name:=gazebo __log:=/home/robocup/.ros/log/2033a6cc-8f52-11ec-8f85-ac1203307591/gazebo-2.log]`.
    - `Aborted (core dumped)`

    - `[gazebo_gui-3] process has died [pid 29668, exit code 134, cmd /opt/ros/melodic/lib/gazebo_ros/gzclient __name:=gazebo_gui __log:=/home/robocup/.ros/log/2033a6cc-8f52-11ec-8f85-ac1203307591/gazebo_gui-3.log].
log file: /home/robocup/.ros/log/2033a6cc-8f52-11ec-8f85-ac1203307591/gazebo_gui-3*.log`
- rosnode list available