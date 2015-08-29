from json import loads as _json_loads
from json import load  as _json_load

SUDOKU_SIZE = (9, 9)
CELL_SIZE = (3, 3)

class Sudoku(object):

    def __init__(self, mat):
        self._mat = mat

        for row in mat:
            if not isinstance(row, list):
                raise ValueError("row should be list.")
            for col in row:
                if not isinstance(col, int) or (col <= 0 and col >= 10):
                    raise ValueError("Illegal Value: {}".format(col))

    @property
    def mat(self):
        return self._mat

    @staticmethod
    def loads(text):
        matrixes = _json_loads(text)
        print(matrixes)
        print([Sudoku(mat)._mat for mat in matrixes])
        return [Sudoku(mat) for mat in matrixes]

    def __eq__(self, other):
        return self.mat == other.mat

class SudokuPageInfo(object):
    def __init__(self, sudoku, header, footer, show_page_number=False):
        self._sudoku = sudoku
        self._header = header
        self._footer = footer
        self._show_page_number = show_page_number

    @property
    def sudoku(self):
        return self._sudoku

    @property
    def header(self):
        return self._header

    @property
    def footer(self):
        return self._footer

    @property
    def show_page_number(self):
        return self._show_page_number
