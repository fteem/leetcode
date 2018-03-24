class ListNode(object):
    """Singly-linked list"""
    def __init__(self, x):
        self.val = x
        self.next = None

def build_list(l):
    head = ListNode(l[0])
    current_node = head
    for i in range(1, len(l)):
        current_node.next = ListNode(l[i])
        current_node = current_node.next
    return head


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 and not l2:
        return
    current_node = ListNode(None)
    head = current_node
    while l1 and l2:
        if l1.val <= l2.val:
            current_node.val = l1.val
            l1 = l1.next
        else:
            current_node.val = l2.val
            l2 = l2.next
        current_node.next = ListNode(None)
        current_node = current_node.next
    if l1:
        current_node.val = l1.val
        current_node.next = l1.next
    else:
        current_node.val = l2.val
        current_node.next = l2.next
    return head

if __name__ == '__main__':
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    l3 = mergeTwoLists(l1, l2)
    l3_array = []
    while l3:
        l3_array.append(l3.val)
        l3 = l3.next
    assert(l3_array == [1, 1, 2, 3, 4, 4])
