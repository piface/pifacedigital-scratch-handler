import sys
from distutils.core import setup


# PY3 = sys.version_info.major >= 3  # major is not available in python2.6
PY3 = sys.version_info[0] >= 3
PIFACECOMMON_MIN_VERSION = '3.0.0'
VERSION_FILE = "scratch_handler.py"


def get_version():
    return '2.0.1'


setup(
    name='pifacedigital-scratch-handler',
    version=get_version(),
    description='The PiFace Digital Scratch Handler.',
    author='Thomas Preston',
    author_email='thomas.preston@openlx.org.uk',
    url='https://github.com/piface/pifacedigital-scratch-handler/',
    py_modules=['scratch_handler.py'],
    long_description=open('README.md').read() + open('CHANGELOG').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or ",
        "later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='piface digital scratch raspberrypi openlx',
    license='GPLv3+',
    requires=['pifacecommon (>='+PIFACECOMMON_MIN_VERSION+')']
)
