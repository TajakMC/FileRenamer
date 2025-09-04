from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QListWidget, QMessageBox, QCheckBox, QSpinBox
)
import sys
import os
from renamer import FileBatchRenamer

class FileRenamerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파일 일괄 이름 변경기')
        self.resize(600, 400)
        layout = QVBoxLayout()

        # 파일 리스트
        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        # 파일 선택 버튼
        btn_layout = QHBoxLayout()
        self.select_btn = QPushButton('파일 선택')
        self.select_btn.clicked.connect(self.select_files)
        btn_layout.addWidget(self.select_btn)
        layout.addLayout(btn_layout)


    # 접두어/접미어 입력
    prefix_layout = QHBoxLayout()
    prefix_layout.addWidget(QLabel('접두어:'))
    self.prefix_input = QLineEdit()
    prefix_layout.addWidget(self.prefix_input)
    layout.addLayout(prefix_layout)

    suffix_layout = QHBoxLayout()
    suffix_layout.addWidget(QLabel('접미어:'))
    self.suffix_input = QLineEdit()
    suffix_layout.addWidget(self.suffix_input)
    layout.addLayout(suffix_layout)

    # 기존 이름 유지 여부 체크박스
    self.keep_name_checkbox = QCheckBox('기존 파일명 유지')
    self.keep_name_checkbox.setChecked(True)
    layout.addWidget(self.keep_name_checkbox)

    # 실행 버튼
    self.rename_btn = QPushButton('이름 일괄 변경')
    self.rename_btn.clicked.connect(self.rename_files)
    layout.addWidget(self.rename_btn)

    self.setLayout(layout)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, '파일 선택', '', '모든 파일 (*)')
        if files:
            self.file_list.clear()
            self.file_list.addItems(files)
    def rename_files(self):
        files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
        prefix = self.prefix_input.text()
        suffix = self.suffix_input.text()
        keep_name = self.keep_name_checkbox.isChecked()
        def __init__(self):
            super().__init__()
            self.setWindowTitle('파일 일괄 이름 변경기')
            self.resize(600, 400)
            layout = QVBoxLayout()

            # 파일 리스트
            self.file_list = QListWidget()
            layout.addWidget(self.file_list)

            # 파일 선택 버튼
            btn_layout = QHBoxLayout()
            self.select_btn = QPushButton('파일 선택')
            self.select_btn.clicked.connect(self.select_files)
            btn_layout.addWidget(self.select_btn)
            layout.addLayout(btn_layout)

            # 접두어/접미어 입력
            prefix_layout = QHBoxLayout()
            prefix_layout.addWidget(QLabel('접두어:'))
            self.prefix_input = QLineEdit()
            prefix_layout.addWidget(self.prefix_input)
            layout.addLayout(prefix_layout)

            suffix_layout = QHBoxLayout()
            suffix_layout.addWidget(QLabel('접미어:'))
            self.suffix_input = QLineEdit()
            suffix_layout.addWidget(self.suffix_input)
            layout.addLayout(suffix_layout)

            # 기존 이름 유지 여부 체크박스
            self.keep_name_checkbox = QCheckBox('기존 파일명 유지')
            self.keep_name_checkbox.setChecked(True)
            layout.addWidget(self.keep_name_checkbox)

            # 실행 버튼
            self.rename_btn = QPushButton('이름 일괄 변경')
            self.rename_btn.clicked.connect(self.rename_files)
            layout.addWidget(self.rename_btn)

            self.setLayout(layout)


