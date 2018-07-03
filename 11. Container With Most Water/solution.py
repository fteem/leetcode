def max_area(height):
    i = 0
    j = len(height) - 1
    max_area = 0

    while i < j:
        # j - i gives x distance
        # min of the heights gives the height of the rectangle
        area = (j - i) * min(height[i], height[j])
        if area > max_area:
            max_area = area
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return max_area

if __name__ == '__main__':
    assert(max_area([1, 2]) == 1)
    assert(max_area([2, 4, 3, 8, 6]) == 12)