import numpy as np
import pickle

from atom import Atom

# Calculate crystal lattice vectors
def calculate_lattice_vectors(a, b, c,
                              alpha, beta, gamma):
    alpha_rev = np.arccos((np.cos(beta) * np.cos(gamma) - np.cos(alpha)) / np.sin(beta) / np.sin(gamma))

    transformation = np.array([\
        [a,     b*np.cos(gamma),   c*np.cos(beta)                       ], \
        [0.0,   b*np.sin(gamma),   -1.0*c*np.sin(beta)*np.cos(alpha_rev)], \
        [0.0,   0.0,               c*np.sin(beta)*np.sin(alpha_rev)     ]
        ])

    vec_a = transformation.dot(np.transpose([1.0, 0.0, 0.0]))
    vec_b = transformation.dot(np.transpose([0.0, 1.0, 0.0]))
    vec_c = transformation.dot(np.transpose([0.0, 0.0, 1.0]))
    
    # print(f'VECTOR A = {vec_a}')
    # print(f'VECTOR B = {vec_b}')
    # print(f'VECTOR C = {vec_c}')
    return vec_a, vec_b, vec_c

def compare_periodic(r1, r2, p_a, p_b, p_c):
    delta = r1 - r2 + np.array([p_a, p_b, p_c])
    tol = 1e-3

    delta[0] = delta[0] % p_a
    delta[1] = delta[1] % p_b
    delta[2] = delta[2] % p_c
    
    delta[0] = min(delta[0], p_a - delta[0])
    delta[1] = min(delta[1], p_b - delta[1])
    delta[2] = min(delta[2], p_c - delta[2])
    return abs(delta[0]) < tol and abs(delta[1]) < tol and abs(delta[2]) < tol

def apply_pbc(atoms,
              a, b, c,
              alpha, beta, gamma,
              bounds_a, bounds_b, bounds_c):
    '''
    # to create unique.npy and adjacency_data.pickle decomment code below

    tol_internal = 1e-3
    unique = np.empty(len(atoms))
    # define what atoms are unique and what are copies
    for atom_idx in range(len(atoms)):
        unique[atom_idx] = (\
            atoms[atom_idx].r[0] > 0.00 and atoms[atom_idx].r[0] < 37.36 and
            atoms[atom_idx].r[1] > 0.00 and atoms[atom_idx].r[1] < 37.36 and
            atoms[atom_idx].r[2] > 0.00 and atoms[atom_idx].r[2] < 37.36)
    
    # correct adjacency: remove ids of copies by ids of their originals
    tol_internal = 1e-3
    p_a, p_b, p_c = (bounds_a[1] - bounds_a[0]) * a, (bounds_b[1] - bounds_b[0]) * b, (bounds_c[1] - bounds_c[0]) * c
    replace_dict = {}
    for atom_idx in range(len(atoms)):
        replace_dict[atom_idx] = atom_idx
    for atom_idx in range(len(atoms)):
        if not unique[atom_idx]:
            continue
        for atom_idx_cmp in range(len(atoms)):
            if unique[atom_idx_cmp]:
                continue
            if compare_periodic(atoms[atom_idx].r, atoms[atom_idx_cmp].r, p_a, p_b, p_c):
                replace_dict[atom_idx_cmp] = atom_idx
    for atom_idx in range(len(atoms)):
        for adj_idx in range(len(atoms[atom_idx].adjacency)):
            atoms[atom_idx].adjacency[adj_idx] = replace_dict[atoms[atom_idx].adjacency[adj_idx]]
    
    np.save('__tmp/unique.npy', unique)
    adjacency_data = [atom.adjacency for atom in atoms]
    with open('__tmp/adjacency_data.pickle', 'wb') as handle:
        pickle.dump(adjacency_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    
    unique = np.load('__tmp/unique.npy')
    with open('__tmp/adjacency_data.pickle', 'rb') as handle:
        adjacency_data = pickle.load(handle)
    for atom_idx in range(len(atoms)):
        atoms[atom_idx].adjacency = np.unique(adjacency_data[atom_idx].copy()).tolist()

    # remove copies from atoms
    shift_ids = {}
    alive_count = 0
    for atom_idx in range(len(atoms)):
        if unique[atom_idx]:
            shift_ids[atom_idx] = alive_count
            alive_count += 1
    atoms = [atoms[atom_idx] for atom_idx in range(len(atoms)) if unique[atom_idx] > 0.0]
    
    # update adjacency after copies removal
    for atom_idx in range(len(atoms)):
        adjacency = atoms[atom_idx].adjacency
        for adj_idx in range(len(adjacency)):
            atoms[atom_idx].adjacency[adj_idx] = shift_ids[adjacency[adj_idx]]
            if adjacency[adj_idx] == atom_idx or adjacency[adj_idx] >= len(atoms):
                print('ERROR')
    return atoms
    '''

def select_in_box(atoms, bounds_x, bounds_y, bounds_z):
    new_atoms = []
    shift = {}
    count = 0
    for atom_idx in range(len(atoms)):
        if \
           atoms[atom_idx].r[0] > bounds_x[0] and atoms[atom_idx].r[0] < bounds_x[1] and \
           atoms[atom_idx].r[1] > bounds_y[0] and atoms[atom_idx].r[1] < bounds_y[1] and \
           atoms[atom_idx].r[2] > bounds_z[0] and atoms[atom_idx].r[2] < bounds_z[1]:
            new_atoms.append(atoms[atom_idx])
            shift[atom_idx] = count
            count += 1
    for atom_idx in range(len(new_atoms)):
        for adj_idx in range(len(new_atoms[atom_idx].adjacency)):
            if new_atoms[atom_idx].adjacency[adj_idx] in shift:
                new_atoms[atom_idx].adjacency[adj_idx] = shift[new_atoms[atom_idx].adjacency[adj_idx]]
            else:
                new_atoms[atom_idx].adjacency[adj_idx] = -1
        new_atoms[atom_idx].adjacency = list(filter(lambda x: x != -1, new_atoms[atom_idx].adjacency))
            
    return new_atoms
