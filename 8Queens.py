import os, sys, time
import termcolor
os.system('color')


class Queens:
    def __init__(self, show_board=False, show_stats=0, return_on='All'):
        self.show_board = show_board
        self.show_stats = show_stats
        self.return_on  = return_on
        self.combination_list = [0, 0, 0, 0, 0, 0, 0, 0]
        self.coins_pos, self.final_combinations = [], []
        self.blocked_moves, self.moves_possible = [], []
        self.level_dict = {}
        os.system('cls')
        

    def Run(self):
        for i in range(1,9):
            self.level_dict[i] = []
        self.Populate(1)

    
    def result(self):
        if self.return_on == 'One':
            return self.final_combinations[0]
        elif self.return_on == 'All':
            return self.final_combinations
        else:
            print("Invalid option for return_on")


    def plot_coins(self):
        self.blocked_moves, self.moves_possible, self.coins_pos = [], [], []
        [[self.moves_possible.append((row, col)) for col in range(1, 9)] for row in range(1, 9)]
        for i in range(8):
            if self.combination_list[i] != 0:
                self.coins_pos.append((self.combination_list[i], i + 1))

        for queen_pos in self.coins_pos:
            for i in range(1, 9):
                self.blocked_moves.append((queen_pos[0], i))
                self.blocked_moves.append((i, queen_pos[1]))
                if queen_pos[0] - i > 0 and queen_pos[1] + i > 0:
                    self.blocked_moves.append((queen_pos[0] - i, queen_pos[1] - i))
                if queen_pos[0] + i < 9 and queen_pos[1] + i < 9:
                    self.blocked_moves.append((queen_pos[0] + i, queen_pos[1] + i))
                if queen_pos[0] - i > 0 and queen_pos[1] + i < 9:
                    self.blocked_moves.append((queen_pos[0] - i, queen_pos[1] + i))
                if queen_pos[0] + i < 9 and queen_pos[1] - i > 0:
                    self.blocked_moves.append((queen_pos[0] + i, queen_pos[1] - i))
            self.blocked_moves = list(dict.fromkeys(self.blocked_moves))
        [self.moves_possible.remove(move) for move in self.blocked_moves if move in self.moves_possible]

   
    def Populate(self, num):
        self.plot_coins()
        self.level_dict[num] = [move for move in self.moves_possible if move[1] == num]
        for _ in range(len(self.level_dict[num])):
            move1 = self.level_dict[num].pop(0)
            self.combination_list[num-1] = move1[0]
            self.update_board()
            if num < 8 :
                self.Populate(num+1)
            else:
                if 0 not in self.combination_list:
                    self.update_board()
                    temp_list = []
                    for val in self.combination_list:
                        temp_list.append(val-1)
                    self.final_combinations.append(temp_list)
            
            self.combination_list[num-1] = 0
       

    def update_board(self):
        self.plot_coins()
        if self.show_board or self.show_stats>=0:
            os.system("cls")

        if self.show_board:
            #print("\n" * 50)
            print("\n" * 2)
            print("   ", end="")
            [print(" " + str(i) + " ", end=' ') for i in range(1, 9)]
            print("\n    --------------------------------")
            for row in range(1, 9):
                print(" " + str(row) + " |", end='')
                for col in range(1, 9):
                    is_here = False
                    is_blocked = False
                    for coin in self.coins_pos:
                        if row == coin[0] and col == coin[1]:
                            is_here = True
                    for move in self.blocked_moves:
                        if row == move[0] and col == move[1]:
                            is_blocked = True
                    if is_here:
                        text = termcolor.colored(' Q ', 'red', attrs=['reverse', 'blink'])
                        print(text +"|", end='')
                    elif is_blocked:
                        text = termcolor.colored('   ', 'cyan', attrs=['reverse', 'blink'])
                        print(text + "|", end='')
                    else:
                        print("   |", end='')
                print("\n    --------------------------------")
            print("\n\n")

        if self.show_stats is 1 or self.show_stats is 2 :
            print("\nPossible Combinations :")
            print()
            [print("\n",i, end='') if n%5 == 0 and n != 0 else print(i, end='') for n,i in enumerate(self.final_combinations, 1)]

            if self.show_stats is 2 :
                print("\n\nCoin_position", self.coins_pos)
                print("level1: ", self.level_dict[1])
                print("level2: ", self.level_dict[2])
                print("level3: ", self.level_dict[3])
                print("level4: ", self.level_dict[4])
                print("level5: ", self.level_dict[5])
                print("level6: ", self.level_dict[6])
                print("level7: ", self.level_dict[7])
                print("level8: ", self.level_dict[8])
                print("\n\nMoves Possible:")
                print(" ", end="")
                [print("\n", move, end="") if n != 0 and move[0] != self.moves_possible[n - 1][0] else print(move, end="")
                for n, move in enumerate(self.moves_possible)]
                print()
               


if __name__ == "__main__":

    #   show_board --> shows the board animate as coins are positioned
    #   Show_stats --> 0: shows no stats
    #                  1 : shows Basic stats
    #                  2 : shows Detailes stats
    #   return_on --> All: shows all 92 combinations
    #                 One: shows first combination and ends program there.
   
    Queen1 = Queens(show_board=True, show_stats=0, return_on='All')
    Queen1.Run()
    print(Queen1.result())
    

