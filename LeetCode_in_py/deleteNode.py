from definition import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0, head)
        head = sentinel
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                return sentinel.next
            head = head.next
        return sentinel.next
