#!/usr/bin/env python3
""" Complex types for - functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float as a multiplier as argument,
    returns a function that multiplies a float by the multiplier.
    """
    def f(n: float) -> float:
        """ multiplies a float by the multiplier """
        return float(n * multiplier)

    return f
