from setuptools import find_packages, setup


with open('requirements.txt') as f:
    lines = filter(None, map(str.strip, f))
    install_requires = [req for req in lines if req[0] not in '-#']


setup(
    name='dixit',
    version='0.0.1',
    author="# TODO",
    url='https://gitlab.com/_todo/dixit',
    description="Django implementation of the popular board game Dixit",
    packages=find_packages(),
    install_requires=install_requires,
    scripts=['manage.py'],
)
