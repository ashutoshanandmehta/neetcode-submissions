class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row checkup
        for x in board:
            d = {}

            for i in x:
                if i == ".":
                    continue
                else:
                    if i not in d.keys():
                        d[i] = 1
                    else:
                        d[i] = d[i] + 1

            if d and max(d.values()) > 1:
                return False


        # Column checkup
        for i in range(0, len(board)):
            column = [board[j][i] for j in range(len(board))]
            d = {}

            for k in column:
                if k == ".":
                    continue
                else:
                    if k not in d.keys():
                        d[k] = 1
                    else:
                        d[k] = d[k] + 1

            if d and max(d.values()) > 1:
                return False


        # Sub-boxes checkup
        for i in range(3):
            rows = board[i*3:(i+1)*3]

            for j in range(3):
                subbox = {}

                for k in range(3):
                    window = rows[k][j*3:(j+1)*3]

                    for x in window:
                        if x == ".":
                            continue
                        else:
                            if x not in subbox.keys():
                                subbox[x] = 1
                            else:
                                subbox[x] = subbox[x] + 1

                if subbox and max(subbox.values()) > 1:
                    return False

        return True