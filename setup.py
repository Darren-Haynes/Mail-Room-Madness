"""."""

from setuptools import setup

setup(

    name='mailroom',
    description='Mailroom Madness',
    package_dir={'': 'src'},
    author='Robert Bronson and Darren Haynes',
    author_email='robert.j.bronson@gmail.com',
    py_modules=['mailroom'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': [
            "mailroom = mailroom:mailroom_main"
        ]
    }

)
