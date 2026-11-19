class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        board_dict_row = defaultdict(list)
        board_dict_col = defaultdict(list)
        board_dict_occupied = defaultdict(list)
        for i in range(row):
            for j in range(col):
                curr = board[i][j]
                if curr == ".":
                    continue
                if board_dict_row[curr] and i in board_dict_row[curr]:
                    return False                      
                else:
                    board_dict_row[curr].append(i)
                if board_dict_col[curr] and j in board_dict_col[curr]:
                    return False
                else:
                    board_dict_col[curr].append(j)
                starting_tuple = (3*(i//3), 3*(j//3))
                if board_dict_occupied[starting_tuple] and curr in board_dict_occupied[starting_tuple]:
                    return False
                else:
                    board_dict_occupied[starting_tuple].append(curr)
        return True