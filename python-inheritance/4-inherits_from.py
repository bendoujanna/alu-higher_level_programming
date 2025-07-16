#!/usr/bin/python3
"""True if the obj is inst of subclass of a_class, else false"""


def inherits_from(obj, a_class):
    """True if obj is instance of subclass of a_class, else False."""
    return isinstance(obj, a_class) and type(obj) is not a_class
