from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI

s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)

# create a GUI with Python Shell
gui = GUI()
win = ivtk.IVTKWithCrustAndBrowser()
win.open()
win.scene.add_actor(a)

# start GUI loop
gui.start_event_loop()