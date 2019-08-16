# -*- coding:utf-8 -*-
import numpy as np
from mayavi import mlab

x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
u = np.sin(np.pi * x) * np.cos(np.pi * z)
v = -2 * np.sin(np.pi * y) * np.cos(2 * np.pi * z)
w = np.cos(np.pi * x) * np.sin(np.pi * z) + np.cos(np.pi * y) * np.sin(2 * np.pi * z)

src = mlab.pipeline.vector_field(u, v, w)
magnitude = mlab.pipeline.extract_vector_norm(src)
mlab.pipeline.iso_surface(magnitude, contours=[2.0, 0.5], opacity=0.3)
vec = mlab.pipeline.vectors(magnitude, mask_points=40, line_width=1,
                            color=(0.8, 0.8, 0.8), scale_factor=4.0)
flow = mlab.pipeline.streamline(magnitude, seedtype='plane', seed_visible=False,
                                seed_scale=0.5, seed_resolution=1, linetype='ribbon')
vcp = mlab.pipeline.vector_cut_plane(magnitude, mask_points=2, scale_factor=4,
                                     colormap='jet', plane_orientation='x_axes')
mlab.outline()
mlab.show()