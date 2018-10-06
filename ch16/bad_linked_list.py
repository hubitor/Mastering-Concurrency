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
        new_node = Node(value)

        current_node = self.head
        if current_node:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

        else:
            self.head = new_node

    # checks if value is in the list
    def check(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True

            current_node = current_node.next

        return False

    # precondition: value has to be in the list
    def find_index(self, value):
        current_node = self.head
        i = 0
        while current_node:
            if current_node.value == value:
                return i

            current_node = current_node.next
            i += 1

    # precondition: value has to be in the list
    def delete(self, value):
        current_node = self.head
        if current_node.value == value:
            self.head = current_node.next
            return

        while current_node.next:
            if current_node.next.value == value:
                break

            current_node = current_node.next

        current_node.next = current_node.next.next
