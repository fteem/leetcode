def num_islands(grid):
    scores = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            scores.append(is_new_island(grid, i, j))
    return sum(scores)

    
def is_new_island(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
        return 0

    grid[x][y] = '-1'
    for i in [-1, 1]:
        is_new_island(grid, x + i, y)
        is_new_island(grid, x, y + 1)
    return 1



if __name__ == '__main__':
    grid1 = [['1','1','1','1','0'],
             ['1','1','0','1','0'],
             ['1','1','0','0','0'],
             ['0','0','0','0','0']]
    grid2 = [['1','1','0','0','0'],
             ['1','1','0','0','0'],
             ['0','0','1','0','0'],
             ['0','0','0','1','1']]
    assert(num_islands(grid1) == 1)
    assert(num_islands(grid2) == 3)
