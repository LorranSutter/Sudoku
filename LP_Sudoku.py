from gurobipy import *
from math import sqrt
from sudoku import *
import time
import sys

def resolve(m, dim, arr = []):
    id_current_constr = 1
    m.params.Heuristics = 0
    dim_2 = int(sqrt(dim))

    # ----- Create problem variables -----
    x = [ [ [ [] for k in range(dim) ] for j in range(dim) ] for i in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == 0:
                for k in range(dim):
                    x[i][j][k] = m.addVar(vtype=GRB.BINARY, name="x_" + str(i+1) + "," + str(j+1) + "," + str(k+1)) # Possibilidades

    # ----- Update model with new variables -----
    m.update()

    # ----- Objective function -----
    m.setObjective(0, GRB.MINIMIZE)

    # ----- Constraint - every table position must be filled with only one value -----
    for i in range(dim):
        for j in range(dim):
            if arr[i][j] == 0:
                m.addConstr( sum( x[i][j][:dim] ), GRB.EQUAL, 1, "R_pos"+str(id_current_constr) )
                id_current_constr += 1

    R = []

    # ----- Constraint - must have only one element by column -----
    for j in range(dim):
        for k in range(dim):
            if k+1 not in [line[j] for line in arr]:
                for i in range(dim):
                    if arr[i][j] == 0:
                        R.append(x[i][j][k])
                #m.addConstr( sum( [x[i][j][k] for i in range(dim)] ), GRB.EQUAL, 1, "R_col"+str(id_current_constr) )
                if R != []:
                    m.addConstr( sum(R), GRB.EQUAL, 1, "R_col"+str(id_current_constr) )
                    id_current_constr += 1
                    R = []

    # ----- Constraint - must have only one element by row -----
    for i in range(dim):
        for k in range(dim):
            if k+1 not in arr[i][:]:
                for j in range(dim):
                    if arr[i][j] == 0:
                        R.append(x[i][j][k])
                #m.addConstr( sum( [x[i][j][k] for j in range(dim)] ), GRB.EQUAL, 1, "R_row"+str(id_current_constr) )
                if R != []:
                    m.addConstr( sum(R), GRB.EQUAL, 1, "R_row"+str(id_current_constr) )
                    id_current_constr += 1
                    R = []

    # ----- Constraint - must have only one element in each ubsquare -----
    for a in range(dim_2):
        for b in range(dim_2):
            for k in range(dim):
                if not in_subsquare(k+1,arr,dim_2,a,b):
                    for i in range(dim_2):
                        for j in range(dim_2):
                            if arr[i + dim_2*a][j + dim_2*b] == 0:
                                R.append(x[i + dim_2*a][j + dim_2*b][k])
                    if R != []:
                        m.addConstr( sum(R), GRB.EQUAL, 1, "R_sub"+str(id_current_constr) )
                        id_current_constr += 1
                        R = []

    m.update()

    # with open("Output/constrs", "w") as f:
    #     for k in m.getConstrs():
    #         f.write(str(k.ConstrName) + " " + str(m.getRow(k)))
    #         f.write('\n')

    m.optimize()

    return x


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Incorret input params")
        print("Correct input:")
        print("                 <none input>")
        print("OR")
        print("                 Input/file.txt")
        sys.exit(0)

    if len(sys.argv) == 2:
        try:
            dim, arr = read_file_sudoku(sys.argv[1])
            if already_solved(arr,dim):
                print("\n Sudoku already solved \n")
                sys.exit(0)
        except Exception as e:
            print('\nERROR ' + e + '\n')
    else:
        try:
            dim = input("\nInput Sudoku dimension: ")
            dim_2 = int(sqrt(dim))
            arr = [[0 for i in range(dim)] for j in range(dim)]
        except Exception as e:
            print('\nERROR ' + e + '\n')

    # ----- Inicializa modelo -----
    m = Model("Sudoku")

    print("\n------------------ Optimization Started ------------------\n")

    try:
        t = time.time()
        x = resolve(m, dim, arr)
        t = time.time() - t
    except Exception as e:
        print('\nERROR ' + e + '\n')

    print("------------------- Optimization Finished -------------------\n")

    if m.Status == GRB.OPTIMAL:
        print("\n------------------- Results -------------------")
        print("Execution time: " + str(t))
        print("--------------------------------------------------\n")

        try:
            m.write("Output/Output_" + str(dim) + "x" + str(dim) + ".sol")
            m.write("Output/Output_" + str(dim) + "x" + str(dim) + ".lp")
            m.write("Output/Output_" + str(dim) + "x" + str(dim) + ".mps")
            print("File written " + "Output_" + str(dim) + "x" + str(dim) + ".sol\n")
            print("File written " + "Output_" + str(dim) + "x" + str(dim) + ".sol\n")
            print("File written " + "Output_" + str(dim) + "x" + str(dim) + ".sol\n")
        except Exception as e:
            print('\nERROR ' + e + '\n')

        grid = [[arr[w][k] for k in range(dim)] for w in range(dim)]

        print("Original Sudoku:\n")
        print_grid(grid,dim)
        print('\n')

        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    if type(x[i][j][k]) == gurobipy.Var:
                        if x[i][j][k].x == 1:
                            grid[i][j] = k+1

        print("Solution:\n")
        print_grid(grid,dim)

        write_sudoku(grid,dim,"Output/sudoku_" + str(dim) + "x" + str(dim) + ".sol")
        print("\nFile written " + "sudoku_" + str(dim) + "x" + str(dim) + ".sol\n")

    elif m.Status == GRB.INFEASIBLE:
        print("\nSudoku Infeasible\n")
