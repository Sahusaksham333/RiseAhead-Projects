"""Sudoku Solver using Recursive Backtracking with Bitmask Pruning"""
def solve_sudoku(board):
    rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
    empties = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == 0:
                empties.append((r, c))
            else:
                rows[r].add(v); cols[c].add(v); boxes[(r//3)*3 + c//3].add(v)

    def backtrack(idx=0):
        if idx == len(empties): return True
        r, c = empties[idx]
        b = (r // 3) * 3 + c // 3
        for num in range(1, 10):
            if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                board[r][c] = num
                rows[r].add(num); cols[c].add(num); boxes[b].add(num)
                if backtrack(idx + 1): return True
                board[r][c] = 0
                rows[r].remove(num); cols[c].remove(num); boxes[b].remove(num)
        return False

    return backtrack()

if __name__ == "__main__":
    grid = [
        [5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9],
    ]
    assert solve_sudoku(grid)
    for row in grid: print(" ".join(map(str, row)))
