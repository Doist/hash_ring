import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hash_ring import HashRing


#--- Global ----------------------------------------------
memcache_servers = ['192.168.0.246:11212',
                    '192.168.0.247:11212',
                    '192.168.0.249:11212',
                    '192.168.0.250:11212',
                    '192.168.0.251:11212',
                    '192.168.0.252:11212',]

ring = HashRing(memcache_servers)

text = open('tests/palindromes.txt').read()
text = text.replace('\n', '').replace('a ', '').replace('an ', '')
palindromes = text.split(',')


#--- Tests ----------------------------------------------
def test_palindromes():
    assert len(palindromes) > 0

def test_get_node():
    server = ring.get_node('amir')
    assert server in memcache_servers
    assert ring.get_node('amir') == ring.get_node('amir')


def test_distribution():
    counts = {}
    for s in memcache_servers:
        counts[s] = 0

    def count_word(w):
        counts[ring.get_node(w)] += 1

    for palindrome in palindromes:
        count_word(palindrome)

    for s in memcache_servers:
        assert counts[s] > 0

def test_iterate_nodes():
    simple_list = ['1', '2', '3', '4', '5']
    new_ring = HashRing(simple_list)

    nodes = []
    for node in new_ring.iterate_nodes('a'):
        nodes.append(node)

    assert len(nodes) == len(simple_list)
    for elm in simple_list:
        assert elm in nodes


class Server(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

def test_with_objects():
    simple_list = [Server(1), Server(2), Server(3)]

    new_ring = HashRing(simple_list)

    node = new_ring.get_node('BABU')
    assert node in simple_list

    nodes = []
    for node in new_ring.iterate_nodes('aloha'):
        nodes.append(node)

    assert len(nodes) == len(simple_list)
    for elm in simple_list:
        assert elm in nodes
