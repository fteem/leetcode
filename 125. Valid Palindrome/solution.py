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


if __name__ == '__main__':
    assert(is_palindrome('not a palindrome') == False)
    assert(is_palindrome('racecar') == True)
    assert(is_palindrome('A man, a plan, a canal: Panama') == True)
    assert(is_palindrome('race a car') == False)
