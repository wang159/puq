import numpy as np


def dump_hdf5(name, v, desc=''):
    np.set_printoptions(threshold=np.nan)
    line = pickle({'name': name, 'desc': desc, 'value': v})
    print 'HDF5:%s:5FDH' % line
