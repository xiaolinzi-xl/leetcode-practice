#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
# @lc code=start
import queue


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1:
            return 1
        visit_queue = queue.Queue()
        ans = -1
        visit_queue.put(((0, 0), 1))
        directions = ((-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1))
        visit_array = [[0] * n for _ in range(n)]
        visit_array[0][0] = 1
        while not visit_queue.empty():
            idx, step = visit_queue.get()
            for direction in directions:
                x, y = idx[0] + direction[0], idx[1] + direction[1]
                if n > x >= 0 and n > y >= 0 and grid[x][y] == 0 and visit_array[x][y] == 0:
                    visit_queue.put(((x, y), step+1))
                    visit_array[x][y] = 1
                    if x == n-1 and y == n-1:
                        return step + 1
        return ans

# @lc code=end
