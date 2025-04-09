# -*- coding: utf-8 -*-

name = 'maya_object_plugin'

version = '1.0.0'

description = 'Custom Maya Object Plugin'

authors = ['Your Name']

requires = ['maya-2025']

variants = [['platform-linux', 'arch-x86_64']]

def commands():
    # 이 플러그인이 설치된 경로 기준으로 설정
    env.MAYA_PLUG_IN_PATH.prepend("{this.root}/plug-ins")
    
    # (선택) 필요한 python 모듈이 있으면 PYTHONPATH도 추가
    env.PYTHONPATH.prepend("{this.root}/python")
    
    # 디버그 로그
    print(">> Loaded maya_object_plugin with plug-ins at: {this.root}/plug-ins")

timestamp = 1744079891

format_version = 2
