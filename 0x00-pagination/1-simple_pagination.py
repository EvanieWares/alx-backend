#!/usr/bin/env python3
"""
Module 0-simple_helper_function

Demonstrate a function that return a tuple of size two containing a start
index and an end index
"""
from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass


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
