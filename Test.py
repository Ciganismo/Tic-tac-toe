board = [[' ', '0', '1', '2'],
         ['0', 'X', 'X', 'X'],
         ['1', 'X', 'X', 'X'],
         ['2', 'X', 'X', 'X']]
for i in range(1,4):
        check = []
        for stroka in board[1:4]:
            check.append(stroka[i])
        if check == ["X", "X", "X"]:
           print(True)
        else:
            print(False)