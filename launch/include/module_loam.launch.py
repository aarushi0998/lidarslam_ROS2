import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    project_name = LaunchConfiguration('project', default='lio_sam')
    
	
    imu_preintegration_node = Node(
      package=project_name,
      executable='lio_sam_imuPreintegration',
      name='imu_preintegration',
      output='screen',
      respawn=True
  )

    image_projection_node = Node(
      package=project_name,
      executable='lio_sam_imageProjection',
      name='image_projection',
      output='screen',
      respawn=True
  )

    feature_extraction_node = Node(
      package=project_name,
      executable='lio_sam_featureExtraction',
      name='feature_extraction',
      output='screen',
      respawn=True
  )

    map_optimization_node = Node(
      package=project_name,
      executable='lio_sam_mapOptmization',
      name='map_optimization',
      output='screen',
      respawn=True
  )
    
    return LaunchDescription([
      DeclareLaunchArgument(project_name),
      imu_preintegration_node,
      image_projection_node,
      feature_extraction_node,
      map_optimization_node
  ])