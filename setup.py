from setuptools import setup, find_packages

setup(
    name='sample-package',
    version='0.0.1',
    description='Tutorial Package',
    author='sangyeon217',
    author_email='sangyeon217@gmail.com',
    packages=find_packages(include=['sample']),
    install_requires=[
        'selenium>=4'
        'webdriver-manager'
    ]
)