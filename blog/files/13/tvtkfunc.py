def ivtk_scene(actors):
    from tvtk.tools import ivtk

    win = ivtk.IVTKWithCrustAndBrowser()
    win.open()
    win.scene.add_actor(actors)

    return win

def event_loop():
    from pyface.api import GUI
    gui = GUI()
    gui.start_event_loop()
