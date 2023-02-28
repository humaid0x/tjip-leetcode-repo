'''
TC: O(NM), N is the number of rows in the grid and M is the number of columns in the grid
MC: O(NM) 
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        vis = [[0 for j in range(M)] for i in range(N)]
        islandCount = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '0' or vis[i][j]:continue
                self.dfs(grid, i, j, N, M, vis)
                islandCount += 1
        return islandCount

    def dfs(self, arr, uX, uY, N, M, vis):
        dir = [0, 1, 0, -1, 0]
        vis[uX][uY] = 1
        for i in range(4):
                X = uX + dir[i]
                Y = uY + dir[i + 1]
                if not (0 <= X < N and 0 <= Y < M):continue
                if arr[X][Y] == '0' or vis[X][Y]:continue
                self.dfs(arr, X, Y, N, M, vis)
