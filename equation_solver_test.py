import numpy as np
from ortools.sat.python import cp_model


def three():
    """
    10a+4.5b+c+2.5d<=300
    2a+1.4b+.6c+.9d<=200
    8a+6.8b+4c+3d<=300
    Max. F=20a+16b+9c+7d
    """
    model=cp_model.CpModel()
    #variable
    a=model.NewIntVar(0, 30, 'a')
    b=model.NewIntVar(0, 30, 'b')
    c=model.NewIntVar(0, 100, 'c')
    d=model.NewIntVar(0, 100, 'd')
    var=[a,b,c,d]
    #constraint
    model.Add(a*100 +b*45 +c*10 +d *25 <=3000)
    model.Add(a*20+b*14+c*6+d*9<=2000)
    model.Add(a*80+b*68+c*40+d*30<=3000)
    model.Maximize(a*20 + b*16 + c* 9 +d*7)
    solver=cp_model.CpSolver()
    # sol_printer=VarArraySolutionPrinter(var)
    # status=solver.SearchForAllSolutions(model, sol_printer)
    # return sol_printer.all_sol
    status=solver.Solve(model)
    if status==cp_model.OPTIMAL:
        print('obj value = {}'.format(solver.ObjectiveValue()))
        print("""
              a={}
              b={}
              c={}
              d={}
              """.format(solver.Value(a),
              solver.Value(b), 
              solver.Value(c), 
              solver.Value(d), 
              ))


three()
