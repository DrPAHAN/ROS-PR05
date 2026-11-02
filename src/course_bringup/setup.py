from setuptools import setup
from glob import glob
import os

package_name = 'course_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ЭТА СТРОКА КОПИРУЕТ LAUNCH-ФАЙЛЫ ПРИ СБОРКЕ:
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='DrPAHAN',
    maintainer_email='p.mironenko@g.nsu.ru',
    description='PR05 course bringup package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pose_relay = course_bringup.pose_relay:main',
        ],
    },
)
