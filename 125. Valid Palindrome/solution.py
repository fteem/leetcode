def is_palindrome(s):
    if s == '':
        return True
    deque = []
    for c in s.lower():
        if c.isalnum():
            deque.append(c)

    # you COULD just use the string and
    # two pointers, but that makes it
    # harder to read
    while len(deque) > 1:
        l = deque.pop(0)
        r = deque.pop()
        if l != r:
            return False
    return True


def python_palindrome_cheat(s):
    # Iterates over the string twice tho
    s = ''.join([c for c in s.lower() if c.isalnum()])
    return s == s[::-1]


if __name__ == '__main__':
    assert(is_palindrome('not a palindrome') is False)
    assert(is_palindrome('racecar') is True)
    assert(is_palindrome('A man, a plan, a canal: Panama') is True)
    assert(is_palindrome('race a car') is False)

    assert(python_palindrome_cheat('not a palindrome') is False)
    assert(python_palindrome_cheat('racecar') is True)
    assert(python_palindrome_cheat('A man, a plan, a canal: Panama') is True)
    assert(python_palindrome_cheat('race a car') is False)
