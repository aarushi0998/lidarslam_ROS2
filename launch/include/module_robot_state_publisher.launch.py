import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node, CommandLaunchArgument
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
     project_name = LaunchConfiguration('project', default='lio_sam')
     share_dir = get_package_share_directory('lio_sam')
     xacro_path = os.path.join(share_dir, 'config', 'robot.urdf.xacro')
     
