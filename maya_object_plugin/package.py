# name = "maya_object_plugin"
# version = "1.0.0"
# description = "Maya plugin that prints selected object names"
# authors = ["YourName"]
# requires = ["maya-2025"]

# build_command = "python {root}/build.py {install_path}"
# private_build_requires = ["python"]  #  추가! python 필요하다고 명시!

# variants = [["platform-linux", "arch-x86_64"]]

# def commands():
#     env.MAYA_PLUG_IN_PATH.prepend("{this.root}/plug-ins")

name = "maya_object_plugin"
version = "1.0.0"
authors = ["Your Name"]
description = "Custom Maya Object Plugin"
requires = ["maya-2025"]
build_command = False

variants = [["platform-linux", "arch-x86_64"]]

def commands():
    # 이 플러그인이 설치된 경로 기준으로 설정
    env.MAYA_PLUG_IN_PATH.prepend("{this.root}/plug-ins")

    # (선택) 필요한 python 모듈이 있으면 PYTHONPATH도 추가
    env.PYTHONPATH.prepend("{this.root}/python")

    # 디버그 로그
    print(">> Loaded maya_object_plugin with plug-ins at: {this.root}/plug-ins")
