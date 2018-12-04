#!/bin/bash

source $SCRATCH/balena-firedrake-install/balena_firedrake_setup_environment.sh

source $SCRATCH/firedrake-complex/firedrake/bin/activate

cd /home/s/orp20/scratch/helmholtz-nearby-preconditioning/dev

mpirun -n 2 python simple.py