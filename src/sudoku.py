from json import loads as _json_loads
from json import load  as _json_load
from reportlab.pdfgen import canvas
import os.path

UNKNOWN = '.'
SUDOKU_SIZE = (9, 9)
CELL_SIZE = (3, 3)
SUDOKU_FONT_SIZE = 30
SUDOKU_PDF_OFFSET = (110, 200)
SUDOKU_XPAD, SUDOKU_YPAD = (5, 5)
DIFFERENCE_FOR_NUMBERS = ((SUDOKU_FONT_SIZE + SUDOKU_XPAD)//2,
                          (SUDOKU_FONT_SIZE + SUDOKU_YPAD)//2)

class Sudoku(object):

    def __init__(self, mat):
        self._mat = mat

        for row in mat:
            if not isinstance(row, list):
                raise ValueError("row should be list.")
            for col in row:
                if (not isinstance(col, int) or (col <= 0 or col >= 10)) and \
                        col != UNKNOWN:
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

    def __init__(self, sudoku, title,
            show_page_number=False, page_number=None):
        self._sudoku = sudoku
        self._title = title
        self._show_page_number = show_page_number
        self._page_number = page_number

    @property
    def sudoku(self):
        return self._sudoku

    @property
    def title(self):
        return self._title

    @property
    def show_page_number(self):
        return self._show_page_number

    @property
    def page_number(self):
        return self._page_number

    def write_pdf(self, canvas):
        canvas.setFont("Helvetica", 70)
        canvas.drawString(70, 70, self.title)

        canvas.setFont("Helvetica", SUDOKU_FONT_SIZE)
        sudoku_offset = SUDOKU_PDF_OFFSET
        xlist = [sudoku_offset[0] + j*(2*SUDOKU_XPAD + SUDOKU_FONT_SIZE) for j in range(0, 9 + 1)]
        ylist = [sudoku_offset[1] + j*(2*SUDOKU_YPAD + SUDOKU_FONT_SIZE) for j in range(0, 9 + 1)]
        canvas.grid(xlist, ylist)
        for x in range(0, 9):
            for y in range(0, 9):
                if self.sudoku.mat[y][x] != UNKNOWN:
                    canvas.drawString(
                        sudoku_offset[0] + (SUDOKU_FONT_SIZE + SUDOKU_XPAD)//2
                            + x*(2*SUDOKU_XPAD + SUDOKU_FONT_SIZE) - 4,
                        sudoku_offset[1] + SUDOKU_FONT_SIZE
                            + y*(2*SUDOKU_YPAD + SUDOKU_FONT_SIZE),
                        str(self.sudoku.mat[y][x])
                        )

        if self.show_page_number:
            canvas.setFont("Helvetica", 10)
            canvas.drawString(280, 800, str(self.page_number))

        # draw a cell
        canvas.setLineWidth(3)
        canvas.grid(xlist[::3], ylist[::3])

def main():
    import sys
    filenames = sys.argv[1:]
    c = canvas.Canvas(os.path.splitext(filenames[0])[0] + '.pdf', bottomup=False)

    if len(filenames) == 1: # case: only problem files
        json_filename = filenames[0]
        with open(json_filename) as f:
            sudokus = Sudoku.load(f)

        page_infos = []
        for j, sudoku in enumerate(sudokus):
            page_infos.append(SudokuPageInfo(sudoku, 'Problem {}'.format(j+1),
            show_page_number=True, page_number= j + 1))

    elif len(filenames) == 2:
        prob_filename, ques_filename = filenames
        with open(prob_filename) as f:
            prob_sudokus = Sudoku.load(f)
        with open(ques_filename) as f:
            ques_sudokus = Sudoku.load(f)

        page_infos = []
        page_number = 1
        for j, sudoku in enumerate(prob_sudokus):
            page_infos.append(
                SudokuPageInfo(sudoku, 'Problem {}'.format(j + 1),
                show_page_number=True, page_number=page_number))
            page_number += 1
        for j, sudoku in enumerate(ques_sudokus):
            page_infos.append(
                SudokuPageInfo(sudoku, 'Answer {}'.format(j + 1),
                show_page_number=True, page_number=page_number))
            page_number += 1

    for i, page_info in enumerate(page_infos):
        page_info.write_pdf(c)
        if i != len(page_infos) - 1:
            c.showPage()

    c.save()

if __name__ == '__main__':
    main()
