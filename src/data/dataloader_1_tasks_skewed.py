import os,sys
import numpy as np
import torch
from torchvision import datasets,transforms
import pandas as pd

# Downloads the MNIST dataset and divides it in two tasks
########################################################################################################################

def get(data_path):
    # Load dataset:
    full_set = pd.read_csv(data_path)
    # Shuffle:
    full_set = full_set.sample(frac=7/8)
    data= {}
    task_outputs = []
    size = [1,29]
    data[0] = {}
    data[0]['name'] = 'All actions'
    data[0]['n_outputs'] = 32
    data[0]['train']= {'x': torch.tensor([full_set.iloc[0:-1000,0:-8].values])[0],'y': torch.tensor([full_set.iloc[0:-1000,-8:].values])[0]}
    data[0]['valid']= {'x': torch.tensor([full_set.iloc[-1000:,0:-8].values])[0],'y': torch.tensor([full_set.iloc[-1000:,-8:].values])[0]}


    # Others
    n=0
    for t in data.keys():
        task_outputs.append((t, data[t]['n_outputs']))
        n += data[t]['n_outputs']
    data['ncla'] = n

    return data, task_outputs, size

########################################################################################################################
