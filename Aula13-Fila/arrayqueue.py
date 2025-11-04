"""
File: arrayqueue.py
"""

from arrays import Array
from abstractcollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Initalize self._front and self._rear here
        self._front = ArrayQueue.DEFAULT_CAPACITY - 1
        self._rear = ArrayQueue.DEFAULT_CAPACITY - 1
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        return iter(self.items)
    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        return self.items[self._front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        # Initalize self._front and self._rear here
        self._front = ArrayQueue.DEFAULT_CAPACITY - 1
        self._rear = ArrayQueue.DEFAULT_CAPACITY - 1
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if(self.size < ArrayQueue.DEFAULT_CAPACITY):
            self.items[self._rear] = item
            self.size += 1
            self._rear -= 1
            if(self._rear == -1):
                self_rear = ArrayQueue.DEFAULT_CAPACITY - 1
        else:
            raise Exception("Queue is full")
    
    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("Queue is empty")
        item = self.items[self._front]
        self.items[self._front] = None
        self._front -= 1
        self.size -= 1
        if self._front == -1:
            self._front = ArrayQueue.DEFAULT_CAPACITY -1
        return item        
         
