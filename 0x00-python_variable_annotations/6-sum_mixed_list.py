#!/usr/bin/env python3

""" Mixed List """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  Returns the sum as a float. """
    return float(sum(mxd_lst))
