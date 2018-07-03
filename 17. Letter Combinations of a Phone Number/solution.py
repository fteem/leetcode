import itertools

NUMBERS_TO_LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def letter_combinations_itertools(digits):
    if not digits:
        return []
    
    letters = [NUMBERS_TO_LETTERS[digit] for digit in digits]
    return [''.join(candidate) for candidate in itertools.product(*letters)]


def letter_combinations_backtrack(digits):
    if not digits:
        return []

    queue = ['']

    for digit in digits:
        for _ in range(len(queue)):
            s = queue.pop(0)
            for char in NUMBERS_TO_LETTERS[digit]:
                queue.append(s + char)
    return queue

if __name__ == '__main__':
    assert(letter_combinations_itertools('') == [])
    assert(letter_combinations_itertools('4') == ['g', 'h', 'i'])
    assert(letter_combinations_itertools('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
    assert(letter_combinations_itertools('232') == ['ada', 'adb', 'adc', 'aea', 'aeb', 'aec', 'afa', 'afb', 'afc', 'bda', 'bdb', 'bdc', 'bea', 'beb', 'bec', 'bfa', 'bfb', 'bfc', 'cda', 'cdb', 'cdc', 'cea', 'ceb', 'cec', 'cfa', 'cfb', 'cfc'])

    assert(letter_combinations_backtrack('') == [])
    assert(letter_combinations_backtrack('4') == ['g', 'h', 'i'])
    assert(letter_combinations_backtrack('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
    assert(letter_combinations_backtrack('232') == ['ada', 'adb', 'adc', 'aea', 'aeb', 'aec', 'afa', 'afb', 'afc', 'bda', 'bdb', 'bdc', 'bea', 'beb', 'bec', 'bfa', 'bfb', 'bfc', 'cda', 'cdb', 'cdc', 'cea', 'ceb', 'cec', 'cfa', 'cfb', 'cfc'])