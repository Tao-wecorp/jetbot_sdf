# Jetbot SDF model in Gazebo
Jetbot SDF model in Gazebo

## To-do
1. Launch Jetbot SDF in ROS;
2. Launch worlds in ROS;
3. Add camera to Jetbot SDF;
4. Control Jetbot in Gazebo;
5. Add RL algorithms.

## Env
1. Run ./env.sh

## Run
    source devel/setup.bash
    roslaunch jetbot_sdf main.launch
    rosrun gazebo_ros spawn_model -h
    rosrun gazebo_ros spawn_model -sdf -database jetbot -model jetbot -y 1 -Y 180
    rosservice call /gazebo/get_model_state '{model_name: jetbot}'
    rosservice call /gazebo/delete_model '{model_name: jetbot}'
    rosservice call /gazebo/set_model_state '{model_state: { model_name: jetbot, pose: { position: { x: 0, y: 0 ,z: 0 }, orientation: {x: 0, y: 0, z: 0, w: 0 } }, twist: { linear: {x: 0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 90.0 } } , reference_frame: world } }'
    rostopic pub -r 20 /gazebo/set_model_state gazebo_msgs/ModelState '{model_name: jetbot, pose: { position: { x: 0, y: 0, z: 0 }, orientation: {x: 0, y: 0, z: 0, w: 0 } }, twist: { linear: { x: 0, y: 0, z: 0 }, angular: { x: 0, y: 0, z: 0} }, reference_frame: world }'

## Depth camera
    <plugin name="camera_plugin" filename="libgazebo_ros_openni_kinect.so">
        <baseline>0.2</baseline>
        <alwaysOn>true</alwaysOn>
        <!-- Keep this zero, update_rate in the parent <sensor> tag
        will control the frame rate. -->
        <updateRate>0.0</updateRate>
        <cameraName>camera_ir</cameraName>
        <imageTopicName>/camera/color/image_raw</imageTopicName>
        <cameraInfoTopicName>/camera/color/camera_info</cameraInfoTopicName>
        <depthImageTopicName>/camera/depth/image_raw</depthImageTopicName>
        <depthImageCameraInfoTopicName>/camera/depth/camera_info</depthImageCameraInfoTopicName>
        <pointCloudTopicName>/camera/depth/points</pointCloudTopicName>
        <frameName>camera_link</frameName>
        <pointCloudCutoff>0.5</pointCloudCutoff>
        <pointCloudCutoffMax>3.0</pointCloudCutoffMax>
        <distortionK1>0</distortionK1>
        <distortionK2>0</distortionK2>
        <distortionK3>0</distortionK3>
        <distortionT1>0</distortionT1>
        <distortionT2>0</distortionT2>
        <CxPrime>0</CxPrime>
        <Cx>0</Cx>
        <Cy>0</Cy>
        <focalLength>0</focalLength>
        <hackBaseline>0</hackBaseline>
    </plugin>