seq_num_move = ("Первый", "Второй", "Третий", "Четвёртый", "Пятый", "Шестой", "Седьмой", "Восьмой", "Девятый")
filled_columns = []
filled_rows = []
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
while (not game_over) and (num_of_moves < 10):
    print(f"{seq_num_move[num_of_moves - 1]} ход")
    num_of_moves += 1
    print_board(board)
    if player == player_X:
        print("Ходят крестики")
    else:
        print("Ходят нолики")
    while True:
        player_row = int(input("Введите номер строки(0,1,2):"))
        player_column = int(input("Введите номер столбца(0,1,2):"))
        if ((player_row in range(0, 3)) and (player_row not in filled_rows)) \
                and ((player_column in range(0, 3)) and (player_column not in filled_columns)):
            filled_rows.append(player_row)
            filled_columns.append(player_column)
        else:
            print(False)
