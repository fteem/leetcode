def three_sum(nums):
    nums.sort()
    results = []

    for i in range(len(nums) - 2):
        # skip number if we've already seen it before
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                results.add((nums[i], nums[left], nums[right]))
                left += 1
    return list(results)

if __name__ == '__main__':
    assert(tree_sum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]])