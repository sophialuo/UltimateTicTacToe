# -*- coding: utf-8 -*-

class UltimateTicTacToe():
    
    def __init__(self):
        self.board = {'a': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'b': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'c': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'd': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'e': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'f': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'g': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'h': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
                      'i': [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]}
        self.minis = {'a':0, 'b':0, 'c':0,
                      'd':0, 'e':0, 'f':0,
                      'g':0, 'h':0, 'i':0}
    
    def print_setup(self):
        print("")
        print("Type a, b, c, d, e, f, g, h, i to reference the mini tic tac toe games throughout the game")
        keys = sorted(list(self.board.keys()))
        for num in range(0,9,3):
            key0 = keys[num]
            key1 = keys[num+1]
            key2 = keys[num+2]
            line = ''
            for i in range(3):
                for key in [key0,key1,key2]:
                    for j in range(3):
                        if j == 2:
                            line += ' ' + key + '  ' + '$ '
                        else:
                            line += ' ' + key + ' ' + '|' 
                print(line[:-2])
                line = ''
                sep = '----------- $ '
                if i == 2:
                    sep = '~~~~~~~~~~~~~~'
                if i == 2 and num == 6:
                    break
                print(sep+sep+sep[:-2])
        
        print("")
        print("Within each mini game, reference each location by row and column")
        for i in range(3):
            line = ''
            for j in range(3):
                line += ' ' + str((i,j)) + ' ' + '|'
            print(line[:-2])
            if i != 2:
                print('--------------------------')
        print("")

    def print_board(self):
        keys = sorted(list(self.board.keys()))
        for num in range(0,9,3):
            key0 = keys[num]
            key1 = keys[num+1]
            key2 = keys[num+2]
            line = ''
            for i in range(3):
                for key in [key0,key1,key2]:
                    for j in range(3):
                        if j == 2:
                            line += ' ' + self.board[key][i][j] + '  ' + '$ '
                        else:
                            line += ' ' + self.board[key][i][j] + ' ' + '|' 
                print(line[:-2])
                line = ''
                sep = '----------- $ '
                if i == 2:
                    sep = '~~~~~~~~~~~~~~'
                if i == 2 and num == 6:
                    break
                print(sep+sep+sep[:-2])
    
    #key: which board
    #coordinates: (row, col)
    def valid_move(self, key, coordinates):
        row, col = coordinates
        return row.isdigit() and col.isdigit() and \
               int(row) in [0, 1, 2] and int(col) in [0, 1, 2] and \
               self.board[key][int(row)][int(col)] == ' '

    #key: which board
    #player: which player
    #coordinates: (row, col)
    def make_move(self, key, player, coordinates):
        row, col = coordinates
        self.board[key][row][col] = player
        self.print_board()
    
    #key: which board
    #player: which player
    #coordinates: (row, col)
    def next_move(self, key, player, coordinates):
        row, col = coordinates
        self.board[key][row][col] = player

        next_mini = ''
        if row == 0:
            if col == 0:
                next_mini = 'a'
            if col == 1:
                next_mini = 'b'
            if col == 2:
                next_mini = 'c'
        elif row == 1:
            if col == 0:
                next_mini = 'd'
            if col == 1:
                next_mini = 'e'
            if col == 2:
                next_mini = 'f'
        elif row == 2:
            if col == 0:
                next_mini = 'g'
            if col == 1:
                next_mini = 'h'
            if col == 2:
                next_mini = 'i'
        #when the board directed to has already been won
        if self.minis[next_mini] != 0:
            remaining = self.remaining_minis()
            print("Possible mini boards: " + " ".join(remaining))
            mini = input('Mini board letter: ')
            while mini not in remaining:
                mini = input('Input the letter of a mini board that has not been won yet: ')
            return mini    

        return next_mini
    

    def remaining_minis(self):
        result = []
        for key in self.minis:
            if self.minis[key] == 0:
                result.append(key)
        return sorted(result)

    #key = which mini 'a', 'b', 'c', etc.
    #player = player X or player O
    def mini_win(self, key, player):
        mini_board = self.board[key]
        #horizontal or vertical 3 in a row
        for i in range(3):
            #horizontal 3 in a row
            if mini_board[i][0] == mini_board[i][1] and \
            mini_board[i][0] == mini_board[i][2] and mini_board[i][0] == player:
                self.minis[key] = player
                return True
            #vertical 3 in a row
            if mini_board[0][i] ==  mini_board[1][i] and \
            mini_board[0][i] == mini_board[2][i] and mini_board[0][i] == player:
                self.minis[key] = player
                return True
        #diagonal 3 in a row
        if mini_board[0][0] == mini_board[1][1] and \
        mini_board[0][0] == mini_board[2][2] and mini_board[0][0] == player:
                self.minis[key] = player
                return True     
        if mini_board[0][2] == mini_board[1][1] and \
        mini_board[0][2] == mini_board[2][0] and mini_board[0][2] == player:
                self.minis[key] = player
                return True                          
        return False
        
    def game_over(self):
        xs = 0
        os = 0
        for key in self.minis:
            if self.minis[key] == 0:
                return False
            if self.minis[key] == 'X':
                xs += 1
            elif self.minis[key] == 'O':
                os += 1
        
        if xs > os:
            print('Player X wins!')
        elif os > xs:
            print('Player O wins!')
        else:
            print("It's a tie!")
        return True

    
    def __main__(self):
        print('Welcome to the Ultimate Tic-Tac-Toe game')
        self.print_setup()

        index = 0
        next_mini = '' 
        while not self.game_over():
            player = ''
            if index == 0:
                next_mini = input('Player X input a letter for a mini board: ')
                player = 'X'
            elif index % 2 == 0:
                print('Player X next move must be in ' + next_mini)
                player = 'X'
            else:
                print('Player O next move must be in ' + next_mini)
                player = 'O'

            row = input('row: ')
            col = input('col: ')

            while not self.valid_move(next_mini, (row, col)):
                print("That is an invalid location.")
                row = input('Please input a valid row: ')
                col = input('Please input a valid col: ')
            row, col = int(row), int(col)

            self.make_move(next_mini, player, (row, col))


            if self.mini_win(next_mini, player) == True:
                if self.game_over():
                    break
                print('Player ' + player + ' has won mini board ' + next_mini + 
                  '. Any directed moves to this mini board can be placed in any valid mini board.')
            
            next_mini = self.next_move(next_mini, player, (row, col))
            index += 1

            
        
        
a = UltimateTicTacToe()
a.__main__()
