#!/usr/bin/python3
"""This module defines classes for a singly-linked list."""


class Node:
    """This class represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node with data and the next node.

        Args:
            data (int): The data stored in the new Node.
            next_node (Node): The next node in the list after this one.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets or sets the data stored in the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("Data must be an integer.")
        self.__data = value

    @property
    def next_node(self):
        """Gets or sets the next node in the list after this one."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("Next node must be a Node object.")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly-linked list."""

    def __str__(self):
        """Defines the string representation of a SinglyLinkedList."""
        nodes = []
        ptr = self.__head

        while ptr is not None:
            nodes.append(str(ptr.data))
            ptr = ptr.next_node

        return "\n".join(nodes)

    def __init__(self):
        """Initializes a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the list in sorted order."""
        newNode = Node(value)

        if self.__head is None or self.__head.data >= newNode.data:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            ptr = self.__head
            while (ptr.next_node is not None and
                   ptr.next_node.data < newNode.data):
                ptr = ptr.next_node
            newNode.next_node = ptr.next_node
            ptr.next_node = newNode
