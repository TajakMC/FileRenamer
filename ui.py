from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QListWidget, QMessageBox, QCheckBox
)
from PySide6.QtCore import Qt
import os
from renamer import FileBatchRenamer

class FileRenamerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파일 일괄 이름 변경기')
        self.resize(650, 500)

        # 메인 레이아웃
        main_layout = QVBoxLayout(self)

        # 1. 파일 목록
        self.file_list = QListWidget()
        main_layout.addWidget(self.file_list)

        # 2. 파일 선택 버튼
        self.select_btn = QPushButton('파일 선택')
        self.select_btn.clicked.connect(self.select_files)
        main_layout.addWidget(self.select_btn)

        # 3. 옵션 입력 (Form Layout)
        form_layout = QFormLayout()
        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText('예: IMG_')
        form_layout.addRow('접두어:', self.prefix_input)

        self.suffix_input = QLineEdit()
        self.suffix_input.setPlaceholderText('예: _edited 또는 _{OrderNo}')
        form_layout.addRow('접미어:', self.suffix_input)

        self.keep_name_checkbox = QCheckBox('기존 파일명 유지')
        self.keep_name_checkbox.setChecked(True)
        form_layout.addRow(self.keep_name_checkbox)

        main_layout.addLayout(form_layout)

        # 4. 실행 버튼
        self.rename_btn = QPushButton('이름 일괄 변경')
        self.rename_btn.clicked.connect(self.rename_files)
        main_layout.addWidget(self.rename_btn)

        # 스타일시트 적용
        self.apply_stylesheet()

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, '파일 선택', '', '모든 파일 (*)')
        if files:
            self.file_list.clear()
            self.file_list.addItems(files)

    def rename_files(self):
        files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
        if not files:
            QMessageBox.warning(self, "경고", "파일을 선택하세요.")
            return

        prefix = self.prefix_input.text()
        suffix = self.suffix_input.text()
        keep_name = self.keep_name_checkbox.isChecked()

        # renamer.py의 클래스를 사용하여 파일 이름 변경
        # '{OrderNo}'가 있으면 일련번호를 사용하도록 renamer.py가 처리함
        use_serial = '{OrderNo}' in prefix or '{OrderNo}' in suffix

        success, message, changed_files_info = FileBatchRenamer.rename_files(
            files, prefix, suffix, use_serial=use_serial, keep_name=keep_name
        )

        if success:
            # 성공 시, 변경된 파일 경로 목록으로 리스트를 새로고침
            if changed_files_info:
                # 원본 파일 경로에서 디렉토리 경로를 가져와 새 파일명과 조합
                dir_name = os.path.dirname(files[0])
                renamed_paths = [os.path.join(dir_name, new_name) for _, new_name in changed_files_info]
                self.file_list.clear()
                self.file_list.addItems(renamed_paths)
            else: # 변경된 파일이 없는 경우 (예: 입력값이 없어 이름이 그대로인 경우)
                self.file_list.clear()
                self.file_list.addItems(files) # 기존 파일 목록 유지
        else:
            # 실패 시 오류 메시지 표시
            QMessageBox.critical(self, "오류", message)
            # 실패 시 목록을 원래대로 복원
            self.file_list.clear()
            self.file_list.addItems(files)

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-size: 14px;
            }
            QListWidget {
                border: 2px dashed #0078d7;
                background-color: white;
                padding: 5px;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 10px;
                font-size: 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QLineEdit {
                border: 1px solid #ccc;
                padding: 8px;
                font-size: 14px;
                border-radius: 5px;
            }
            QLabel {
                font-size: 14px;
                padding-top: 8px;
            }
        """)