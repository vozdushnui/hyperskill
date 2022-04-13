class TicTacToe:
    """
    Class specified for playing Tic Tac Toe
    """

    def __init__(self):
        self.step = 0
        self.ground_situation = '         '
        self.usr_step = ''
        self.usr_choice_index = 0
        self.count_x_row = 0
        self.count_o_row = 0
        self.count_null_row = 0
        self.x_3_row = 0
        self.o_3_row = 0
        self.usr_sign = 'X'

    def state_machine(self):
        if self.step == 0:
            self.usr_step = self.ask_usr_step()
            self.step = 1
        elif self.step == 1:
            if self.usr_input_checker(self.usr_step):
                self.step = 0
            else:
                self.step = 2
        elif self.step == 2:
            self.usr_choice_index = self.count_choice_index(self.usr_step)
            if self.nonempty_cell_checker(self.ground_situation, self.usr_choice_index):
                self.step = 0
            else:
                self.step = 3
        elif self.step == 3:
            self.put_user_choice(self.ground_situation, self.usr_choice_index)
            if self.game_stopper():
                exit()
            self.change_usr_sign()
            self.step = 0

    @staticmethod
    def ask_usr_step():
        return input('Enter the coordinates: ').split()

    @staticmethod
    def usr_input_checker(usr_steps):
        if ''.join(usr_steps).isnumeric():
            for item in usr_steps:
                if int(item) < 1 or int(item) > 3:
                    print('Coordinates should be from 1 to 3!')
                    return True
            else:
                return False
        else:
            print('You should enter numbers!')
            return True

    @staticmethod
    def count_choice_index(usr_steps):
        return (int(usr_steps[0]) - 1) * 3 + (int(usr_steps[1]) - 1)

    @staticmethod
    def nonempty_cell_checker(row, index):
        if row[index] == ' ':
            return False
        else:
            print('This cell is occupied!')
            return True

    def change_usr_sign(self):
        if self.usr_sign == 'X':
            self.usr_sign = 'O'
        else:
            self.usr_sign = 'X'

    def put_user_choice(self, row, index):
        x = list(row)
        x[index] = self.usr_sign
        self.ground_situation = ''.join(x)
        print(self.ground_situation_view())

    def game_stopper(self):
        win_combination = [self.ground_situation[:3], self.ground_situation[3:6], self.ground_situation[6:9],
                           self.ground_situation[0::3], self.ground_situation[1::3], self.ground_situation[2::3],
                           self.ground_situation[0::4], self.ground_situation[2:-2:2]]
        for row in win_combination:
            if row == 'XXX':
                print('X wins')
                return True
            elif row == 'OOO':
                print('O wins')
                return True
        else:
            if ' ' in list(self.ground_situation):
                return False
            else:
                print('Draw')
                return True

    def ground_situation_view(self):
        return f"---------\n" \
               f"| {self.ground_situation[0]} {self.ground_situation[1]} {self.ground_situation[2]} |\n" \
               f"| {self.ground_situation[3]} {self.ground_situation[4]} {self.ground_situation[5]} |\n" \
               f"| {self.ground_situation[6]} {self.ground_situation[7]} {self.ground_situation[8]} |\n" \
               f"---------"


play_1 = TicTacToe()
print(play_1.ground_situation_view())

while True:
    play_1.state_machine()
