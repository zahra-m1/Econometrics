#! usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
data = np.loadtxt("TrainExer21.txt",
                  dtype = np.str)[1:,:].astype(np.float)
data[:,0] = 1
X2 = np.matrix(data[:, 4:7])
X1 = np.matrix(data[:, [0,3]])
P = (X1.T*X1).I*X1.T*X2
print(P)
