def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    words = s.split()
    if not words:
        return 0
    return len(words[-1])

if __name__ == '__main__':
    assert(lengthOfLastWord('Hello world') == 5)
    assert(lengthOfLastWord('') == 0)
    assert(lengthOfLastWord('   ') == 0)
    assert(lengthOfLastWord('hello   ') == 5)
