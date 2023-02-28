'''
TC: O(NM), N and M are the dimensions of the input grid
MC: O(NM) 
'''

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        dir = [0, 1, 0, -1, 0]
        N = len(rooms)
        if N == 0:return
        M = len(rooms[0])
        Q = deque()

        for i in range(N):
            for j in range(M):
                if rooms[i][j] == 0:
                    Q.append((i, j))

        while Q:
            uX, uY = Q.popleft()
            for i in range(4):
                X = uX + dir[i]
                Y = uY + dir[i + 1]
                if not (0 <= X < N and 0 <= Y < M):continue
                if rooms[uX][uY] + 1 < rooms[X][Y]:
                    rooms[X][Y] = rooms[uX][uY] + 1
                    Q.append((X, Y))
                
        