class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def list_search(ls, key):
    x = ls.head
    while x is not None and key != x.val:
        x = x.next
    try:
        if x.val == key:
            print(f"{key} found!")
    except AttributeError:
        print("Not found!")


def list_insert(ls, pos, key):  # Index starts at 1.
    new = Node(key)
    x = ls.head
    for i in range(pos - 1):
        x = x.next
    new.next = x.next
    x.next = new


def list_delete(ls, pos):
    x = ls.head
    for i in range(pos - 1):
        x = x.next
    temp = x
    temp.next = x.next.next


def list_edit(ls, pos, key):
    x = ls.head
    for i in range(pos - 1):
        x = x.next
    x.next.val = key


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(None)
    first = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = first
    first.next = second
    second.next = third
    list_insert(llist, 4, 100)
    n = llist.head
    while n is not None:
        print(n.val)
        n = n.next
    list_delete(llist, 1)
    n = llist.head
    while n is not None:
        print(n.val)
        n = n.next
    list_search(llist, 100)
    list_edit(llist, 3, 200)
    n = llist.head
    while n is not None:
        print(n.val)
        n = n.next
