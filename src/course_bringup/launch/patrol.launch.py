from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node

def generate_launch_description():
    namespace_arg = DeclareLaunchArgument('namespace', default_value='robot_a')
    sub_reliability_arg = DeclareLaunchArgument('subscriber_reliability', default_value='reliable')
    record_arg = DeclareLaunchArgument('record', default_value='false')
    bag_dir_arg = DeclareLaunchArgument('bag_dir', default_value='evidence/pr05/bag')

    namespace = LaunchConfiguration('namespace')
    record = LaunchConfiguration('record')
    bag_dir = LaunchConfiguration('bag_dir')

    pose_relay_node = Node(
        package='course_bringup',
        executable='pose_relay',
        namespace=namespace,
        output='screen'
    )

    bag_record = ExecuteProcess(
        cmd=[
            'ros2', 'bag', 'record', '-s', 'mcap', '-o', bag_dir,
            '--topics', PathJoinSubstitution(['/', namespace, 'sensor_pose'])
        ],
        condition=IfCondition(record),
        output='screen'
    )

    return LaunchDescription([
        namespace_arg,
        sub_reliability_arg,
        record_arg,
        bag_dir_arg,
        pose_relay_node,
        bag_record
    ])
