import os, sys, time
import termcolor
combination_list = [0, 0, 0, 0, 0, 0, 0, 0]
coins_pos, blocked_moves, moves_possible = [], [], []
level1, level2, level3, level4, level5, level6, level7, level8 = [], [], [], [], [], [], [], []
final_combinations = []
move_dict = {}
show_movesPossible = True


def plot_coins():
    global coins_pos, blocked_moves, moves_possible
    coins_pos, blocked_moves, moves_possible = [], [], []
    [[moves_possible.append((row, col)) for col in range(1, 9)] for row in range(1, 9)]

    for i in range(8):
        if combination_list[i] != 0:
            coins_pos.append((combination_list[i], i + 1))

    for queen_pos in coins_pos:
        for i in range(1, 9):
            blocked_moves.append((queen_pos[0], i))
            blocked_moves.append((i, queen_pos[1]))
            if queen_pos[0] - i > 0 and queen_pos[1] + i > 0:
                blocked_moves.append((queen_pos[0] - i, queen_pos[1] - i))
            if queen_pos[0] + i < 9 and queen_pos[1] + i < 9:
                blocked_moves.append((queen_pos[0] + i, queen_pos[1] + i))
            if queen_pos[0] - i > 0 and queen_pos[1] + i < 9:
                blocked_moves.append((queen_pos[0] - i, queen_pos[1] + i))
            if queen_pos[0] + i < 9 and queen_pos[1] - i > 0:
                blocked_moves.append((queen_pos[0] + i, queen_pos[1] - i))
        blocked_moves = list(dict.fromkeys(blocked_moves))
    [moves_possible.remove(move) for move in blocked_moves if move in moves_possible]


def update_board():
    plot_coins()
    #time.sleep(1)
    os.system("cls")
    #print("\n" * 100)
    print("   ", end="")
    [print(" " + str(i) + " ", end=' ') for i in range(1, 9)]
    print("\n  ---------------------------------")
    for row in range(1, 9):
        print(str(row) + " |", end='')
        for col in range(1, 9):
            is_here = False
            is_blocked = False
            for coin in coins_pos:
                if row == coin[0] and col == coin[1]:
                    is_here = True
            for move in blocked_moves:
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
        print("\n  ---------------------------------")

    if show_movesPossible:
        print("\nCoin_position", coins_pos)
        print("\nlevel1: ", level1)
        print("level2: ", level2)
        print("level3: ", level3)
        print("level4: ", level4)
        print("level5: ", level5)
        print("level6: ", level6)
        print("level7: ", level7)
        print("level8: ", level8)
        print("\nPossible Combinations :")
        [print(i) if n%5 == 0 and n != 0 else print(i, end='') for n,i in enumerate(final_combinations)]
        print("\n\nMoves Possible:")
        print(" ", end="")
        [print("\n", move, end="") if n != 0 and move[0] != moves_possible[n - 1][0] else print(move, end="")
         for n, move in enumerate(moves_possible)]
        print()



def strategy():
    global combination_list, coins_pos, level1, level2, level3, level4, level5, level6, level7, level8, final_combinations
    num = 1
    level1 = [move for move in moves_possible if move[1] == 1]
    for i in range(len(level1)):
        move1 = level1.pop(0)
        combination_list[0] = move1[0]
        update_board()

        level2 = [move for move in moves_possible if move[1] == 2]
        for j in range(len(level2)):
            move2 = level2.pop(0)
            combination_list[1] = move2[0]
            update_board()

            level3 = [move for move in moves_possible if move[1] == 3]
            for k in range(len(level3)):
                move3 = level3.pop(0)
                combination_list[2] = move3[0]
                update_board()

                level4 = [move for move in moves_possible if move[1] == 4]
                for k in range(len(level4)):
                    move4 = level4.pop(0)
                    combination_list[3] = move4[0]
                    update_board()

                    level5 = [move for move in moves_possible if move[1] == 5]
                    for k in range(len(level5)):
                        move5 = level5.pop(0)
                        combination_list[4] = move5[0]
                        update_board()

                        level6 = [move for move in moves_possible if move[1] == 6]
                        for k in range(len(level6)):
                            move6 = level6.pop(0)
                            combination_list[5] = move6[0]
                            update_board()

                            level7 = [move for move in moves_possible if move[1] == 7]
                            for k in range(len(level7)):
                                move7 = level7.pop(0)
                                combination_list[6] = move7[0]
                                update_board()

                                level8 = [move for move in moves_possible if move[1] == 8]
                                for k in range(len(level8)):
                                    move8 = level8.pop(0)
                                    combination_list[7] = move8[0]


                                    if 0 not in combination_list:
                                        update_board()
                                        final_combinations.append(combination_list[:])
                                        

                                    update_board()

                                combination_list[7] = 0
                            combination_list[6] = 0
                        combination_list[5] = 0
                    combination_list[4] = 0
                combination_list[3] = 0
            combination_list[2] = 0
        combination_list[1] = 0





if __name__ == "__main__":
    show_movesPossible = True
    Manual_mode = False
    update_board()
    strategy()


    if Manual_mode:
        for i in range(100):
            plot_coins()
            update_board()
            print(coins_pos)
            n = 8
            combination_list = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
            print(combination_list)