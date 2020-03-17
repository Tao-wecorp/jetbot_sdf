# Jetbot SDF model in Gazebo
Jetbot SDF model in Gazebo

## To-do
1. Launch Jetbot SDF in ROS;
2. Launch worlds in ROS;
3. Control Jetbot in Gazebo;
4. Add training algorithms.

## Env
1. Run ./env.sh

## Run
    source devel/setup.bash
    roslaunch jetbot_sdf main.launch
    rosrun gazebo_ros spawn_model -h
    rosrun gazebo_ros spawn_model -sdf -database jetbot -model jetbot -y 1 -Y 180
    rosservice call /gazebo/get_model_state '{model_name: jetbot}'
    rosservice call /gazebo/delete_model '{model_name: jetbot}'
    rosservice call /gazebo/set_model_state '{model_state: { model_name: rrbot, pose: { position: { x: 1, y: 1 ,z: 10 }, orientation: {x: 0, y: 0.491983115673, z: 0, w: 0.870604813099 } }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: world } }'
    rostopic pub -r 20 /gazebo/set_model_state gazebo_msgs/ModelState '{model_name: jetbot, pose: { position: { x: 1, y: 0, z: 0 }, orientation: {x: 0, y: 0, z: 0, w: 90 } }, twist: { linear: { x: 0, y: 0, z: 0 }, angular: { x: 0, y: 0, z: 0}  }, reference_frame: world }'
