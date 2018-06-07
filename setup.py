from setuptools import setup

setup(
    name='optimine2dat',
    version='0.1',
    packages=['optimine2dat'],
    package_data={
        'optimine2dat': ['*.ui']
    },
    url='https://bitbucket.org/zberkowitz/pv_cert',
    license='BSD',
    author='Zac Berkowitz',
    author_email='zberkowitz@whoi.edu',
    description='',
    entry_points={
        'gui_scripts': [
            'Optimine2Dat = optimine2dat.export:main'
        ]
    },
    install_requires=[
        'PyQt5 >= 5.10',
        'PyQtChart >= 5.10',
        'pandas'
    ]
)
