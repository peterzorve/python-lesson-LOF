
import os 
import pandas as pd 




folder_path = "C:/Users/zorve/OneDrive/Desktop/python-lesson_LOF/data"

file_name, extracted_number = [], []

for file in os.listdir(folder_path):
    # print(file)
    path = f'{folder_path}/' + file 
    # print(path)

    with open(path, 'r') as f:
        lines = f.readlines()
    # print(lines)
    
    for line in lines:
        # print(line)
        if line.startswith(' Sum of electronic and thermal Free Energies='):
            # print(line[:20])
            number = float(line[47:].strip())
            file_name.append(file), extracted_number.append(number)

            # print(number)


# print(extracted_number)

df = pd.DataFrame({'file_name' : file_name, 'gibbs_energy' : extracted_number})
df['kJmol-1'] = round(df['gibbs_energy'] * 0.001, 2)

# print(df)
df.to_csv('gibbs.csv')


my_list = [ '10_pyramid_(MgCl2)27_(AlCl3)14.log',
            '11_slab_(MgCl2)28_(AlCl3)14.log',
            '12_pipe_(MgCl2)29_(AlCl3)16.log',
            '13_diamond_(MgCl2)34_(AlCl3)16.log',
            '14_quadrangle_(MgCl2)36_(AlCl3)16.log',
            '1_quadrangle_(MgCl2)4_(AlCl3)6.log',
            '2_pyramid_(MgCl2)5_(AlCl3)7.log',
            '3_diamond_(MgCl2)7_(AlCl3)8.log',
            '4_pipe_(MgCl2)9_(AlCl3)8.log',
            '5_diamond_(MgCl2)14_(AlCl3)10.log',
            '6_quadrangle_(MgCl2)16_(AlCl3)10.log',
            '7_pipe_(MgCl2)19_(AlCl3)12.log',
            '8_pipe_(MgCl2)24_(AlCl3)14.log',
            '9_quaqdrangle_(MgCl2)25_(AlCl3)14.log']

for item in my_list:
    shape_idx_1 = item.find('_')
    shape_idx_2 = item.find('_', shape_idx_1+1)
    shape = item[shape_idx_1+1:shape_idx_2]

    print(shape)

for item in my_list:
    mgcl2_idx_1 = item.find('2)')
    mgcl2_idx_2 = item.find('_(', mgcl2_idx_1+1)
    mgcl2 = item[mgcl2_idx_1+2:mgcl2_idx_2]
    print(mgcl2)


for item in my_list:
    alcl3_idx_1 = item.find('3)')
    alcl3_idx_2 = item.find('.log', alcl3_idx_1+1)
    alcl3 = item[alcl3_idx_1+2:alcl3_idx_2]
    print(alcl3)