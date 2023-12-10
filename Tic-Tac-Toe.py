seq_num_move = ("Первый", "Второй", "Третий", "Четвёртый", "Пятый", "Шестой", "Седьмой", "Восьмой", "Девятый")

board = [[' ', '0', '1', '2'],
         ['0', '-', '-', '-'],
         ['1', '-', '-', '-'],
         ['2', '-', '-', '-']]


def print_board(desk):
    for row in desk:
        line = ''
        for cell in row:
            line += cell + " "
        print(line)


player_X = 'X'
player_O = 'O'
win_X = ['X', 'X', 'X']
win_O = ['O', 'O', 'O']

# preparing for the game
player = player_X
num_of_moves = 1
game_over = False

# start game
while (game_over != True) and (num_of_moves < 10):
    print(f"{seq_num_move[num_of_moves - 1]} ход")
    num_of_moves += 1
    print_board(board)
    if player == player_X:
        print("Ходят крестики")
    else:
        print("Ходят нолики")
    while True:
        pass
        break