# import os
# import shutil
# import sys

# def main():
#     root_dir = os.path.abspath(os.path.dirname(__file__))
#     source_path = os.path.join(root_dir, "src", "maya_object_plugin.py")

#     install_path = sys.argv[1]
#     dest_dir = os.path.join(install_path, "plug-ins")
    
#     with open(os.path.join(install_path, "build_complete.txt"), "w") as f:
#         f.write("done")


#     os.makedirs(dest_dir, exist_ok=True)
#     shutil.copy2(source_path, dest_dir)

#     print(f" 플러그인 설치 완료: {source_path} → {dest_dir}")

#     # Rez가 설치됐다고 인식하게 하는 "마커 파일"
#     marker_file = os.path.join(install_path, "build_complete.txt")
#     with open(marker_file, "w") as f:
#         f.write("installed!")

# if __name__ == "__main__":
#     main()

# """ 페이즈2"""
# import os
# import shutil
# import sys

# def main():
#     install_path = sys.argv[1]
#     source_path = os.path.join(os.path.dirname(__file__), "src", "maya_object_plugin.py")
#     dest_dir = os.path.join(install_path, "plug-ins")

#     os.makedirs(dest_dir, exist_ok=True)
#     shutil.copy2(source_path, dest_dir)

#     print(f" 플러그인 설치 완료: {source_path} → {dest_dir}")

#     #  반드시 이 파일 이름이어야 Rez가 인식함!
#     marker_path = os.path.join(install_path, ".rez_installed.txt")
#     print(" 마커 생성 시도 중...")
#     with open(marker_path, "w") as f:
#         f.write("installed")
#     print(f" 마커 파일 생성됨: {marker_path}")

# if __name__ == "__main__":
#     main()
# build.py
import os
import sys
import shutil

def main():
    install_path = sys.argv[1]
    print(f"[BUILD] install_path = {install_path}")  #  로그 확인용

    # 플러그인 파일 복사
    plugin_src = os.path.join(os.path.dirname(__file__), "src", "maya_object_plugin.py")
    plugin_dest = os.path.join(install_path, "plug-ins")
    os.makedirs(plugin_dest, exist_ok=True)
    shutil.copy2(plugin_src, plugin_dest)
    print(f"[BUILD] 플러그인 복사 완료: {plugin_src} -> {plugin_dest}")

    # 마커 파일 생성
    marker_path = os.path.join(install_path, ".rez_installed.txt")
    with open(marker_path, "w") as f:
        f.write("installed\n")
    print(f"[BUILD] 마커 생성됨: {marker_path}")

if __name__ == "__main__":
    main()
