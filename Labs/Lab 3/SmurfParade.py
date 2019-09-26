class node:

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
        return f'{self.data}'


class smurf_parade:
    def __init__(self, head):
        self.head = head

    def append(self, item):
        current = self.head
        while current.next is not None:
            current = current.next
        current.set_next(item)

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def __contains__(self, item):
        current = self.head
        while current is not None:
            if item.data == current.data:
                return True
            current = current.next
        return False

    def __iter__(self):
        smurf_list = []
        current = self.head
        while current is not None:
            smurf_list.append(current)
            current = current.next
        return iter(smurf_list)

    def __getitem__(self, key):
        current = self.head
        count = 0
        while current is not None:
            if key == count:
                return current
            current = current.next
            count += 1
        return False

    def count(self, item):
        current = self.head
        count = 0
        while current is not None:
            if item.data == current.data:
                count += 1
            current = current.next
        return count

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            if item.data == current.data:
                return count
            current = current.next

    def __reversed__(self):
        current = self.head


def main():
    smurf_a = node('smurf A', None)
    smurf_b = node('smurf B', None)
    smurf_c = node('smurf C', None)
    smurf_d = node('smurf D', None)
    smurfs = smurf_parade(smurf_a)
    smurfs.append(smurf_b)
    smurfs.append(smurf_c)
    smurfs.append(smurf_d)
    print(f'There are {len(smurfs)} smurfs in the parade. They are:')
    for smurf in smurfs:
        print(smurf)
    print(f'Is smurf B in the parade?: {smurfs.__contains__(smurf_b)}\n'
          f'How many smurf B are there? {smurfs.count(smurf_b)}')
    print(f'Which smurf is the 3rd smurf in parade? {smurfs[2]}')
    print(f'Smurf D is the {smurfs.index(smurf_c)}th in the parade.')


if __name__ == '__main__':
    main()
