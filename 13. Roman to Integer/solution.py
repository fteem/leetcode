def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    rules = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    p1 = 0
    p2 = 1
    tally = 0
    while p2 <= len(s):
        if p2 == len(s):
            tally += rules[s[p1]]
            break
        if rules[s[p1]] >= rules[s[p2]]:
            tally += rules[s[p1]]
            p1 += 1
            p2 += 1
        else:
            tally += (rules[s[p2]] - rules[s[p1]])
            p1 += 2
            p2 += 2
    return tally

if __name__ == '__main__':
    assert(romanToInt('MDCCLXXVI') == 1776)
    assert(romanToInt('MCMLIV') == 1954)
    assert(romanToInt('MCMXCIV') == 1994)
    assert(romanToInt('MMXIV') == 2014)
