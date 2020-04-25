# Sudoku

Project created to solve sudoku game for any square dimension (3x3, 4x4, 5x5 ...) employing linear problem concepts.

## Usage Example

```sh
python3 LP_Sudoku.py sudoku_9x9.txt
```

## Dependencies

gurobipy library must be installed.

Installation instructions in [Gurobi](http://www.gurobi.com/).

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{i=1}^nx_{ijk}=1\quad%20for\quad%20j,k\in[1,n])

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{j=1}^nx_{ijk}=1\quad%20for\quad%20i,k\in[1,n])

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{k=1}^nx_{ijk}=1\quad%20for\quad%20i,j\in[1,n])

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{j=3p-2}^{3p}\sum_{i=3q-2}^{3q}x_{ijk}=1\quad%20for\quad%20k\in[1,n]\\:and\\:p,q\in[1,\sqrt%20n])

![formula](https://render.githubusercontent.com/render/math?math=$\sum_{j=1}^{\sqrt%20n}\sum_{i=1}^{\sqrt%20n}x_{i+pj+qk}=1\quad%20for\quad%20k\in[1,n]\\:and\\:p,q\in[1,\sqrt%20n])
