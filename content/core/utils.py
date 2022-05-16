import os
import string
import uuid
from binascii import hexlify
import random


def generate_pk(prefix, upper=False, length=15, separator="-"):
    chars = "%s%s%s%s" % (
        string.ascii_uppercase, string.digits, uuid.uuid1().hex, hexlify(os.urandom(16)).decode("utf-8"))
    pk = prefix.lower() + separator + "".join(random.choice(chars) for _ in range(length)).lower()
    if upper:
        pk = pk.upper()
    return pk