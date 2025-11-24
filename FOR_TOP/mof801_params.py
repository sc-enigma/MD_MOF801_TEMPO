def get_mof801_params():
    # [atom_type] = m
    mass = {}
    mass['itcFF_Zr'] = 91.224
    mass['itcFF_H1'] =  1.008
    mass['itcFF_H7'] =  1.008
    mass['itcFF_O1'] = 16.000
    mass['itcFF_O2'] = 16.000
    mass['itcFF_C1'] = 12.011
    mass['itcFF_C2'] = 12.011
 
    # [atom_type] = q
    charge = {}
    charge['itcFF_Zr'] =  2.2168
    charge['itcFF_H1'] =  0.2343
    charge['itcFF_H7'] =  0.2343
    charge['itcFF_O1'] = -0.7785
    charge['itcFF_O2'] = -0.6272
    charge['itcFF_C1'] =  0.7608
    charge['itcFF_C2'] = -0.1282

    # [atom_type-atom_type] = [funct, r0, k]
    bond_params = {}
    bond_params['itcFF_C1-itcFF_C2'] = [1, 0.1514, 259408.438]
    bond_params['itcFF_C2-itcFF_C2'] = [1, 0.1324, 259408.512]
    bond_params['itcFF_C1-itcFF_O1'] = [1, 0.1267, 376560.000]
    bond_params['itcFF_C2-itcFF_H1'] = [1, 0.0930, 284512.408]
    bond_params['itcFF_O3-itcFF_Zr'] = [3, 0.2061, 109.0350, 19.8000]
    bond_params['itcFF_O1-itcFF_Zr'] = [3, 0.2240, 109.0350, 19.8000]
    bond_params['itcFF_O2-itcFF_Zr'] = [3, 0.2256, 109.0350, 19.8000]
    bond_params['itcFF_O2-itcFF_H7'] = [1, 0.1090, 284512.408]
    bond_params['itcFF_Zr-itcFF_Zr'] = [1, 0.3498, 173523.512]    

    # [atom_type-atom_type-atom_type] = [funct, angle, k]
    angle_params = {}
    angle_params['itcFF_O1-itcFF_Zr-itcFF_O1'] = [1,  76.62, 669.440]
    angle_params['itcFF_C1-itcFF_O1-itcFF_Zr'] = [1, 130.20, 109.500]
    angle_params['itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [1,  59.95, 527.184]
    angle_params['itcFF_O2-itcFF_Zr-itcFF_O2'] = [1,  76.26, 669.440]
    angle_params['itcFF_C1-itcFF_C2-itcFF_C2'] = [1, 118.48, 527.184]
    angle_params['itcFF_C2-itcFF_C1-itcFF_O1'] = [1, 116.40, 120.400]
    angle_params['itcFF_O1-itcFF_Zr-itcFF_Zr'] = [1, 109.73, 120.400]
    angle_params['itcFF_O1-itcFF_C1-itcFF_O1'] = [1, 129.88, 669.440]
    angle_params['itcFF_Zr-itcFF_O2-itcFF_Zr'] = [1, 101.42, 109.500]
    angle_params['itcFF_O2-itcFF_Zr-itcFF_Zr'] = [1,  39.38, 120.400]
    angle_params['itcFF_O1-itcFF_Zr-itcFF_O2'] = [1,  71.29, 669.440]
    
    # [atom_type-atom_type-atom_type-atom_type] = [funct, angle, k, n]        - periodic
    # [atom_type-atom_type-atom_type-atom_type] = [funct, c1, c2, c3, c4, c5] - fourier
    dihedral_params = {}
    dihedral_params['itcFF_C1-itcFF_O1-itcFF_Zr-itcFF_O1'] = [9, 116.17, 3.09616, 2]
    dihedral_params['itcFF_C1-itcFF_O1-itcFF_Zr-itcFF_O2'] = [9, 41.09, 3.09616, 2]
    dihedral_params['itcFF_Zr-itcFF_Zr-itcFF_O2-itcFF_Zr'] = [9, 105.70, 3.09616, 2]
    dihedral_params['itcFF_C2-itcFF_C2-itcFF_C1-itcFF_O1'] = [9, 172.99, 3.09616, 2]
    dihedral_params['itcFF_Zr-itcFF_O2-itcFF_Zr-itcFF_Zr'] = [9, 22.98, 3.09616, 2]
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [9, 166.39, 3.09616, 2]
    dihedral_params['itcFF_O2-itcFF_Zr-itcFF_O2-itcFF_Zr'] = [9, 117.18, 3.09616, 2]
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_Zr-itcFF_O2'] = [9, 13.06, 3.09616, 2]
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_Zr-itcFF_O1'] = [9, 69.04, 3.09616, 2]
    dihedral_params['itcFF_O1-itcFF_C1-itcFF_O1-itcFF_Zr'] = [9, 0.62, 3.09616, 2]
    dihedral_params['itcFF_Zr-itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [9, 54.83, 3.09616, 2]
    dihedral_params['itcFF_C2-itcFF_C1-itcFF_O1-itcFF_Zr'] = [9, 179.80, 3.09616, 2]
    dihedral_params['itcFF_C1-itcFF_C2-itcFF_C2-itcFF_C1'] = [9, 179.84, 3.09616, 2]
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_O2-itcFF_Zr'] = [9, 167.02, 3.09616, 2]
    dihedral_params['itcFF_O2-itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [9, 153.33, 3.09616, 2]
    dihedral_params['itcFF_O2-itcFF_Zr-itcFF_Zr-itcFF_O2'] = [9, 162.09, 3.09616, 2]
    dihedral_params['itcFF_C1-itcFF_O1-itcFF_Zr-itcFF_Zr'] = [9, 48.83, 3.09616, 2]

















    return mass, charge, bond_params, angle_params, dihedral_params