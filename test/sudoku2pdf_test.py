from sys import path
path.append('sudoku_json2pdf')
from sudoku2pdf import Sudoku, SudokuPageInfo
from unittest import TestCase
from nose.tools import raises


class SudokuTestCase(TestCase):

    def loads_test1(self):
        assert(Sudoku.loads("""
        [
            [
                [1, 8, 7, 4, 9, 3, 6, 5, 2],
                [6, 4, 3, 1, 2, 5, 8, 9, 7],
                [2, 5, 9, 7, 8, 6, 3, 1, 4],

                [7, 1, 4, 2, 3, 8, 5, 6, 9],
                [9, 6, 8, 5, 7, 1, 4, 2, 3],
                [5, 3, 2, 6, 4, 9, 1, 7, 8],

                [8, 7, 6, 9, 1, 4, 2, 3, 5],
                [4, 9, 1, 3, 5, 2, 7, 8, 6],
                [3, 2, 5, 8, 6, 7, 9, 4, 1]
            ]
        ]
        """) == [Sudoku([
            [1, 8, 7, 4, 9, 3, 6, 5, 2],
            [6, 4, 3, 1, 2, 5, 8, 9, 7],
            [2, 5, 9, 7, 8, 6, 3, 1, 4],

            [7, 1, 4, 2, 3, 8, 5, 6, 9],
            [9, 6, 8, 5, 7, 1, 4, 2, 3],
            [5, 3, 2, 6, 4, 9, 1, 7, 8],

            [8, 7, 6, 9, 1, 4, 2, 3, 5],
            [4, 9, 1, 3, 5, 2, 7, 8, 6],
            [3, 2, 5, 8, 6, 7, 9, 4, 1]
        ]
        )])

    def loads_test2(self):
        assert(Sudoku.loads("""
        [
            [
                [1, 8, 7, 4, 9, 3, 6, 5, 2],
                [6, 4, 3, 1, 2, 5, 8, 9, 7],
                [2, 5, 9, 7, 8, 6, 3, 1, 4],

                [7, 1, 4, 2, 3, 8, 5, 6, 9],
                [9, 6, 8, 5, 7, 1, 4, 2, 3],
                [5, 3, 2, 6, 4, 9, 1, 7, 8],

                [8, 7, 6, 9, 1, 4, 2, 3, 5],
                [4, 9, 1, 3, 5, 2, 7, 8, 6],
                [3, 2, 5, 8, 6, 7, 9, 4, 1]
            ],
            [
                [8, 4, 6, 9, 2, 7, 5, 1, 3],
                [3, 5, 2, 8, 4, 1, 9, 7, 6],
                [7, 1, 9, 6, 3, 5, 4, 2, 8],

                [1, 7, 4, 5, 6, 9, 3, 8, 2],
                [6, 8, 3, 2, 1, 4, 7, 9, 5],
                [2, 9, 5, 3, 7, 8, 1, 6, 4],

                [4, 2, 7, 1, 8, 3, 6, 5, 9],
                [5, 6, 1, 4, 9, 2, 8, 3, 7],
                [9, 3, 8, 7, 5, 6, 2, 4, 1]
            ]
        ]
        """) == [
            Sudoku([
                [1, 8, 7, 4, 9, 3, 6, 5, 2],
                [6, 4, 3, 1, 2, 5, 8, 9, 7],
                [2, 5, 9, 7, 8, 6, 3, 1, 4],

                [7, 1, 4, 2, 3, 8, 5, 6, 9],
                [9, 6, 8, 5, 7, 1, 4, 2, 3],
                [5, 3, 2, 6, 4, 9, 1, 7, 8],

                [8, 7, 6, 9, 1, 4, 2, 3, 5],
                [4, 9, 1, 3, 5, 2, 7, 8, 6],
                [3, 2, 5, 8, 6, 7, 9, 4, 1]
            ]),
            Sudoku([
                [8, 4, 6, 9, 2, 7, 5, 1, 3],
                [3, 5, 2, 8, 4, 1, 9, 7, 6],
                [7, 1, 9, 6, 3, 5, 4, 2, 8],

                [1, 7, 4, 5, 6, 9, 3, 8, 2],
                [6, 8, 3, 2, 1, 4, 7, 9, 5],
                [2, 9, 5, 3, 7, 8, 1, 6, 4],

                [4, 2, 7, 1, 8, 3, 6, 5, 9],
                [5, 6, 1, 4, 9, 2, 8, 3, 7],
                [9, 3, 8, 7, 5, 6, 2, 4, 1]
            ])
        ])

    @raises(ValueError)
    def loads_test3(self):
        Sudoku.loads("""
        [
            [
                ["a", 8, 7, 4, 9, 3, 6, 5, 2],
                [6, 4, 3, 1, 2, 5, 8, 9, 7],
                [2, 5, 9, 7, 8, 6, 3, 1, 4],

                [7, 1, 4, 2, 3, 8, 5, 6, 9],
                [9, 6, 8, 5, 7, 1, 4, 2, 3],
                [5, 3, 2, 6, 4, 9, 1, 7, 8],

                [8, 7, 6, 9, 1, 4, 2, 3, 5],
                [4, 9, 1, 3, 5, 2, 7, 8, 6],
                [3, 2, 5, 8, 6, 7, 9, 4, 1]
            ]
        ]
        """)

    @raises(ValueError)
    def loads_test4(self):
        # only sudoku, not list of sudoku
        Sudoku.loads("""
            [
                [1, 8, 7, 4, 9, 3, 6, 5, 2],
                [6, 4, 3, 1, 2, 5, 8, 9, 7],
                [2, 5, 9, 7, 8, 6, 3, 1, 4],

                [7, 1, 4, 2, 3, 8, 5, 6, 9],
                [9, 6, 8, 5, 7, 1, 4, 2, 3],
                [5, 3, 2, 6, 4, 9, 1, 7, 8],

                [8, 7, 6, 9, 1, 4, 2, 3, 5],
                [4, 9, 1, 3, 5, 2, 7, 8, 6],
                [3, 2, 5, 8, 6, 7, 9, 4, 1]
            ]
        """)

    @raises(ValueError)
    def loads_test5(self):
        Sudoku.loads('"abc"')

    def mat_test(self):
        m = [
            [1, 8, 7, 4, 9, 3, 6, 5, 2],
            [6, 4, 3, 1, 2, 5, 8, 9, 7],
            [2, 5, 9, 7, 8, 6, 3, 1, 4],

            [7, 1, 4, 2, 3, 8, 5, 6, 9],
            [9, 6, 8, 5, 7, 1, 4, 2, 3],
            [5, 3, 2, 6, 4, 9, 1, 7, 8],

            [8, 7, 6, 9, 1, 4, 2, 3, 5],
            [4, 9, 1, 3, 5, 2, 7, 8, 6],
            [3, 2, 5, 8, 6, 7, 9, 4, 1]
        ]
        assert(Sudoku(m).mat == m)


