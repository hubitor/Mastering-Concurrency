from copy import deepcopy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ''
        current_node = self.head
        while current_node:
            result += f'{current_node.value} - '
            current_node = current_node.next

        return result[: -3]

    def add(self, value):
        copy_list = deepcopy(self)

        new_node = Node(value)

        current_node = copy_list.head
        if current_node:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

        else:
            copy_list.head = new_node

        self = copy_list
