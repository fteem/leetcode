def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums) # or i + 1


if __name__ == '__main__':
    assert(searchInsert([1, 3, 5, 6], 5) == 2)
    assert(searchInsert([1, 3, 5, 6], 2) == 1)
    assert(searchInsert([1, 3, 5, 6], 7) == 4)
    assert(searchInsert([1, 3, 5, 6], 0) == 0)
