import os
import sys
import random
import string
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hash_ring import HashRing

memcache_servers = ['192.168.0.246:11212',
                    '192.168.0.247:11212',
                    '192.168.0.249:11212']
weights = {
    '192.168.0.246:11212': 1,
    '192.168.0.247:11212': 2,
    '192.168.0.249:11212': 1
}

ring = HashRing(memcache_servers, weights)
iterations = 100000

def genCode(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])

def random_distribution():
    counts = {}
    for s in memcache_servers:
        counts[s] = 0

    for i in range(0, iterations):
        word = genCode(10)
        counts[ring.get_node(word)] += 1

    for k in counts:
        print('%s: %s' % (k, counts[k]))

    print(sum(counts.values()))

random_distribution()
