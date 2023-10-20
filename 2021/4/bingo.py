with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')
rolls = [int(c) for c in rows[0].split(',')]
boards = rows[1:]
boards = [[[int(value) for value in row.split()] for row in board.split('\n')] for board in boards]
checks = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
wins = [False for _ in range(len(boards))]
print(boards[0])
print(boards[1])
print(boards[2])
winner = -1
for r in rolls:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, value in enumerate(row):
                if value == r:
                    checks[i][j][k] = True
        if not wins[i]:
            for j in range(5):
                check = [checks[i][j][k] for k in range(5)]
                if all(check):
                    if winner == -1:
                        winner = i
                        fr = r
                        winning_board = [[e for e in row] for row in boards[i]]
                        winning_checks = [[e for e in row] for row in checks[i]]
                    wins[i] = True
                    last_winner = i
                check = [checks[i][k][j] for k in range(5)]
                if all(check):
                    if winner == -1:
                        winner = i
                        fr = r
                        winning_board = [[e for e in row] for row in boards[i]]
                        winning_checks = [[e for e in row] for row in checks[i]]
                    wins[i] = True
                    last_winner = i
    if all(wins):
        loser = last_winner
        break
for aa in range(5):
    print([str(a).ljust(6) for a in winning_board[aa]])
for aa in range(5):
    print([str(a).ljust(6) for a in winning_checks[aa]])
sum = 0
for j, row in enumerate(winning_board):
    for k, value in enumerate(row):
        if not winning_checks[j][k]:
            sum += value
sum2 = 0
for j, row in enumerate(boards[loser]):
    for k, value in enumerate(row):
        if not checks[loser][j][k]:
            sum2 += value

print(winner)
print(loser)
print(sum, fr, sum*fr)
print(sum2, r, sum2*r)