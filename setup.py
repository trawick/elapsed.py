#!/usr/bin/env python

# Copyright 2016 Jeff Trawick, http://emptyhammock.com/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from distutils.core import setup

setup(
    author='Jeff Trawick',
    author_email='trawick@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python 2.7',
        'Programming Language :: Python 3',
    ],
    description='Calculate elapsed time from strings in Python',
    install_requires=[],
    license="ASL 2.0",
    name='elapsed',
    packages=['elapsed', ],
    scripts=['elapsed.py', ],
    url='https://github.com/trawick/elapsed.py',
    version='0.1.0',
)
