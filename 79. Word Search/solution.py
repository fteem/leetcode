def exist_diagonal(board, word):
    # So this one will find words with diagonal adjacencies, which is NOT what
    # the assignment said. That can be solved by just using a bunch of if 
    # statements though.
    num_rows = len(board)
    num_cols = len(board[0])

    stack = []
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == word[0]:
                stack.append([(i, j)])

    while stack:
        current = stack.pop()
        if len(current) == len(word):
            return True

        char_index = len(current)
        # last character of the word
        i, j = current[-1]
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < num_rows and 0 <= y < num_cols and board[x][y] == word[char_index] and (x, y) not in current:
                    stack.append(current + [(x, y)])

    return False


def exist(board, word):
    num_rows = len(board)
    num_cols = len(board[0])

    stack = []
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == word[0]:
                stack.append([(i, j)])

    while stack:
        current = stack.pop()
        if len(current) == len(word):
            return True

        next_char_index = len(current)
        # index of the next character in the sequence we're looking for
        i, j = current[-1]
        if i - 1 >= 0 and board[i-1][j] == word[next_char_index] and (i-1, j) not in current:
            stack.append(current + [(i-1, j)])
        if i + 1 < num_rows and board[i+1][j] == word[next_char_index] and (i+1, j) not in current:
            stack.append(current + [(i+1, j)])
        if j - 1 >= 0 and board[i][j-1] == word[next_char_index] and (i, j-1) not in current:
            stack.append(current + [(i, j-1)])
        if j + 1 < num_cols and board[i][j+1] == word[next_char_index] and (i, j+1) not in current:
            stack.append(current + [(i, j+1)])

    return False

if __name__ == '__main__':
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert(exist(board, 'ABCCED') is True)
    assert(exist(board, 'SEE') is True)
    assert(exist(board, 'ABCB') is False)