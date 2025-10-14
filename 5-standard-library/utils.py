# Hashing functions are provided by the hashlib module
import hashlib
# The json module allows us to convert python objects into json strings (including structures such as lists and dictionaries)
import json

def hash_string_256(string):
    """ Hash a string using sha256 """
    return hashlib.sha256(string).hexdigest()

def hash_block(block):
    """ Hash a block using its strucutre as base """
    # On this case, first we are going to convert the block into a json string
    # Then we are going to encode it to bytes with the enconde function
    encoded_block = json.dumps(block, sort_keys=True).encode()
    # And at last, we are going to return the hashed block using sha256
    # but converted into a hexadecimal string (for easier reading)
    return hash_string_256(encoded_block)