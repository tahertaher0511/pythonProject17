class Tictactoe:
    def __init__(self):
        self.cells = '-' * 9
        self.turn = 'X'

    def print_field(self):
        print('-' * 9)
        print(f'| {self.cells[0]} {self.cells[1]} {self.cells[2]} |')
        print(f'| {self.cells[3]} {self.cells[4]} {self.cells[5]} |')
        print(f'| {self.cells[6]} {self.cells[7]} {self.cells[8]} |')
        print('-' * 9)

    def result(self):
        if self.impossible():
            print('IMPOSSIBLE!')
        # elif self.wins(self.turn):
            # print(self.turn, 'wins')
        elif self.wins('X'):
            print('X wins')
        elif self.wins('O'):
            print('O wins')
        elif self.not_finished():
            print('NOT FINISHED YET!')
        else:
            print('DRAW>>> TIE>>> GO AGAIN!')

    def impossible(self):
        if self.wins('X') and self.wins('O') or \
                abs(self.cells.count('X') - self.cells.count('O')) >= 2:
            return True

    def not_finished(self):
        return self.cells.count('X') + self.cells.count('O') != 9

    def wins(self, side):
        grid = [list(self.cells[0:3]),
                list(self.cells[3:6]),
                list(self.cells[6:9])]
        return ([grid[0][x] for x in range(3)].count(side) == 3 or
                [grid[1][x] for x in range(3)].count(side) == 3 or
                [grid[2][x] for x in range(3)].count(side) == 3 or
                [grid[y][0] for y in range(3)].count(side) == 3 or
                [grid[y][1] for y in range(3)].count(side) == 3 or
                [grid[y][2] for y in range(3)].count(side) == 3 or
                [grid[x][x] for x in range(3)].count(side) == 3 or
                [grid[2 - x][x] for x in range(3)].count(side) == 3)

    def ask_for_coordinates(self):
        while True:
            try:
                xy = input('Enter the coordinates: ').split()
                x = xy[0]
                y = xy[1] if len(xy) > 1 else ''
                if x not in '123456789' or y not in '123456789':
                    print('You should enter numbers!')
                else:
                    x = int(x)
                    y = int(y)
                    if 1 <= x <= 3 and 1 <= y <= 3:
                        cells = list(self.cells)
                        if cells[(x - 1) + (3 - y) * 3] == '-':
                            cells[(x - 1) + (3 - y) * 3] = self.turn
                            self.cells = ''.join(cells)
                            return
                        else:
                            print('This cell is occupied!')
                    else:
                        print('You sould enter number from 1 to 3!')
            except ValueError:
                print('Enter a seprate two number from 1 to 3!')
            except IndexError:
                print('Enter a seprate two number from 1 to 3!')

    def game(self):
        for i in range(9):
            self.print_field()
            self.ask_for_coordinates()
            if self.wins(self.turn):
                break
            self.turn = 'O' if self.turn == 'X' else 'X'
        self.print_field()
        self.result()
        return


tictacto = Tictactoe()
tictacto.game()
