#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import os

from setuptools import setup

def list_files(path):
    for fn in os.listdir(path):
        if fn.startswith('.'):
            continue
        fn = os.path.join(path, fn)
        if os.path.isfile(fn):
            yield fn

setup(name='hash_ring',
      version = '1.3.1',
      author="Amir Salihefendic",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['hash_ring'],
      platforms=["Any"],
      license="BSD",
      keywords='memcached hashing hash consistent',
      description="Implements consistent hashing in Python (using md5 as hashing function).",
      long_description="""\
About hash_ring
---------------

Implements consistent hashing that can be used when
the number of server nodes can increase or decrease (like in memcached).
The hashing ring is built using the same algorithm as libketama.

Consistent hashing is a scheme that provides a hash table functionality
in a way that the adding or removing of one slot
does not significantly change the mapping of keys to slots.

More about hash_ring can be read in a blog post (that explains the idea in greater details):

* Consistent hashing implemented simply in python <http://amix.dk/blog/viewEntry/19367>

More information about consistent hashing can be read in these articles:

* Web Caching with Consistent Hashing <http://www8.org/w8-papers/2a-webserver/caching/paper2.html>
* Consistent hashing and random trees <http://citeseerx.ist.psu.edu/legacymapper?did=38148>

There is also a wrapper MemcacheRing that extends python-memcache to use consistent hashing
for key distribution.


Example
-------

Basic example of usage (for managing memcached instances)::

    memcache_servers = ['192.168.0.246:11212',
                        '192.168.0.247:11212',
                        '192.168.0.249:11212']

    ring = HashRing(memcache_servers)
    server = ring.get_node('my_key')

Example using weights::

    memcache_servers = ['192.168.0.246:11212',
                        '192.168.0.247:11212',
                        '192.168.0.249:11212']
    weights = {
        '192.168.0.246:11212': 1,
        '192.168.0.247:11212': 2,
        '192.168.0.249:11212': 1
    }

    ring = HashRing(memcache_servers, weights)
    server = ring.get_node('my_key')

How to use MemcacheRing::

    from hash_ring import MemcacheRing
    mc = MemcacheRing(['127.0.0.1:11212'])
    mc.set('hello', 'world')
    print mc.get('hello')

The code should be clean and simple. Feel free to concat the author if you detect bugs.
""")
