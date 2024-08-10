# Import necessary libraries
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node


def generate_launch_description():
    share_dir = get_package_share_directory('lio_sam')
    
    #should paramsLivoxIMU.yaml be changed to params.yaml? Usually for ROS2 param.yaml is the default but the ROS1 launch file had paramsLivoxIMU.
    parameter_file = LaunchConfiguration('params_file', default=os.path.join(share_dir, 'config', 'paramsLivoxIMU.yaml'))
    
    loam_launch = IncludeLaunchDescription(
      launch_launch_file=os.path.join(share_dir, 'launch/include', 'module_loam.launch.py'),
      launch_arguments={'params_file': parameter_file}  # Pass parameters if needed
  )

    robot_state_launch = IncludeLaunchDescription(
      launch_launch_file=os.path.join(share_dir, 'launch/include', 'module_robot_state_publisher.launch.py'),
      launch_arguments={'params_file': parameter_file}  # Pass parameters if needed
  )

    rviz_launch = IncludeLaunchDescription(
      launch_launch_file=os.path.join(share_dir, 'launch/include', 'module_rviz.launch.py'),
  )
    
    navsat_launch = IncludeLaunchDescription(
       launch_launch_file=os.path.join(share_dir, 'launch/include', 'module_navsat.launch.py'),
  )
    
    return LaunchDescription([
 
      loam_launch,
      robot_state_launch,
      rviz_launch,
      navsat_launch 
  
  ])