import ast


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr  = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


if __name__ == "__main__":
    raw = input("Enter list (e.g. [1,2,3,4,5]): ").strip()
    head = build_list(ast.literal_eval(raw))
    result = Solution().reverseList(head)
    print(to_list(result))