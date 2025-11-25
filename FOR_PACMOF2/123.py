import numpy as np

with open('C:\\PROJECTS\\MD_MOF801\\FOR_PACMOF2\\mof801_pacmof_1.cif', 'r') as f:
    lines = [l.replace('\n', '') for l in f]
    spl = [[l.split()[0], l.split()[1], float(l.split()[2]), float(l.split()[3]), float(l.split()[4])] for l in lines]
    
    i, j = 0, 0
    while i < len(spl):
        j = i + 1
        while j < len(spl):
            v1 = np.array([spl[i][2], spl[i][3], spl[i][4]])
            v2 = np.array([spl[j][2], spl[j][3], spl[j][4]])
            if np.linalg.norm(v1 - v2) < 0.01:
                spl.pop(j)
                break
            j += 1
        i += 1
    
    with open('C:\\PROJECTS\\MD_MOF801\\FOR_PACMOF2\\mof801_pacmof_2.cif', 'w') as f2:
        for rec in spl:
            f2.write(f'{rec[0]} {rec[1]} {rec[2]} {rec[3]} {rec[4]}\n')