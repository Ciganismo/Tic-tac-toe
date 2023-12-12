seq_num_move = ("Первый", "Второй", "Третий", "Четвёртый", "Пятый", "Шестой", "Седьмой", "Восьмой", "Девятый")
possible_moves = (0, 1, 2, 10, 11, 12, 20, 21, 22)
all_moves = []
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

# preparing for the game
player = player_X
game_over = False

# start game
while (not game_over) and (len(all_moves) < 9):
    print(f"{seq_num_move[len(all_moves)]} ход")
    print_board(board)
    if player == player_X:
        print("Ходят крестики")
    else:
        print("Ходят нолики")
    while True:
        player_row = input("Введите номер строки(0,1,2):")
        player_column = input("Введите номер столбца(0,1,2):")
        player_move = int(player_row + player_column)
        player_row = int(player_row)
        player_column = int(player_column)
        if (player_move in possible_moves) and (player_move not in all_moves):
            print("Ход защитан")
            all_moves.append(player_move)

            if player == player_X:
                board[player_row + 1][player_column + 1] = 'X'
                player = player_O
            else:
                board[player_row + 1][player_column + 1] = 'O'
                player = player_X
            break
        else:
            print("Ход не защитан")