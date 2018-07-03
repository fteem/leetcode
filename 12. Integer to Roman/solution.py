def int_to_roman(num):
    ROMAN = {
        1: 'I', 
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    roman = ''
    magnitude = 1

    while num > 0:
        digit = num % 10
        num //= 10
        if digit == 4:
            roman = ROMAN[magnitude] + ROMAN[magnitude*5] + roman
        elif digit == 9:
            roman = ROMAN[magnitude] + ROMAN[magnitude*10] + roman
        elif digit < 5:
            roman = ROMAN[magnitude] * int(digit % 5) + roman
        else:
            roman = ROMAN[5*magnitude] + ROMAN[magnitude] * int(digit % 5) + roman
    
        magnitude *= 10

    return roman

if __name__ == '__main__':
    assert(int_to_roman(3) == 'III')
    assert(int_to_roman(4) == 'IV')
    assert(int_to_roman(9) == 'IX')
    assert(int_to_roman(58) == 'LVIII')
    assert(int_to_roman(1994) == 'MCMXCIV')
    assert(int_to_roman(3994) == 'MMMCMXCIV')