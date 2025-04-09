name = "nuke_multi_render"
version = "1.0.0"

requires = ["python-3.9", "PySide2-5.15+"]

def commands():
    env.PYTHONPATH.append('{root}/python')
    env.PATH.append('{root}/bin')