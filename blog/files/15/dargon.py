# -*- coding:utf-8 -*-
from mayavi import mlab
import os
import tarfile

# 读取tar压缩文件
# 这里有个玄学，直接读取自己解压的ply会出现vtk错误，但是在代码里解压就不报错
dragon_tar_file = tarfile.open('dragon.tar.gz')
try:
    os.mkdir('dragon_data')
except:
    pass
dragon_tar_file.extractall('dragon_data')
dragon_tar_file.close()
dragon_ply_file = os.path.join('dragon_data', 'dragon_recon', 'dragon_vrip.ply')

# 渲染dragon ply文件
mlab.pipeline.surface(mlab.pipeline.open(dragon_ply_file))
mlab.show()

# 删除解压的文件夹
import shutil
shutil.rmtree('dragon_data')