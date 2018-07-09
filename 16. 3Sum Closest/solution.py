import sys

def three_sum_closest(nums, target):
    nums.sort()
    gap = sys.maxsize
    result = 0

    for i in range(len(nums) - 2):
        # skip number if we've already seen it before
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if abs(s - target) < gap:
                result = s
                gap = abs(s - target)
            if target - s > 0:
                left += 1
            elif target - s < 0:
                right -= 1
            else:
                return s
    return result

if __name__ == '__main__':
    assert(three_sum_closest([-1, 2, 1, -4], 1) == 2)