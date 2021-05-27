from definition import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0, head)
        head = sentinel
        while sentinel.next:
            if sentinel.next.val == val:
                sentinel.next = sentinel.next.next
            else:
                sentinel = sentinel.next
        return head.next
