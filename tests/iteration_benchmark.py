import os, sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hash_ring import HashRing

init_servers = ['192.168.0.246:11212',
                '192.168.0.247:11212',
                '192.168.0.249:11212',
                '192.168.0.250:11212',
                '192.168.0.251:11212',
                '192.168.0.252:11212',
                '192.168.0.253:11212',
                '192.168.0.255:11212',
                '192.168.0.256:11212',
                '192.168.0.257:11212',
                '192.168.0.258:11212',
                '192.168.0.259:11212']

ring = HashRing(init_servers)
t_start = time.time()
for n in ring.iterate_nodes('test'):
    print(n)
print('Time elapsed %s' % (time.time() - t_start))
