
import time
import sys
import subprocess

def is_pkg_ist(pn):
    try:
        __import__(pn)
        return True
    except ImportError:
        return False

def uid():
    return str(time.time() * 1000)

def remove_right_side(input_string, key):
    return input_string.split(key)[0]
