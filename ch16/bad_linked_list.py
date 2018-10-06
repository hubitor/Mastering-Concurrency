class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # adds another node with 'value' at the end of the list
    def add_at_tail(self, value):
        new_node = Node(value)

        current_node = self.head

        if current_node:
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node

        else:
            self.head = new_node

    # finds and returns the index of the first occurence of 'value' in the list
    # returns 'False' if 'value' is not in the list
    def find_index_of(self, value):
        current_node = self.head
        i = 0

        while current_node:
            if current_node.value == value:
                return i

            current_node = current_node.next
            i += 1

        return False

    # deletes the 'delete_index'-th node in the list and returns its value
    # returns 'False' if 'delete_index' is out of bound
    def delete_at_index(self, delete_index):
        if self.head:
            if delete_index == 0:
                delete_value = self.head.value
                self.head = self.head.next
                return delete_value

            current_node = self.head
            i = 0

            while i < delete_index - 1:
                current_node = current_node.next
                i += 1

                if current_node is None:
                    return False

            delete_value = current_node.next.value
            current_node.next = current_node.next.next
            return delete_value

        return False
