================
SudokuJson2Pdf
================

This project provides a tool which convert json file of sudoku information to pdf.

How to Install
================

::

  $ python setup.py install

Usage
=======

::

  $ sudoku2pdf.py [option] question-filename [answer-filename]

For example, if you want to output out.pdf from in.json with hidden title, you can obtain by
following code:

::

  $ sudoku2pdf.py --hidden-title in.json -o out.pdf

License
=========

Apache License 2.0
