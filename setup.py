#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import os
import re

from setuptools import setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

def get_version():
    """
    get_version reads the version info from bin/vpc-free:__version__
    """

    init = open(os.path.join(ROOT, 'bin', 'zabbix-template-converter')).read()
    return VERSION_RE.search(init).group(1)

setup(name='zabbix-template-converter',
      version=get_version(),
      description='Convert Zabbix templates to older versions.',
      long_description=open('README.rst').read(),
      url='http://github.com/cavaliercoder/zabbix-template-converter',
      author='Ryan Armstrong',
      author_email='ryan@cavaliercoder.com',
      license='GNU Public License v3.0',
      scripts=['bin/zabbix-template-converter'])
