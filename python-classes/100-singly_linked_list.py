#!/usr/bin/python3
"""Module that defines a Node class and a SinglyLinkedList class."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes the list."""
        self.__head = None

    def __str__(self):
        """Defines how to print the list."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position."""
        new_node = Node(value)
        # Case 1: Empty list or new value is smaller than the head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Traverse to find the insertion point
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
