def solve_n_queens(n):
    res = []
    board = [["."]*n for _ in range(n)]

    def backtrack(r, cols, diag1, diag2):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r-c) in diag1 or (r+c) in diag2:
                continue
            board[r][c] = "Q"
            backtrack(r+1, cols|{c}, diag1|{r-c}, diag2|{r+c})
            board[r][c] = "."
    backtrack(0, set(), set(), set())
    return res
