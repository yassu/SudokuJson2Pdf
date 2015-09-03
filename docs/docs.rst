============
SudokuJson2Pdf
============

This project provides a tool which convert json file of sudoku information to pdf.

How to Install
================

::

  $ python setup.py install

Usage
=======

::

  $ sudoku2pdf.py [option] problem-filename [answer-filename]

For example, if you want to output out.pdf from in.json with hidden title, you can obtain by
  following code:

::

  $ sudoku2pdf.py --hidden-title in.json -o out.pdf

Options
=========

OutPut Filename
-----------------

In default, output pdf filename is {inputfilename}.pdf.

To specify output filename, you can use `-o`, or `--output`

Hidden Page Numbers
--------------------

In default, output pdf has page numbers.

To obtain pdf which has no page number, you can use `--hidden-page-number` option:

::

  $ sudoku2pdf.py --hidden-page-number problem-filename

Hidden Title
--------------

In default, page of output pdf has titles.

To obtain page of output pdf which has no titles, you can use `--hidden-title` option:

::

  $ sudoku2pdf.py --hidden-title problem-filename

Title of Problem Page
-----------------------

In default, title of problem page is "Problem {number}".

To become "`problem_name` {number}", you can use `--problem-name` option.

For example, to become "Question {number}",

::

    $ sudoku2pdf.py --problem-name Question problem-filename

Title of Question Page
------------------------

In default, title of answer page is "Answer {number}".

To become `answer_name` {number}, you can use `--answer-name` option.

For example,

::

  $ cat examples/question1.json
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

  $ cat examples/answer1.json
  [
    [
        [1, ".", 7, 4, 9, 3, 6, 5, 2],
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
        [8, ".", 6, 9, 2, 7, 5, 1, 3],
        [3, 5, 2, 8, 4, 1, 9, 7, 6],
        [7, 1, 9, 6, 3, 5, 4, 2, 8],

        [1, 7, 4, 5, 6, 9, 3, 8, 2],
        [6, 8, 3, 2, 1, 4, 7, 9, 5],
        [2, 9, 5, 3, 7, 8, 1, 6, 4],

        [4, 2, 7, 1, 8, 3, 6, 5, 9],
        [5, 6, 1, 4, 9, 2, 8, 3, 7],
        [9, 3, 8, 7, 5, 6, 2, 4, "."]
    ]
  ]

  $ sudoku2pdf.py examples/question1.json examples/answer1.json -o examples/out.pdf
  $ ls examples/out.pdf
    examples/out.pdf

License
=========

Apache License 2.0
