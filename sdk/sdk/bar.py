#!/usr/bin/env python
"""
    Bar
    ---

    This is a module about bar

"""

import requests


def bar():
    """Make a request."""
    response = requests.get('https://google.com')
    return response.content


if __name__ == '__main__':
    bar()