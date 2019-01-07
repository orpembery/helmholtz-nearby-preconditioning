#!/bin/bash

#source $SCRATCH/balena-firedrake-install/balena_firedrake_setup_environment.sh

#source $SCRATCH/firedrake-complex/firedrake/bin/activate

#cd /home/s/orp20/scratch/helmholtz-nearby-preconditioning/dev

for num_procs in 1 2 4 8 16
do
    echo $num_procs
    for system_size in 10 20 40 80
    do
	time mpirun -n num_procs python simple.py system_size
    done
done