def get_mof801_params():
    # [atom_type] = m
    mass = {}
    mass['itcFF_Zr'] = 91.224
    mass['itcFF_O1'] = 16.000
    mass['itcFF_O2'] = 16.000
    mass['itcFF_C1'] = 12.011
    mass['itcFF_C2'] = 12.011
    mass['itcFF_H1'] =  1.008
    mass['itcFF_H7'] =  1.008
 
    # [atom_type] = q
    charge = {}
    charge['itcFF_Zr'] =  1.968
    charge['itcFF_O1'] = -0.633
    charge['itcFF_O2'] = -0.902
    charge['itcFF_C1'] =  0.630
    charge['itcFF_C2'] = -0.309
    charge['itcFF_H1'] =  0.131
    charge['itcFF_H7'] =  0.402
    
    # [atom_type-atom_type] = [funct, r0, k]
    bond_params = {}

    bond_params['itcFF_Zr-flexFF_O1'] = [1, 0.2232, 287290.200]
    bond_params['itcFF_Zr-flexFF_O2'] = [1, 0.2098, 107733.800]   
    bond_params['itcFF_C1-itcFF_O1'] = [1, 0.1273, 451872.000]
    bond_params['itcFF_O2-itcFF_H7'] = [1, 0.1080, 304106.800]
    bond_params['itcFF_C2-itcFF_H1'] = [1, 0.1080, 304106.800]
    bond_params['itcFF_C1-itcFF_C2'] = [1, 0.1514, 293928.300]
    bond_params['itcFF_C2-itcFF_C2'] = [1, 0.1324, 293928.300]
    
    # [atom_type-atom_type-atom_type] = [funct, angle, k]
    angle_params = {}
    angle_params['itcFF_O1-itcFF_Zr-itcFF_O1'] = [1,  74.400, 115.776]
    angle_params['itcFF_O2-itcFF_Zr-itcFF_O2'] = [1, 100.400, 115.776]
    angle_params['itcFF_O1-itcFF_Zr-itcFF_O2'] = [1, 150.500, 115.776]
    angle_params['itcFF_C1-itcFF_O1-itcFF_Zr'] = [1, 135.800, 231.637]
    angle_params['itcFF_O1-itcFF_C1-itcFF_O1'] = [1, 125.000,1213.360]    
    angle_params['itcFF_C2-itcFF_C1-itcFF_O1'] = [1, 117.300, 456.013]    
    angle_params['itcFF_C2-itcFF_C2-itcFF_H1'] = [1, 120.000, 309.616]
    angle_params['itcFF_C1-itcFF_C2-itcFF_H1'] = [1, 120.000, 309.616]
    angle_params['itcFF_C1-itcFF_C2-itcFF_C2'] = [1, 120.000, 231.637]
    # angle_params['itcFF_H7-itcFF_O2-itcFF_Zr'] = [1, 134.8165, 460.240]
    
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