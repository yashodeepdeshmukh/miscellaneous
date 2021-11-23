import os

import pandas as pd

os.chdir(r'PATH NAME')
dir_path=os.getcwd()
FOLDERPATH1=os.path.join(dir_path,'FOLDERNAME1')
FOLDERPATH2=os.path.join(dir_path,'FOLDERNAME2')
datasets=[]
#cell_model
list1=os.listdir(FOLDERPATH1)
file1={}
for i in list1:
    n=''.join((i.split('.'))[:-1])
    file=os.path.join(cell_model_path,i)
    file1[n]=pd.read_csv(file,low_memory=False,index_col=0)

for key,val in file1.items():
        exec(key + '=val')
        datasets.append(key)
#tcga_data
list2=os.listdir(FOLDERPATH2)
file2={}
for j in list2:
    m=''.join((j.split('.'))[:-1])
    file=os.path.join(tcga_path,j)
    file2[m]=pd.read_csv(file,low_memory=False,index_col=0)
for key,val in file2.items():
        exec(key + '=val')
        datasets.append(key)
print(datasets)
