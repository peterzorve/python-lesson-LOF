
import os 
import pandas as pd 
import matplotlib.pyplot as plt 



def find_everything(file):
    idx_1 = file.find('_')
    idx_2 = file.find('_', idx_1+1)
    shape = file[idx_1+1:idx_2].capitalize()

    mgcl_idx_1 = file.find('2)')
    mgcl_idx_2 = file.find('_(', mgcl_idx_1)
    mgcl2 = file[mgcl_idx_1+2 : mgcl_idx_2]

    alcl_idx_1 = file.find('3)')
    alcl_idx_2 = file.find('.log', alcl_idx_1 )
    alcl3 = file[alcl_idx_1+2 : alcl_idx_2]

    return shape, int(mgcl2), int(alcl3)


folder_path = "C:/Users/zorve/OneDrive/Desktop/python-lesson_LOF/data"
file_path =   "C:/Users/zorve/OneDrive/Desktop/python-lesson_LOF/data/"

gibbs_energy, gibbs_shapes, gibbs_mgcl2, gibbs_alcl3   = [], [], [], []

for file in os.listdir(folder_path):
    files = file_path + file
    with open(files, 'r') as f: 
        lines = f.readlines()

        shape, mgcl2, alcl3 = find_everything(file)
        gibbs_shapes.append(shape), gibbs_mgcl2.append(mgcl2), gibbs_alcl3.append(alcl3)

        for line in lines:
            if line.startswith(' Sum of electronic and thermal Free Energies='):
                gibbs = float(line[45:].strip())

                gibbs_energy.append(round(gibbs * 0.001, 1))

data = pd.DataFrame({'shape' : gibbs_shapes, 'mgcl2' : gibbs_mgcl2, 'alcl3' : gibbs_alcl3, 'kjmol-1' : gibbs_energy})

data = data.sort_values(by='mgcl2')

data['per MgCl2'] = round(data['kjmol-1'] / data['mgcl2'], 1)
data['per AlCl3'] = round(data['kjmol-1'] / data['alcl3'], 1)

plt.bar(gibbs_mgcl2, data['kjmol-1'] / data['mgcl2'] )
plt.ylim(bottom=-5, top=-1)
plt.show()


