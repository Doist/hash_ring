hash_ring
===========================================

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


Installing
===========

To install hash_ring simply do::
    
    $ sudo easy_install hash_ring


Example
===========

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

The code should be clean and simple. Feel free to contact the author if you detect bugs.

Compatibility
=============

This version of python hash_ring is compatible with:

 * nodejs hash_ring (https://github.com/cypreess/node-hash-ring)
