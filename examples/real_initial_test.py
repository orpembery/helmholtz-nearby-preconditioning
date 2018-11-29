from helmholtz_nearby_preconditioning import experiments
from k_to_index import k_to_index

# In real

k_list = [10.0,12.0,14.0]

h_mult_power_list = [(1.0,-1.5)]

fine_grid_mult_power = (1.0,-2.0)

experiments.real_process_for_fem_approx_props(k_list,h_mult_power_list,fine_grid_mult_power,k_to_index)
