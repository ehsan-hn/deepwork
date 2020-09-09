from setuptools import setup

setup(
    name='deepwork',
    version='0.1',
    py_modules=['deepwork'],
    install_requires=[
        'Click',
        'tabulate'
    ],
    scripts=['deepwork.py',
             'db.py',
             'model.py']
)