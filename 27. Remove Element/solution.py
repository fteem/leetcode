def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if not nums:
        return 0

    p1 = 0
    for p2 in range(0, len(nums)):
        if nums[p2] != val:
            nums[p1] = nums[p2]
            p1 += 1
    return p1

if __name__ == '__main__':
    assert(removeElement([3, 2, 2, 3], 3) == 2)
    assert(removeElement([], 0) == 0)
    assert(removeElement([1], 1) == 0)
    assert(removeElement([3, 3], 3) == 0)
    assert(removeElement([4, 5], 5) == 1)
