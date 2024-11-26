from setuptools import setup, find_packages

setup(
    name="passurls",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'passurls = passurls:main', 
        ],
    },
    python_requires='>=3.6',
)
