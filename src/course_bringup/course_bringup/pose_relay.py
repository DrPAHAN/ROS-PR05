import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from turtlesim_msgs.msg import Pose  # Для Lyrical


class PoseRelayNode(Node):
    def __init__(self):
        super().__init__('pose_relay')
        
        # Подписка на глобальный топик черепахи (вне namespace)
        self.sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )
        
        # Публикация с BEST_EFFORT (относительное имя 'sensor_pose' 
        # автоматически получит префикс namespace, например /robot_a/sensor_pose)
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            depth=10
        )
        self.pub = self.create_publisher(
            Pose,
            'sensor_pose',
            qos_profile
        )
        self.get_logger().info('Нода pose_relay запущена. Публикация с BEST_EFFORT.')

    def pose_callback(self, msg: Pose):
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PoseRelayNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
