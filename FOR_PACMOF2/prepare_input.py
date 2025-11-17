import sys
import numpy as np
import pickle

sys.path.append('../ITP')
from atom import Atom, select_atoms, remove_atoms, mol2_to_atoms, count_atoms, shift_atoms, dump_atoms, count_atoms, shift_atoms
from read_utils import read_mol2_file
from write_utils import write_gro_file, write_mol2_file
from write_utils import write_atoms, write_bonds, write_angles, write_dihedrals, compose_itp_files
from pbc import calculate_lattice_vectors, select_in_box
from mof801_utils import remove_extra_oxygens, define_mof801_atom_types, define_mof801_atom_names, check_mof801_atom_names

# STEP 1. Read data
# Set lower bound in Mercury calculate packing = 0.0
a     = 17.8348
b     = 17.8348
c     = 17.8348
alpha = 90.00 / 180 * np.pi
beta  = 90.00 / 180 * np.pi
gamma = 90.00 / 180 * np.pi
bounds_a, bounds_b, bounds_c = [0.0, 2.5], [0.0, 2.5], [0.0, 2.5]
atoms = mol2_to_atoms(read_mol2_file('test.mol2'))

write_mol2_file(atoms, 'test123.mol2', a, b, c, alpha, beta, gamma)