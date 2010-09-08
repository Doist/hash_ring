from hash_ring import HashRing

try:
    from memcache_ring import MemcacheRing
except ImportError, e:
    pass
