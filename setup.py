import os
from setuptools import setup, find_packages


INSTALL_REQUIRES = [
    "Click>=7.0",
    "PyYAML"
]

about = {}
with open(os.path.join(os.path.dirname(__file__), 'cli_app', '__about__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name='cli_app',
    version=about['__version__'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'cli-app = cli_app.__main__:main']
    }
)
