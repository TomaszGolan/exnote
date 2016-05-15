from setuptools import setup
import exnote

with open('README.md') as f:
    long_description = f.read()


setup(
    name="exnote",
    version=exnote.__version__,
    author=exnote.__author__,
    author_email=exnote.__email__,
    url="https://github.com/tomaszgolan/exnote",
    description=("Executable Notes"),
    license=exnote.__license__,
    long_description=long_description,
    classifiers=[
        "Development Status :: " + exnote.__status__,
        'Environment :: Console',
        'License :: OSI Approved :: ' + exnote.__license__,
        'Programming Language :: Python'
    ],
    packages=['exnote'],
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'exnote=exnote.exnote:main',
            ],
    },
)
