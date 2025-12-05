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
    charge['itcFF_Zr'] =  1.38159
    charge['itcFF_H1'] =  0.1014
    charge['itcFF_H7'] =  0.3027
    charge['itcFF_O1'] = -0.5296
    charge['itcFF_O2'] = -0.5868
    charge['itcFF_C1'] =  0.4962
    charge['itcFF_C2'] = -0.1692
    
    # [atom_type-atom_type] = [funct, r0, k]
    bond_params = {}
    bond_params['itcFF_C1-itcFF_C2'] = [1, 0.1514, 259408.438]
    bond_params['itcFF_C2-itcFF_C2'] = [1, 0.1324, 259408.512]
    bond_params['itcFF_C1-itcFF_O1'] = [1, 0.1267, 376560.000]
    bond_params['itcFF_C2-itcFF_H1'] = [1, 0.0930, 284512.408]
    bond_params['itcFF_O3-itcFF_Zr'] = [1, 0.2061, 376560.000]
    bond_params['itcFF_O1-itcFF_Zr'] = [1, 0.2240, 376560.000]
    bond_params['itcFF_O2-itcFF_Zr'] = [1, 0.2256, 376560.000]
    bond_params['itcFF_O2-itcFF_H7'] = [1, 0.1090, 284512.408]
    # bond_params['itcFF_Zr-itcFF_Zr'] = [1, 0.3498, 173523.512]    

    # [atom_type-atom_type-atom_type] = [funct, angle, k]
    angle_params = {}
    angle_params['itcFF_O1-itcFF_Zr-itcFF_Zr'] = [1, 164.0260, 669.440]
    angle_params['itcFF_O1-itcFF_Zr-itcFF_O1'] = [1,  76.6239, 669.440]
    angle_params['itcFF_O2-itcFF_Zr-itcFF_O2'] = [1,  76.6888, 669.440]
    angle_params['itcFF_O2-itcFF_Zr-itcFF_Zr'] = [1,  39.2636, 669.440]
    angle_params['itcFF_O1-itcFF_Zr-itcFF_O2'] = [1, 140.8839, 669.440]
    angle_params['itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [1,  60.0000, 669.440]
    angle_params['itcFF_Zr-itcFF_O2-itcFF_Zr'] = [1, 101.9165, 669.440]
    angle_params['itcFF_O1-itcFF_C1-itcFF_O1'] = [1, 129.8778, 669.440]
    angle_params['itcFF_C2-itcFF_C1-itcFF_O1'] = [1, 116.4024, 669.440] 
    angle_params['itcFF_C1-itcFF_O1-itcFF_Zr'] = [1, 131.0393, 502.080]
    angle_params['itcFF_C2-itcFF_C2-itcFF_H1'] = [1, 120.7132, 418.400]
    angle_params['itcFF_C1-itcFF_C2-itcFF_H1'] = [1, 120.8076, 418.400]
    angle_params['itcFF_C1-itcFF_C2-itcFF_C2'] = [1, 118.4791, 418.400]
    angle_params['itcFF_H7-itcFF_O2-itcFF_Zr'] = [1, 134.8165, 460.240]
    
    # [atom_type-atom_type-atom_type-atom_type] = [funct, angle, k, n]        - periodic
    # [atom_type-atom_type-atom_type-atom_type] = [funct, c1, c2, c3, c4, c5] - fourier
    dihedral_params = {}
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_Zr-itcFF_O1'] = [9,  69.2207, 4.60240, 2]
    dihedral_params['itcFF_Zr-itcFF_O2-itcFF_Zr-itcFF_Zr'] = [9, 105.0829, 4.60240, 2]
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [9,   1.1384, 4.60240, 2]
    dihedral_params['itcFF_O2-itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [9, 154.0040, 4.60240, 2]
    dihedral_params['itcFF_H7-itcFF_O2-itcFF_Zr-itcFF_O1'] = [9, 105.5045, 4.60240, 2]
    dihedral_params['itcFF_O2-itcFF_Zr-itcFF_Zr-itcFF_O2'] = [9, 162.0955, 4.60240, 2]
    dihedral_params['itcFF_C2-itcFF_C1-itcFF_O1-itcFF_Zr'] = [9, 179.9613, 4.60240, 2]
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_Zr-itcFF_O2'] = [9, 12.41910, 4.60240, 2]
    dihedral_params['itcFF_C1-itcFF_O1-itcFF_Zr-itcFF_O1'] = [9, 116.8298, 4.60240, 2]
    dihedral_params['itcFF_H7-itcFF_O2-itcFF_Zr-itcFF_Zr'] = [9, 166.8349, 4.60240, 2]
    dihedral_params['itcFF_C1-itcFF_O1-itcFF_Zr-itcFF_Zr'] = [9,   0.9832, 4.60240, 2]
    dihedral_params['itcFF_H7-itcFF_O2-itcFF_Zr-itcFF_O2'] = [9, 179.0884, 4.60240, 2]
    dihedral_params['itcFF_Zr-itcFF_Zr-itcFF_Zr-itcFF_Zr'] = [9, 109.5114, 4.60240, 2]
    dihedral_params['itcFF_O2-itcFF_Zr-itcFF_O2-itcFF_Zr'] = [9, 117.2833, 4.60240, 2]
    dihedral_params['itcFF_C1-itcFF_O1-itcFF_Zr-itcFF_O2'] = [9,  79.6248, 4.60240, 2]
    dihedral_params['itcFF_C1-itcFF_C2-itcFF_C2-itcFF_C1'] = [9, 179.8450, 4.60240, 2]
    dihedral_params['itcFF_O1-itcFF_Zr-itcFF_O2-itcFF_Zr'] = [9, 86.56357, 4.60240, 2]
    dihedral_params['itcFF_C2-itcFF_C2-itcFF_C1-itcFF_O1'] = [9,   6.5133, 4.60240, 2]
    dihedral_params['itcFF_Zr-itcFF_Zr-itcFF_O2-itcFF_Zr'] = [9, 105.0829, 4.60240, 2]
    dihedral_params['itcFF_O1-itcFF_C1-itcFF_O1-itcFF_Zr'] = [9,   0.7736, 4.60240, 2]

















    return mass, charge, bond_params, angle_params, dihedral_params