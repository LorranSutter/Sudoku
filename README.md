# Sudoku

<p align="center">
  Project created to solve sudoku game for any square dimension (9x9, 16x16, 25x25 ...) employing linear problem concepts.
</p>

<p align="center">
  <a href="#runner-how-to-run">How to run</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#pencil-dependencies">Dependencies</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#game_die-what-is-sudoku">What is sudoku?</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#pencil2-what-is-linear-programming">What is linear programming?</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#triangular_ruler-sudoku-model">Sudoku model</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#cookie-credits">Credits</a>
</p>

## :runner: How to run

```sh
python3 LP_Sudoku.py sudoku_9x9.txt
```

Input example

```
9
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
```

Output example

```
3  1  6  | 5  7  8  | 4  9  2
5  2  9  | 1  3  4  | 7  6  8
4  8  7  | 6  2  9  | 5  3  1
-------------------------------
2  6  3  | 4  1  5  | 9  8  7
9  7  4  | 8  6  3  | 1  2  5
8  5  1  | 7  9  2  | 6  4  3
-------------------------------
1  3  8  | 9  4  7  | 2  5  6
6  9  2  | 3  5  1  | 8  7  4
7  4  5  | 2  8  6  | 3  1  9
```

## :pencil: Dependencies

gurobipy library must be installed.

Installation instructions in [Gurobi](https://www.gurobi.com/documentation/9.0/quickstart_mac/py_python_interface.html).

---

## :game_die: What is sudoku?

Sudoku is a logic puzzle game with the objective to fill a 9x9 grid with digits from 1 to 9. It respects a set of rules to fill this grid:

- Each row must have all digits from 1 to 9
- Each column must have all digits from 1 to 9
- Each of the nine 3x3 subgrid must have all digits from 1 to 9

<div align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg" alt="Sudoku unsolved" width="300"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Sudoku_Puzzle_by_L2G-20050714_solution_standardized_layout.svg" alt="Sudoku solved" width="300"/>
</div>

## :pencil2: What is linear programming?

Linear programming is a technique used to solve optimization problems where the elements have a linear relationship.

Linear programs aims to maximize a **objective function** made of **decision variables** subject to **constraints** which ensures that all the elements have a linear relationship and all variables are non-negative.

## :triangular_ruler: Sudoku model

In this case we just want to find a combination of variables that solves the puzzle. Therefore there will be no objetive function do be maximized, only linear constraints as follows:

<div align="center">

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{i=1}^nx_{ijk}=1\quad%20for\quad%20j,k\in[1,n])

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{j=1}^nx_{ijk}=1\quad%20for\quad%20i,k\in[1,n])

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{k=1}^nx_{ijk}=1\quad%20for\quad%20i,j\in[1,n])

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{j=3p-2}^{3p}\sum_{i=3q-2}^{3q}x_{ijk}=1\quad%20for\quad%20k\in[1,n]\\:and\\:p,q\in[1,\sqrt%20n])

<!-- i+p and j+q does not work -->
<!-- ![formula](https://render.githubusercontent.com/render/math?math=$\sum_{j=1}^{\sqrt%20n}\sum_{i=1}^{\sqrt%20n}x_{i+pj+qk}=1\quad%20for\quad%20k\in[1,n]\\:and\\:p,q\in[1,\sqrt%20n]) -->
</div>

We want to generalize the problem to solve a sudoku of any square dimension (9x9, 16x16, 25x25 ...). For that purpose, **n** represents the dimension of the puzzle, **x** are decision variables, **i** represents the columns, **j** represents the rows, **k** represents all possible digitis depending on the puzzle dimension, and **p** and **q** represents an auxiliar variable to iterate in all subgrids.

The first and the second constraints ensures that all columns and all rows will be filled must have only one of the available digits. The third constraint ensures that each cell in the grid will have only one digit. The last constraint ensures that all subgrid will have only one of the available digits.

---

## :cookie: Credits

Thanks to [Harshit Sidhwa](https://github.com/harshitsidhwa?tab=repositories) in providing back tracking [code](https://repl.it/@rui1337/backtrack-sudoku-solver) as an inspiration to solve this problem.
