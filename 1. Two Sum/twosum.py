def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_indices = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_indices:
            return num_indices[diff], i
        num_indices[num] = i

if __name__ == '__main__':
    assert(twoSum([2, 7, 11, 15], 9) == (0, 1)
    assert(twoSum([2, 2], 4) == (0, 1))
