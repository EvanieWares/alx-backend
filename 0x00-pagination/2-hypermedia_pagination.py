#!/usr/bin/env python3
"""
Module 0-simple_helper_function

Demonstrate a function that return a tuple of size two containing a start
index and an end index
"""
from typing import Tuple
import csv
import math
from typing import List, Dict


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List:
        """
        Get a page of dataset.

        Args:
            page (int): The page number, defaults to 1.
            page_size (int): The number of items per page, defaults to 10.

        Returns:
            List: A list of lists representing a page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a hypermedia page of dataset.

        Args:
            page (int): The page number, defaults to 1.
            page_size (int): The number of items per page, defaults to 10.

        Returns:
            Dict: A dictionary containing the hypermedia page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        return {
            'page_size': len(dataset[startIndex:endIndex]),
            'page': page,
            'data': dataset[startIndex:endIndex],
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Parameters:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
