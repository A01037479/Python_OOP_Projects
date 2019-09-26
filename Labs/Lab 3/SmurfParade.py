class node:
    """
    Class represents node that contains string type data and a pointer that
    points to another node
    """
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node

    def get_data(self):
        return self._data

    def set_data(self, value):
        self._data = value

    def get_next(self):
        return self._next_node

    def set_next(self, item):
        self._next_node = item

    next = property(get_next, set_next)

    data = property(get_data, set_data)

    def __str__(self):
        """
        returns String representation to print out data of a node
        :return: String
        """
        return f'{self.data}'


class smurf_parade:
    """
    A linked list that contains a head node
    """
    def __init__(self, head):
        self.head = head

    def append(self, item):
        """
        Appends a node to the end of the trailing node
        :param item: Node
        """
        current = self.head
        while current.next is not None:
            current = current.next
        current.set_next(item)

    def __len__(self):
        """
        Measures the number of nodes in the linked list
        :return: Int
        """
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def __contains__(self, item):
        """
        Checks if the linked list contains a specific node
        :param item: Node
        :return: Boolean
        """
        current = self.head
        while current is not None:
            if item.data == current.data:
                return True
            current = current.next
        return False

    def __iter__(self):
        """
        Makes the linked list iterable
        :return: smurf_list
        """
        smurf_list = []
        current = self.head
        while current is not None:
            smurf_list.append(current)
            current = current.next
        return iter(smurf_list)

    def __getitem__(self, key):
        """
        Checks and returns a node at index of key
        :param key: int
        :return: Node
        """
        current = self.head
        count = 0
        while current is not None:
            if key == count:
                return current
            current = current.next
            count += 1
        return False

    def count(self, item):
        """
        Measures and returns the number of times the data of a node appears
        :param item: Node
        :return: int
        """
        current = self.head
        count = 0
        while current is not None:
            if item.data == current.data:
                count += 1
            current = current.next
        return count

    def index(self, item):
        """
        Checks and returns the index of a node that's in the linked list
        :param item: Node
        :return: int
        """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            if item.data == current.data:
                return count
            current = current.next

    def __reversed__(self):
        """
        Creates a new linked list that is reversed of the linked list
        :return: smurf_parade
        """
        if self.head is None or self.head.next is None:
            return smurf_parade(self.head)
        new_head = self.head
        current_node = new_head
        prev_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        new_head = prev_node

        return smurf_parade(new_head)


def main():
    smurf_a = node('smurf A', None)
    smurf_b = node('smurf B', None)
    smurf_b2 = node('smurf B', None)
    smurf_c = node('smurf C', None)
    smurf_d = node('smurf D', None)
    smurfs = smurf_parade(smurf_a)
    smurfs.append(smurf_b)
    smurfs.append(smurf_c)
    smurfs.append(smurf_d)
    smurfs.append(smurf_b2)
    print(f'There are {len(smurfs)} smurfs in the parade. '
          f'\nThey are:')
    for smurf in smurfs:
        print(smurf)
    print(f'Is smurf B in the parade?:             '
          f'{smurf_b in smurfs}\n'
          f'How many smurf B are there?            {smurfs.count(smurf_b)}')
    print(f'Which smurf has index of 2 in parade?  {smurfs[2]}')
    print(f'What index does Smurf D have?          {smurfs.index(smurf_c)}')
    for smurf in reversed(smurfs):
        print(smurf)


if __name__ == '__main__':
    main()
