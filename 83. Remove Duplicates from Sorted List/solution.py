class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None

    current_node = head
    while current_node and current_node.next:
        if current_node.val == current_node.next.val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return head

if __name__ == '__main__':
    main()
