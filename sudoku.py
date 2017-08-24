from math import sqrt
from random import choice
from random import randint
import sys

def already_solved(arr, dim):
    """
      already_solved(arr, dim) -> bool

      Check if arr is already solved

      Params
      ----------
          num   -> number to be chacked
          arr   -> sudoku 2D list

      Return
      ----------
          bool -> if arr is already solved
    """
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == 0: return False
    return True

def in_subsquare(num, arr, dim_2, row, col):
    """
      in_subsquare(num, arr, dim_2, row, col) -> bool

      Check if num is in the subsquare which stars at row row and
      column col and has dimension dim_2

      Params
      ----------
          num   -> number to be chacked
          arr   -> sudoku 2D list
          dim_2 -> sudoku subsquare dimension
          row   -> row that subsquare starts
          col   -> col that subsquare starts

      Return
      ----------
          bool -> if num is in subsquare
    """
    for i in range(row*dim_2, row*dim_2 + dim_2):
        for j in range(col*dim_2, col*dim_2 + dim_2):
            if num == arr[i][j]: return True
    return False

def read_file_sudoku(file_sudoku):
    """
      read_file_sudoku(arr) -> int, [list, list]

      Read sudoku file

      Params
      ----------
          file_sudoku -> sudoku file
                         dim
                         pos11 pos12 ...
                         pos21 pos22 ...
                         ...   ...

      Return
      ----------
          dim -> sudoku dimension
          arr -> sudoku 2D list
    """
    with open(file_sudoku,'r') as f:
        dim = int(f.readline())
        arr = [[] for k in range(dim)]
        for k in range(dim):
            arr[k] = list(map(int,f.readline().split()))
    return dim, arr

def print_grid(arr, dim):
    """
      print_grid(arr, dim)

      Print a good view sudoku

      Params
      ----------
          arr -> sudoku 2D list
          dim -> sudoku dimension
    """
    l = ""
    dim_2 = int(sqrt(dim))
    for i in range(dim):
		for j in range(dim):
			l = l + str(arr[i][j]) + " "
			if arr[i][j] < 10: l = l + " "
			if (j+1)%dim_2 == 0 and j != dim-1: l = l + "| "
		print(l)
		if (i+1)%dim_2 == 0 and i != dim-1: print("-" * len(l))
		l = ""

def num_blank_spaces(arr):
    return sum([k.count(0) for k in arr])

def num_not_blank_spaces(arr,dim):
    return dim*dim - num_blank_spaces(arr)

def remove_sudoku_nums(arr, dim, num):
    """
      remove_sudoku_nums(arr, dim, num)

      Remove randomly num numbers from sudoku arr

      Params
      ----------
          arr -> sudoku 2D list
          dim -> sudoku dimension
          num -> number of blank spaces
    """
    if num_not_blank_spaces(arr,dim) < num:
        print("Sudoku has less avaliable spaces than blank spaces wished\n")
        sys.exit(0)
    while num > 0:
        i, j = randint(1,dim)-1, randint(1,dim)-1
        if arr[i][j] != 0:
            arr[i][j] = 0
            num -= 1

def write_sudoku(arr, dim, out):
    """
      write_sudoku(arr,dim,out)

      Write sudoku output file

      Params
      ----------
          arr -> sudoku 2D list
          dim -> sudoku dimension
          out -> output file name
    """
    l = ""
    with open(out,'w') as f:
        f.write(str(dim))
        f.write('\n')
        for i in range(dim):
            for j in range(dim):
                l = l + str(arr[i][j]) + " "
            f.write(l)
            f.write('\n')
            l = ""
