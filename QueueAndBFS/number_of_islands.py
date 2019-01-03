# coding: utf-8

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '*'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)

if __name__ == '__main__':
    test_input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    solution = Solution()
    answer = solution.numIslands(test_input)
    print("answer is: ", answer)
    assert answer == 1
