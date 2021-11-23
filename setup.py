from setuptools import setup

setup(
    name="os",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click>=8.0.3',
        'progress',
        'inquirer',
    ],
    entry_points='''
        [console_scripts]
        os=cli:main
    ''',
)