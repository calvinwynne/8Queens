import unittest
import queens

class TestQueens(unittest.TestCase):

    Q1 = queens.Queens(show_board=False, show_stats=1, return_on='All')

    def setup(self):
        self.Q1.combination_list = [0, 0, 0, 0, 0, 0, 0, 0]
        
    def test_plot_coins(self):
        test_list = []
        [[test_list.append((row, col)) for col in range(1,9)]for row in range(1,9)]
        self.Q1.plot_coins()
        self.assertEqual(self.Q1.moves_possible, test_list)
    
    def tearDown(self):
        self.Q1.combination_list = 0


    def setUp(self):
        self.show_board = True
        self.show_stats = True
        self.return_on  = 'All'
        self.Q1.combination_list = [1, 3, 0, 0, 0, 0, 0, 0]
        self.Q1.coins_pos = [(1, 1), (3, 2)]
        self.Q1.level_dict[1] = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
        self.Q1.level_dict[2] = [(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]
        self.Q1.level_dict[3] = []
        self.Q1.level_dict[4] = []
        self.Q1.level_dict[5] = []
        self.Q1.level_dict[6] = []
        self.Q1.level_dict[7] = []


    def test_update_board(self):
        self.Q1.update_board()

        test_list = [(2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
         (4, 5), (4, 6), (4, 7), (4, 8), (5, 3), (5, 6), (5, 7),
         (5, 8), (6, 3), (6, 4), (6, 7), (6, 8), (7, 3),
         (7, 4), (7, 5), (7, 8), (8, 3), (8, 4), (8, 5), (8, 6)]
        self.assertEqual(self.Q1.moves_possible, test_list)











if __name__=="__main__":
    unittest.main()