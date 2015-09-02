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

For example, to become `Hoge {number}`,

::

    $ sudoku2pdf.py --answer-name Hoge problem-filename

License
=========

Apache License 2.0
