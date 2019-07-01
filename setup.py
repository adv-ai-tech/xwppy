from setuptools import setup, find_packages

setup(
    name='xwppy',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A wordpress python to CLI conversion library',
    long_description=open('README.md').read(),
    install_requires=['os'],
    url='https://github.com/adv-ai-tech/xwppy',
    author='Advait Lab',
    author_email='contact@advaitlabs.com'
)
