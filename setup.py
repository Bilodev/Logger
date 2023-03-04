from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'Logging made simple and beautiful'
LONG_DESCRIPTION = 'A package that allows to log in a simple and efficient way.'

# Setting up
setup(
    name="Logger",
    version=VERSION,
    author="Bilodev (Antonio Bilotta)",
    author_email="bilotta.antonio.biz@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['print_color'],
    keywords=['python', 'Log', 'Logging', 'Debug', 'TUI', 'Terminal'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)