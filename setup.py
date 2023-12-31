from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'stopwatch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ryotaro Karikomi',
    maintainer_email='ryotaro.karikomi@gmail.com',
    description='a package for homework 2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	    'talker = stopwatch.talker:main',
	    'listener = stopwatch.listener:main',
        ],
    },
)
