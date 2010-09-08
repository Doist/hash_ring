import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hash_ring import HashRing

text = open('tests/palindromes.txt').read()
text = text.replace('\n', '').replace('a ', '').replace('an ', '')
palindromes = [t.strip() for t in text.split(',')]

#--- Helper functions ----------------------------------------------
def create_sets(servers):
    server_sets = {}
    for s in servers:
        server_sets[s] = set()

    ring = HashRing(servers)
    for word in palindromes:
        node = ring.get_node(word)
        server_sets[node].add(word)

    return server_sets

def print_distributions(name, server_sets):
    print '\nDistribution of %s::' % name
    for s in server_sets:
        print '%s: %s' % (s, len(server_sets[s]))

def print_set_info(servers_init, servers_new):
    for init_server in servers_init:
        init_set = servers_init[init_server]
        new_set = servers_new[init_server]

        print ''
        print '%s: %s in init_set' %\
                (init_server, len(init_set))
        print '%s: %s in new_set' %\
                (init_server, len(new_set))
        print '%s: %s in both init_set and new_set' %\
                (init_server, len(init_set.intersection(new_set)))

#--- Testing ----------------------------------------------
init_servers = ['192.168.0.246:11212',
                '192.168.0.247:11212',
                '192.168.0.248:11212']
server_sets_3 = create_sets(init_servers)

print_distributions('server_sets_3', server_sets_3)

extra_servers = ['192.168.0.246:11212',
                 '192.168.0.247:11212',
                 '192.168.0.248:11212',
                 '192.168.0.249:11212',
                 '192.168.0.250:11212']
server_sets_5 = create_sets(extra_servers)

print_distributions('server_sets_5', server_sets_5)

print_set_info(server_sets_3, server_sets_5)
