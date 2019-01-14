# coding: utf-8

def num_islands(grid):
    """
    type grid: List[List[str]]
    rtype: int
    """
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    count = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count


if __name__ == '__main__':
    input_a = [
            ["1", "1", "1", "1", "0"],
   ["1", "1", "0", "1", "0"], 
   ["1", "1", "0", "0", "0"], 
   ["0", "0", "0", "0", "0"]
    ]
    print(num_islands(input_a))