class SudokuPageInfoTestCase(TestCase):

    def setUp(self):
        sudoku = Sudoku([
            [1, 8, 7, 4, 9, 3, 6, 5, 2],
            [6, 4, 3, 1, 2, 5, 8, 9, 7],
            [2, 5, 9, 7, 8, 6, 3, 1, 4],

            [7, 1, 4, 2, 3, 8, 5, 6, 9],
            [9, 6, 8, 5, 7, 1, 4, 2, 3],
            [5, 3, 2, 6, 4, 9, 1, 7, 8],

            [8, 7, 6, 9, 1, 4, 2, 3, 5],
            [4, 9, 1, 3, 5, 2, 7, 8, 6],
            [3, 2, 5, 8, 6, 7, 9, 4, 1]
        ])
        self.sudoku_info = SudokuPageInfo(
            sudoku, "title", show_title=False, show_page_number=True)

    def sudoku_test1(self):
        assert(self.sudoku_info.sudoku.mat == [
            [1, 8, 7, 4, 9, 3, 6, 5, 2],
            [6, 4, 3, 1, 2, 5, 8, 9, 7],
            [2, 5, 9, 7, 8, 6, 3, 1, 4],

            [7, 1, 4, 2, 3, 8, 5, 6, 9],
            [9, 6, 8, 5, 7, 1, 4, 2, 3],
            [5, 3, 2, 6, 4, 9, 1, 7, 8],

            [8, 7, 6, 9, 1, 4, 2, 3, 5],
            [4, 9, 1, 3, 5, 2, 7, 8, 6],
            [3, 2, 5, 8, 6, 7, 9, 4, 1]
        ])

    def show_title_test(self):
        assert(self.sudoku_info.show_title is False)

    def title_test(self):
        assert(self.sudoku_info.title == "title")

    def show_page_number_test(self):
        assert(self.sudoku_info.show_page_number is True)
