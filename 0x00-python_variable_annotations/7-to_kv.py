#!/usr/bin/env python3
""" Complex types for - string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments
    returns them as a tuple.
    """

    return (k, v**2)
