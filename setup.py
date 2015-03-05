from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Spintune',
    version=get_version('mopidy_spintune/__init__.py'),
    url='https://github.com/jamestowers/mopidy-musicbox-webclient',
    license='GNU General Public License v3 (GPLv3)',
    author='James Towers',
    author_email='james@songdrop.com',
    description='Mopidy Spintune web extension',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.19',
    ],
    entry_points={
        'mopidy.ext': [
            'spintune = mopidy_spintune:MusicBoxExtension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
