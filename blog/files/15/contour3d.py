# -*- coding:utf-8 -*-
import numpy as np
from mayavi import mlab

x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
scalars = x * x + y * y + z * z

obj = mlab.contour3d(scalars, contours=6, transparent=True)
mlab.show()