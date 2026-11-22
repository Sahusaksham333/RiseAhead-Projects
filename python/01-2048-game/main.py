"""2048 Puzzle Game (Console + Core Merge Engine)"""
import random

def new_board(n=4):
    b = [[0]*n for _ in range(n)]
    add_tile(b); add_tile(b)
    return b

def add_tile(b):
    empties = [(r, c) for r in range(len(b)) for c in range(len(b)) if b[r][c] == 0]
    if empties:
        r, c = random.choice(empties)
        b[r][c] = 4 if random.random() < 0.1 else 2

def compress_merge(row):
    vals = [x for x in row if x != 0]
    out, score, i = [], 0, 0
    while i < len(vals):
        if i + 1 < len(vals) and vals[i] == vals[i + 1]:
            out.append(vals[i] * 2); score += vals[i] * 2; i += 2
        else:
            out.append(vals[i]); i += 1
    return out + [0] * (len(row) - len(out)), score

def move_left(b):
    total = 0
    new_b = []
    for row in b:
        r, s = compress_merge(row)
        new_b.append(r); total += s
    return new_b, total

def transpose(b): return [list(r) for r in zip(*b)]
def reverse_rows(b): return [list(reversed(r)) for r in b]

def step(b, direction):
    if direction == "L": return move_left(b)
    if direction == "R":
        nb, s = move_left(reverse_rows(b)); return reverse_rows(nb), s
    if direction == "U":
        nb, s = move_left(transpose(b)); return transpose(nb), s
    if direction == "D":
        nb, s = move_left(reverse_rows(transpose(b))); return transpose(reverse_rows(nb)), s
    return b, 0

if __name__ == "__main__":
    board, score = new_board(), 0
    print("2048 Game — Controls: W(Up) A(Left) S(Down) D(Right) Q(Quit)")
    key_map = {"w": "U", "a": "L", "s": "D", "d": "R"}
    while True:
        print(f"\nScore: {score}")
        for r in board: print(" ".join(f"{x:4d}" if x else "   ." for x in r))
        cmd = input("Move (W/A/S/D/Q): ").strip().lower()
        if cmd == "q": break
        if cmd in key_map:
            nxt, gained = step(board, key_map[cmd])
            if nxt != board:
                board = nxt; score += gained; add_tile(board)
