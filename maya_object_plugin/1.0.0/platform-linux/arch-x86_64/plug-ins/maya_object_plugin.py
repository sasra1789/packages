# src/maya_object_plugin.py
import maya.api.OpenMaya as om

def maya_useNewAPI():
    pass

class MayaObjectCommand(om.MPxCommand):
    COMMAND_NAME = "mayaObject"

    def __init__(self):
        super().__init__()

    def doIt(self, args):
        selection = om.MGlobal.getActiveSelectionList()
        if selection.length() == 0:
            om.MGlobal.displayInfo("아무것도 선택되지 않았어요.")
        else:
            for i in range(selection.length()):
                dagPath = selection.getDagPath(i)
                om.MGlobal.displayInfo(f"선택된 오브젝트: {dagPath.fullPathName()}")

def cmdCreator():
    return MayaObjectCommand()

def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.registerCommand(MayaObjectCommand.COMMAND_NAME, cmdCreator)
    om.MGlobal.displayInfo("mayaObject 플러그인 로드됨!")

def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    pluginFn.deregisterCommand(MayaObjectCommand.COMMAND_NAME)
    om.MGlobal.displayInfo("mayaObject 플러그인 언로드됨!")
