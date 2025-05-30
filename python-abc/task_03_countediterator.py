#!/usr/bin/python3
class CountedIterator:
    """
    An iterator wrapper that counts how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initialize with any iterable and set the iteration counter to 0.
        """
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0  # Initialize the count of iterated items

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Raises:
        StopIteration: If there are no more items to return.
        """
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1  # Increment count for each successfully fetched item
        return item

    def get_count(self):
        """
        Return the number of items returned so far by this iterator.

        Returns:
        int: The number of times __next__ has successfully returned an item.
        """
        return self.count

    def __iter__(self):
        """
        Return self as an iterator object.
        Required to be used in loops like 'for item in ...'
        """
        return self
