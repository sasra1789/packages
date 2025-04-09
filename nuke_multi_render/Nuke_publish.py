from PySide2.QtWidgets import (
    QMainWindow, QApplication, QLineEdit, QLabel, QCheckBox,QWidget,QSpacerItem,
    QVBoxLayout, QHBoxLayout, QSizePolicy,QPushButton
)

import os

import nuke

class NukePublishUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # UI 파일을 로드합니다.
        self.make_default_ui()
        
        self.pushButton_update.clicked.connect(self.update_write_nodes)
        self.pushButton_execute.clicked.connect(self.execute_render)

        self.update_write_nodes()
    def make_default_ui(self):
        # 메인 윈도우 설정
        self.setWindowTitle("MainWindow")
        self.setGeometry(0, 0, 700, 445)

        # 중앙 위젯 생성
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 레이아웃 생성
        self.layout = QVBoxLayout(self.central_widget)

        # 'Update nodes' 버튼 추가
        self.pushButton_update = QPushButton("Update nodes", self)
        self.layout.addWidget(self.pushButton_update)
        
        # 노드 레이아웃 추가
        self.write_nodes_layout = QVBoxLayout()
        self.layout.addLayout(self.write_nodes_layout)

        # Spacer 추가
        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(self.vertical_spacer)

        # 'Execute' 버튼 추가
        self.pushButton_execute = QPushButton("Execute", self)
        self.layout.addWidget(self.pushButton_execute)
        
        # 상태 바 추가
        self.statusbar = self.statusBar()
    
    def update_write_nodes(self):
        """Write 노드들을 업데이트하고 UI에 표시합니다."""
        # 리스트 초기화.
        self.write_nodes = []
        self.node_name_fields = []
        self.node_path_fields = []
        self.node_checkboxes = []

        # 기존 레이아웃 초기화
        self.clear_layout(self.write_nodes_layout)

        # 모든 Write 노드를 서치 후 리스트에 추가
        for node in nuke.allNodes():
            if node.Class() == "Write":
                self.write_nodes.append(node)

        # 각 Write 노드를 UI에 추가
        for node in self.write_nodes:
            node_name = node["name"].value()
            output_path = self.generate_output_path(node_name)
            self.add_node_item(node_name, output_path)

    def execute_render(self):
        """체크된 Write 노드들을 렌더링합니다."""
        # 체크박스 체크
        for checkbox in self.node_checkboxes:
            if checkbox.isChecked():
                # 체크된 항목의 인덱스를 찾아 노드 정보 갱신
                index = self.node_checkboxes.index(checkbox)
                node_name = self.node_name_fields[index].text()
                output_path = self.node_path_fields[index].text()
                
                # Nuke 노드를 찾고 출력 경로 및 품질 설정
                node = nuke.toNode(node_name)
                node["file"].setValue(output_path)
                node["_jpeg_quality"].setValue(1)

                # 첫 번째 및 마지막 프레임을 가져옴
                root = nuke.Root()
                start_frame = int(root["first_frame"].value())
                end_frame = int(root["last_frame"].value())

                # 출력 디렉토리를 생성
                output_dir = os.path.dirname(output_path)
                os.makedirs(output_dir, exist_ok=True)
                
                # 렌더링을 실행
                nuke.execute(node, start_frame, end_frame, 1)

    def clear_layout(self, layout):
        """입력된 레이아웃에서 모든 항목을 제거합니다."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def generate_output_path(self, node_name):
        """스크립트 이름과 노드 이름을 기반으로 출력 경로를 생성합니다."""
        script_path = nuke.scriptName()
        script_dir, script_file = os.path.split(script_path)
        file_name, _ = os.path.splitext(script_file)
        return f"{script_dir}/{file_name}/{file_name}_{node_name}.%04d.jpg"

    def add_node_item(self, node_name, output_path):
        """Write 노드에 대한 UI 항목을 추가합니다."""
        # Write 노드 항목 레이아웃
        node_entry_layout = QHBoxLayout()
        self.write_nodes_layout.addLayout(node_entry_layout)
        # 노드 정보 레이아웃
        node_info_layout = QVBoxLayout()
        node_entry_layout.addLayout(node_info_layout)
        
        # 노드 체크박스 생성
        node_checkbox = QCheckBox()
        node_entry_layout.addWidget(node_checkbox)
        node_checkbox.toggle()
        self.node_checkboxes.append(node_checkbox)

        # 노드 이름 입력란
        # 노드 이름 라벨
        name_layout = QHBoxLayout()
        node_info_layout.addLayout(name_layout)
        name_label = QLabel("Node")
        name_label.setFixedWidth(40)
        name_layout.addWidget(name_label)
        # 노드 입력 라인에딧
        name_field = QLineEdit()
        name_field.setText(node_name)
        name_layout.addWidget(name_field)
        self.node_name_fields.append(name_field)

        # 출력 경로 입력란
        # 패스 라벨
        path_layout = QHBoxLayout()
        node_info_layout.addLayout(path_layout)
        path_label = QLabel("Path")
        path_label.setFixedWidth(40)
        path_layout.addWidget(path_label)
        # 패스 입력 라인에딧
        path_field = QLineEdit()
        path_field.setText(output_path)
        path_layout.addWidget(path_field)
        self.node_path_fields.append(path_field)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    nuke_publish_ui = NukePublishUI()
    nuke_publish_ui.show()
    sys.exit(app.exec_())
else:
    nuke_publish_ui = NukePublishUI()
    nuke_publish_ui.show()

"""
import imp
import sys
import nuke
sys.path.append("/home/rapa/nuke/python")
import Nuke_publish
imp.reload(Nuke_publish)
"""

