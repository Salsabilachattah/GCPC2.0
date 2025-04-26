def isValid(board, x, y):
            for i in range(9):
                if i != x and board[i][y] == board[x][y]:
                    return False
            for j in range(9):
                if j != y and board[x][j] == board[x][y]:
                    return False
            i = int(3 * (x / 3) )
            while int(i < 3 * (x / 3 + 1)) and i < 9:
                j = int(3 * (y / 3) )

                while j < int(3 * (y / 3 + 1))and j < 9:
                    print('jj',j)
                    if (i != x or j != y) and board[i][j] == board[x][y]:
                        return False
                    j += 1
                i += 1
            return True

def solver(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j] == '0'):
                        for k in range(9):
                            board[i][j] = chr(ord('1') + k)
                            if isValid(board, i, j) and solver(board):
                                return True
                            board[i][j] = '0'
                        return False
            return True
import sys
# solver(board)
board = [[0]*9]*9
i = 0
for line in sys.stdin : 
      s = line.split()
    #   print(' i ', i)
      board[i] = s

      i += 1
# print(board)
# s = Solution()
# print(isValid(board))

solver(board)
print(board)
