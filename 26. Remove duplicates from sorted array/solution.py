def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    p1 = 0
    p2 = len(nums) - 1
    if p2 == -1:
        return 0
    if p2 == 0:
        return 1

    while p1 < p2:
        if p1 + 1 < len(nums) and nums[p1] == nums[p1 + 1]:
            swap(nums, p1 + 1, p2)
            p2 -= 1
        else:
            p1 += 1
    return p1 + 1

if __name__ == '__main__':
    assert(removeDuplicates([1, 1, 2]) == 2)
    assert(removeDuplicates([]) == 0)
    assert(removeDuplicates([1]) == 1)
    assert(removeDuplicates([1, 2]) == 2)
    assert(removeDuplicates([1, 1]) == 1)
    assert(removeDuplicates([1, 1, 1]) == 1)
    assert(removeDuplicates([1, 1, 1, 2]) == 2)
