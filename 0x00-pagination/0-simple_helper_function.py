#!/usr/bin/env python3
"""
Module 0-simple_helper_function

Demonstrate a function that return a tuple of size two containing a start
index and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Parameters:
    - page (int): Page number
    - page_size (int): Number of items per page

    Returns:
    - tuple: Start index and end index
    """
    start_index = (page - 1) * page_size if page > 1 else 0
    end_index = page * page_size
    return (start_index, end_index,)
