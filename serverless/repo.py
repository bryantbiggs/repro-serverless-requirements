#!/usr/bin/env python
"""
    Repro
    -----

    This is a module about repro

"""

from sdk.foo import foo


def handler(event, context):
    """Make a request and print it"""
    resp = foo()
    print(resp)


if __name__ == '__main__':
    handler('a', 'b')