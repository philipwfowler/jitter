from setuptools import setup

setup(
    install_requires=[
        "numpy >= 1.13"
    ],
    name='jitter',
    scripts=['bin/jitter.py'],
    version='0.1.0',
    url='https://github.com/philipwfowler/jitter',
    author='Philip W Fowler',
    packages=['jitter'],
    license='MIT',
    long_description=open('README.md').read(),
)
