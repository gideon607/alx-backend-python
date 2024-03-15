#!/usr/bin/env python3
""" Lets duck type for an iterable object"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ The element length """
    return [(i, len(i)) for i in lst]
