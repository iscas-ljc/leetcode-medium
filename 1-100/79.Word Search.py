class Solution(object):
    def exist(self, board, word):
        def find(board, word, i, j, m, n):
            if word == '':
                #找完了最后一个字符返回找到了
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
                #出界了就返回没找到
            elif word[0] == board[i][j]:
                board[i][j] = None #标记
                res = find(board, word[1:], i+1, j, m, n) or find(board, word[1:], i-1, j, m, n) or find(board, word[1:], i, j+1, m, n) or find(board, word[1:], i, j-1, m, n)
                #上下左右找
                board[i][j] = word[0] #恢复原来的值
                return res
        if len(word) == 0:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if find(board, word, i, j, m, n):
                    return True
        else:
            return False