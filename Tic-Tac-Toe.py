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
                for i in board[1:4]:
                    i = i[1:4]
                    if i == ['X', 'X', 'X']:
                        game_over = True
                        break
                for i in range(1, 4):
                    check = []
                    for stroka in board[1:4]:
                        check.append(stroka[i])
                    if check == ["X", "X", "X"]:
                        game_over = True
                        break
                if game_over:
                    break
                check = []
                check2 = []
                for i in range(1, 4):
                    stroka = board[i]
                    check.append(stroka[i])
                    check2.append(stroka[4 - i])
                if check == ["X", "X", "X"] or check2 == ["X", "X", "X"]:
                    game_over = True
                    break
                player = player_O
            elif player == player_O:
                board[player_row + 1][player_column + 1] = 'O'
                for i in board[1:4]:
                    i = i[1:4]
                    if i == ['O', 'O', 'O']:
                        game_over = True
                        break
                for i in range(1, 4):
                    check = []
                    for stroka in board[1:4]:
                        check.append(stroka[i])
                    if check == ["O", "O", "O"]:
                        game_over = True
                        break
                if game_over:
                    break
                check = []
                check2 = []
                for i in range(1, 4):
                    stroka = board[i]
                    check.append(stroka[i])
                    check2.append(stroka[4 - i])
                if check == ["O", "O", "O"] or check2 == ["O", "O", "O"]:
                    game_over = True
                    break
                player = player_X
        else:
                board[player_row + 1][player_column + 1] = 'O'
                player = player_X
                
        break
    else:
        print("Ход не защитан")
print_board(board)
if game_over:
    if player == player_X:
        print("Выиграли крестики")
    else:
        print("Выиграли нолики")
elif len(all_moves) == 9:
    print("Ничья")
