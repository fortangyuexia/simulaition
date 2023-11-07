import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue



def generate_launch_description():
    
    package_name = 'gongnengbao'
    
   

    ld = LaunchDescription()
    pkg_share = FindPackageShare(package=package_name).find(package_name) 
    
    gazebo_world_path = os.path.join(pkg_share, 'world/ditu.world')

    
    # Start Gazebo server
    start_gazebo_cmd =  ExecuteProcess(
        cmd=['gazebo', '--verbose','-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so',gazebo_world_path],
        output='screen')
        
    ld.add_action(start_gazebo_cmd)

    return ld
