#!/usr/bin/env python
"""
    Foo
    ---

    This is a module about foo

"""

import requests


def foo():
    """Make a request."""
    response = requests.get('https://google.com')
    return response.content


if __name__ == '__main__':
    foo()