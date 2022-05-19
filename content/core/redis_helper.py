from django.core.cache import cache


# This function set value
def setKey(key, value, timeout=None):
    return cache.set(key, value, timeout=timeout)


# This function set value if key exist then give error
def addKey(key, value, timeout=None):
    return cache.add(key, value, timeout=timeout)


# This function get value by key
def getKey(key):
    return cache.get(key)


# This function delete value by key
def deleteKey(key):
    return cache.delete(key)


# This function delete value by pattern
def getAllKey(pattern):
    return cache.keys(pattern)

