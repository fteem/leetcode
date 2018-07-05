class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


if __name__ == '__main__':
    h1 = ListNode(3)
    h1.next = ListNode(4)
    h1.next.next = ListNode(5)
    h1.next.next.next = h1
    
    h2 = ListNode(4)
    h2.next = ListNode(5)
    h2.next.next = ListNode(4)

    assert(has_cycle(h1) == True)
    assert(has_cycle(h2) == False)
    assert(has_cycle(None) == False)
    assert(has_cycle(ListNode(1)) == False)