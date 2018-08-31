from setuptools import setup

setup(
  name='ec2-snapshot-analysis',
  version='0.1',
  author='Andrew Mitchell',
  author_email='andrewpmitchell7@gmail.com',
  description='Demo application for python practice in the context of AWS',
  packages=['shotty'],
  license='',
  url='https://github.com/mitch292/ec2-snapshot-analysis',
  install_requires=[
    'click',
    'boto3'
  ],
  entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
  ''',

)