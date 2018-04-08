def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # Python formats binary strings with a '0b' prefix
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    assert(addBinary('1', '11') == '100')
