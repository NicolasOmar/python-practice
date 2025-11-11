import hashlib
import json

def hash_string_256(string):
    """ Hash a string using sha256 """
    return hashlib.sha256(string).hexdigest()

def hash_block(block):
    """ Hash a block using its strucutre as base """
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    encoded_block = json.dumps(hashable_block, sort_keys=True).encode()
    
    return hash_string_256(encoded_block)

def add__line():
    print('------------------------------')