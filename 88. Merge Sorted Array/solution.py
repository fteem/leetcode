def merge(nums1, m, nums2, n):
    """
    We can write to the back entries of nums1, so
    we need a pointer that keeps track of where to
    inject values. We move the pointer back, inserting
    the highest value in the last place, and decrement
    the w pointer, and the pointer to the highest value.
    """
    w = len(nums1) - 1
    p1 = m - 1
    p2 = n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[w] = nums1[p1]
            p1 -= 1
        else:
            nums1[w] = nums2[p2]
            p2 -= 1
        w -= 1

    # if there's anything left in nums2, just insert
    # those in the remaining slots
    while p2 >= 0:
        nums1[w] = nums2[p2]
        p2 -= 1
        w -= 1

    return nums1


if __name__ == '__main__':
    assert(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6])
    assert(merge([5, 7, 8, 0, 0, 0], 3, [1, 2, 6], 3) == [1, 2, 5, 6, 7, 8])
