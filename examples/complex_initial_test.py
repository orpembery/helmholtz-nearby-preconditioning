from helmholtz_nearby_preconditioning import experiments
from k_to_index import k_to_index

# In complex

k_list = [10.0,12.0]

# Need to somehow square this with fun_gen, because otherwise we're specifying the h conditions in two different places

h_mult_power_list = [(1.0,-1.5),(1.0,-2.0)]

num_pieces = 2

noise_level_system_A = 0.1

noise_level_system_n = 0.1

noise_level_rhs_A = 0.1

num_system = 3

num_rhs = 4

fine_grid_mult_power = (0.25,-2.0)

seed = 3


#
experiments.test_fem_approx_props(k_list,h_mult_power_list,num_pieces,
                                     noise_level_system_A,noise_level_system_n,
                                     noise_level_rhs_A,num_system,num_rhs,
                                     fine_grid_mult_power,seed,k_to_index)
