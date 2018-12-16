# -*- coding:utf-8 -*-
import numpy as np
from mayavi import mlab

s = np.random.random((20, 20))

img = mlab.imshow(s, colormap='gist_earth')
mlab.show()