from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        self.visited = "#"
        self.word_len = len(word)
        start = end = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    start += 1
                elif board[r][c] == word[-1]:
                    end += 1

        if start > end:
            word = word[::-1]

        for i in range(n):
            for j in range(m):
                if self.dfs(board, i, j, 0, word):
                    return True

        return False

    def dfs(self, board: List[List[str]], i: int, j: int, k: int, word: str) -> bool:
        if k == self.word_len:
            return True

        n, m = len(board), len(board[0])
        if (i < 0 or i >= n) or (j < 0 or j >= m) or word[k] != board[i][j]:
            return False

        board[i][j] = self.visited
        res = self.dfs(board, i + 1, j, k + 1, word) or \
              self.dfs(board, i - 1, j, k + 1, word) or \
              self.dfs(board, i, j + 1, k + 1, word) or \
              self.dfs(board, i, j - 1, k + 1, word)
        board[i][j] = word[k]

        return res

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

obj = Solution()
obj.exist(board,word)