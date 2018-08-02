# User Class.py

import json
import os

class User:
    # class var
    count = 0

    # init Method
    def __init__(self, userKey):
        self.userKey = userKey
        self.flag  =  1
