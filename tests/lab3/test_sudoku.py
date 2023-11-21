import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab3.sudoku import group, get_row, get_col, get_block, check_solution, find_empty_positions, find_possible_values

class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_row(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_row(grid, (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row(grid, (1, 0)), ['4', '5', '6'])
        self.assertEqual(get_row(grid, (2, 0)), ['7', '8', '9'])

    def test_get_col(self):
        grid = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        self.assertEqual(get_col(grid, (0, 0)), ['1', '4', '7'])
        self.assertEqual(get_col(grid, (0, 1)), ['2', '5', '8'])
        self.assertEqual(get_col(grid, (0, 2)), ['.', '6', '9'])

    def test_get_block(self):
        grid = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])

    def test_valid_solution(self):
        valid_solution = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9']
        ]
        self.assertTrue(check_solution(valid_solution))

    def test_invalid_solution(self):
        invalid_solution = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '7']
        ]
        self.assertFalse(check_solution(invalid_solution))


    def test_find_empty_positions(self):
        grid2 = ([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
        assert find_empty_positions(grid2) == (0, 2)

        grid3 = ([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
        assert find_empty_positions(grid3) == (1, 1)

        grid4 = ([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
        assert find_empty_positions(grid4) == (2, 0)

    def test_find_possible_values(self):
        grid = [['5', '3', ' ', ' ', '7', ' ', ' ', ' ', ' '],
                ['6', ' ', ' ', '1', '9', '5', ' ', ' ', ' '],
                [' ', '9', '8', ' ', ' ', ' ', ' ', '6', ' '],
                ['8', ' ', ' ', ' ', '6', ' ', ' ', ' ', '3'],
                ['4', ' ', ' ', '8', ' ', '3', ' ', ' ', '1'],
                ['7', ' ', ' ', ' ', '2', ' ', ' ', ' ', '6'],
                [' ', '6', ' ', ' ', ' ', ' ', '2', '8', ' '],
                [' ', ' ', ' ', '4', '1', '9', ' ', ' ', '5'],
                [' ', ' ', ' ', ' ', '8', ' ', ' ', '7', '9']]

        values = find_possible_values(grid, (0, 2))
        self.assertEqual(values, {'1', '2', '4'})

        values = find_possible_values(grid, (4, 7))
        self.assertEqual(values, {'2', '5', '9'})



if __name__ == '__main__':
    unittest.main()