import hashlib
import json

def hash_string_256(string):
    """ Hash a string using sha256 """
    return hashlib.sha256(string).hexdigest()

def hash_block(block):
    """ Hash a block using its strucutre as base """
    encoded_block = json.dumps(block, sort_keys=True).encode()
    
    return hash_string_256(encoded_block)