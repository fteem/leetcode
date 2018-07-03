"""Add Two Numbers module"""

class ListNode(object):
    """List node representation"""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """Solution class"""
    def __init__(self):
        """Constructor"""
        self._head = None
        self._tail = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self._head = ListNode(0)
        self._tail = self._head
        carry = 0
        while l1 is not None or l2 is not None:
            summary = self._value(l1) + self._value(l2) + carry
            carry = summary / 10
            self._create_node(summary % 10)
            l1 = self._next(l1)
            l2 = self._next(l2)
        if carry is 1:
            self._create_node(carry)
        return self._head.next

    # Private section

    @staticmethod
    def _value(node):
        return 0 if node is None else node.val

    @staticmethod
    def _next(node):
        return None if node is None else node.next

    def _create_node(self, val):
        self._tail.next = ListNode(val)
        self._tail = self._tail.next

class SumHelper(object):
    """SumHelper class"""
    def __init__(self, a, b):
        self._first_list = self._array_to_linked_list(a)
        self._second_list = self._array_to_linked_list(b)

    def sum(self, as_array=True):
        """
        Adds 2 linked lists and
        represents the output linked list as an array or a linked list
        """
        res_list = Solution().addTwoNumbers(self._first_list, self._second_list)
        return self._linked_list_to_array(res_list) if as_array else res_list

    # Private section

    @staticmethod
    def _array_to_linked_list(array):
        """Converts an array into a linked list"""
        head = None
        tail = None
        for value in array:
            if head is None:
                head = ListNode(value)
                tail = head
            else:
                tail.next = ListNode(value)
                tail = tail.next
        return head

    @staticmethod
    def _linked_list_to_array(linked_list):
        """Converts a linked list into an array"""
        array = []
        head = linked_list
        while head is not None:
            array.append(head.val)
            head = head.next
        return array

if __name__ == '__main__':
    assert SumHelper([2, 4, 3], [5, 6, 4]).sum() == [7, 0, 8]
    assert SumHelper([2, 4], [5, 6, 4]).sum() == [7, 0, 5]
    assert SumHelper([2], [5, 6, 4]).sum() == [7, 6, 4]
    assert SumHelper([9, 9, 9], [1]).sum() == [0, 0, 0, 1]
    assert SumHelper([9, 9, 9], [1, 2]).sum() == [0, 2, 0, 1]
    assert SumHelper([], []).sum() == []
    assert SumHelper([], [1, 2, 3]).sum() == [1, 2, 3]
