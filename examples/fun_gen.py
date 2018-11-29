from firedrake import UnitSquareMesh, FunctionSpace, Function
from helmholtz_firedrake import utils

def fun_gen(ii,k):
    
    if ii==0:
    
        num_cells = utils.h_to_mesh_points(k**-1.5)

    elif ii==1:
        
        num_cells = utils.h_to_mesh_points(k**-2.0)
        
    
    elif ii==2:

        num_cells = utils.h_to_mesh_points(0.25*k**-2.0)

    mesh = UnitSquareMesh(num_cells,num_cells)

    V = FunctionSpace(mesh,"CG",1)

    u = Function(V)

    
    return u

