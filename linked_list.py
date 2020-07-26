class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


def list_search(ls, key):
    x = ls
    while x is not None and key != x.val:
        x = x.next
    try:
        if x.val == key:
            print(f"{key} found!")
    except AttributeError:
        print(f"{key} Not found!")


def list_insert(ls, pos, key):  # Index starts at 1.
    new = ListNode(key)
    x = ls
    for i in range(pos - 1):
        x = x.next
    new.next = x.next
    x.next = new


def list_delete(ls, pos):
    x = ls
    for i in range(pos - 1):
        x = x.next
    temp = x
    temp.next = x.next.next


def list_edit(ls, pos, key):
    x = ls
    for i in range(pos - 1):
        x = x.next
    x.next.val = key


if __name__ == '__main__':
    llist = ListNode(None)
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    llist.next = first
    first.next = second
    second.next = third
    list_insert(llist, 4, 100)
    n = llist
    while n is not None:
        print(n.val)
        n = n.next
    list_delete(llist, 1)
    n = llist
    while n is not None:
        print(n.val)
        n = n.next
    list_search(llist, 100)
    list_edit(llist, 3, 200)
    n = llist
    while n is not None:
        print(n.val)
        n = n.next
