class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_cnt = len(grid)
        col_cnt = 0
        if row_cnt > 0:
            col_cnt = len(grid[0])
        perimeter = 0
        for i in range(row_cnt):
            for j in range(col_cnt):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    if i == row_cnt - 1 or grid[i+1][j] == 0:
                        perimeter += 1
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    if j == col_cnt - 1 or grid[i][j+1] == 0:
                        perimeter += 1
        return perimeter

if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    print(s.islandPerimeter(grid))
