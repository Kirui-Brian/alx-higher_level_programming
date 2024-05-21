#!/usr/bin/python3
"""
Module: singly_linked_list

This module defines a Node class for elements in a singly linked list,
and a SinglyLinkedList class for managing nodes and insertion in sorted order.
"""


class Node:
    """
    Node class for a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initialization called when an instance of the Node class is created.

        Parameters:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the list, default is None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.
        """
        if self.__validate_data(data):
            self.__data = data
        if self.__validate_node(next_node):
            self.__next_node = next_node

    @property
    def data(self):
        """
        Getter for the data attribute.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute. Validates that the data is an integer.

        Parameters:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if self.__validate_data(value):
            self.__data = value

    @property
    def next_node(self):
        """
        Getter for the next_node attribute.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute. Validates that the next node is a
        Node object or None.

        Parameters:
            value (Node): The new next node in the list.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if self.__validate_node(value):
            self.__next_node = value

    def __validate_data(self, data):
        """
        Validates the data, checking its type.

        Parameters:
            data (int): The data to be validated.

        Returns:
            bool: True if data is a valid integer, False otherwise.

        Raises:
            TypeError: If data is not an integer.
        """
        if isinstance(data, int):
            return True
        raise TypeError("data must be an integer")

    def __validate_node(self, node):
        """
        Validates the node, checking if it's a Node object or None.

        Parameters:
            node (Node): The node to be validated.

        Returns:
            bool: True if node is a valid Node object or None, False otherwise.

        Raises:
            TypeError: If node is not a Node object or None.
        """
        if isinstance(node, Node) or node is None:
            return True
        raise TypeError("next_node must be a Node object or None")


class SinglyLinkedList:
    """
    SinglyLinkedList class for managing a singly linked list.

    Attributes:
        __head (Node): The head node of the list.
    """
    def __init__(self):
        """
        Initialization called when an instance of the SinglyLinkedList class
        is created.
        """
        self.__head = None

    def __str__(self):
        """
        Used by print to represent the linked list as a string.

        Returns:
            str: The string representation of the linked list.
        """
        tmp = self.__head
        string = ""
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += '\n'
        return string

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position (based on data).

        Parameters:
            value (int): The data to be stored in the new node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
