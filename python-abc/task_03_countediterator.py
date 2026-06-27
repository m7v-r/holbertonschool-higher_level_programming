#!/usr/bin/env python3
"""Module for CountedIterator class"""


class CountedIterator:
    """Class to iterate over an object and count items"""
    def __init__(self, data):
        self.iterator = iter(data)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count

    def __iter__(self):
        return self
