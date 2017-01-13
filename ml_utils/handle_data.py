import hickle
import os
import numpy as np
import h5py

def cache_data(data, path):
    if os.path.isdir(os.path.dirname(path)):
        file = open(path, 'w')
        hickle.dump(data, file)
        file.close()
    else:
        print('Directory doesn\'t exists; Creating..')
        os.mkdir(os.path.dirname(path), 0755)
        file = open(path, 'w')
        hickle.dump(data, file)
        file.close()

def restore_data(path):
    data = dict()
    if os.path.isfile(path):
        file = open(path, 'r')
        data = hickle.load(file)
    return data

def print_h5_keys(h5File):
    f = h5py.File(h5File, 'r')
    print f.keys()

def read_h5_key_value(h5File, key):
    f = h5py.File(h5File, 'r')
    value = f.get(key)
    return value

def swap_axes(npArray, axis0, axis1):
    npArray = np.swapaxes(npArray, 1, 2)
    npArray = np.swapaxes(npArray, 2, 3)
    return npArray
