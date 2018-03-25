def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if haystack == needle:
        return 0
    start = 0
    end = len(needle)

    while end <= len(haystack):
        if haystack[start:end] == needle:
            return start
        start += 1
        end += 1
    return -1

if __name__ == '__main__':
    assert(strStr('hello', 'll') == 2)
    assert(strStr('aaaaa', 'bba') == -1)
    assert(strStr('', '') == 0)
    assert(strStr('bla', 'b') == 0)
    assert(strStr('mississippi', 'pi') == 9)
