#!/usr/bin/env python

"""
My own implementation of the "find" command.
"""

import os
import sys


def my_find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    result = my_find(sys.argv[-1], dir_path)

    if result is None:
        print("No such file")
    else:
        print(result)
