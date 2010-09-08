import memcache
import types

from hash_ring import HashRing

class MemcacheRing(memcache.Client):
    """Extends python-memcache so it uses consistent hashing to
    distribute the keys.
    """

    def __init__(self, servers, *k, **kw):
        self.hash_ring = HashRing(servers)

        memcache.Client.__init__(self, servers, *k, **kw)

        self.server_mapping = {}
        for server_uri, server_obj in zip(servers, self.servers):
            self.server_mapping[server_uri] = server_obj

    def _get_server(self, key):
        if type(key) == types.TupleType:
            return memcache.Client._get_server(key)

        for i in range(self._SERVER_RETRIES):
            iterator = self.hash_ring.iterate_nodes(key)
            for server_uri in iterator:
                server_obj = self.server_mapping[server_uri]
                if server_obj.connect():
                    return server_obj, key

        return None, None
