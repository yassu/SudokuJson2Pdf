from json import loads as _json_loads
from json import load  as _json_load
from reportlab.pdfgen import canvas

SUDOKU_SIZE = (9, 9)
CELL_SIZE = (3, 3)
FONT_SIZE = 30
SUDOKU_PDF_OFFSET = (50, 50)
SUDOKU_XPAD, SUDOKU_YPAD = (5, 5)
DIFFERENCE_FOR_NUMBERS = ((FONT_SIZE + SUDOKU_XPAD)//2,
                          (FONT_SIZE + SUDOKU_YPAD)//2)

class Sudoku(object):

    def __init__(self, mat):
        self._mat = mat

        for row in mat:
            if not isinstance(row, list):
                raise ValueError("row should be list.")
            for col in row:
                if not isinstance(col, int) or (col <= 0 or col >= 10):
                    raise ValueError("Illegal Value: {}".format(col))

    @property
    def mat(self):
        return self._mat

    @staticmethod
    def loads(text):
        matrixes = _json_loads(text)
        return [Sudoku(mat) for mat in matrixes]

    @staticmethod
    def load(f):
        return Sudoku.loads(f.read())

    def __eq__(self, other):
        return self.mat == other.mat

class SudokuPageInfo(object):

    def __init__(self, sudoku, header, footer,
            show_page_number=False, page_num=None):
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

    def write_pdf(self, canvas):
        xlist = [j*(2*XPAD + FONT_SIZE) for j in range(0, 9 + 1)]
        ylist = [j*(2*YPAD + FONT_SIZE) for j in range(0, 9 + 1)]
        canvas.grid(xlist, ylist)
        for x in range(0, 9):
            for y in range(0, 9):
                canvas.drawString(
                    (FONT_SIZE + XPAD)//2 + x*(2*SUDOKU_XPAD + FONT_SIZE) - 4,
                    FONT_SIZE + y*(2*SUDOKU_YPAD + FONT_SIZE),
                    str(self.sudoku.mat[x][y])
                    )

if __name__ == '__main__':
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
    sudoku_info = SudokuPageInfo(sudoku, 'header', 'footer',
        show_page_number=True, page_num=3)

    c = canvas.Canvas("sample.pdf", bottomup=False)
    XPAD, YPAD = (5, 5)
    c.setFont("Helvetica", FONT_SIZE)
    sudoku_info.write_pdf(c)
    c.save()
