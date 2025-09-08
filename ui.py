from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QListWidget, QMessageBox, QCheckBox
)
import os

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

        # 접두어 입력
        prefix_layout = QHBoxLayout()
        prefix_layout.addWidget(QLabel('접두어:'))
        self.prefix_input = QLineEdit()
        prefix_layout.addWidget(self.prefix_input)
        layout.addLayout(prefix_layout)

        # 접미어 입력
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

        if not files:
            QMessageBox.warning(self, "경고", "파일을 선택하세요.")
            return

        total_files = len(files)
        order_width = len(str(total_files))  # 자리수 계산

        renamed_files = []
        for idx, file_path in enumerate(files, 1):
            dir_name, base_name = os.path.split(file_path)
            name, ext = os.path.splitext(base_name)
            if keep_name:
                new_name = f"{prefix}{name}{suffix}{ext}"
            else:
                new_name = f"{prefix}{suffix}{ext}"
            if "{OrderNo}" in new_name:
                order_str = str(idx).zfill(order_width)
                new_name = new_name.replace("{OrderNo}", order_str)
            new_path = os.path.join(dir_name, new_name)
            try:
                os.rename(file_path, new_path)
                renamed_files.append(new_path)
            except Exception as e:
                QMessageBox.warning(self, "오류", f"파일 이름 변경 실패: {file_path}\n{e}")

        # 변경된 파일 목록 보여주기
        if renamed_files:
            msg = "변경된 파일 목록:\n" + "\n".join(renamed_files)
            QMessageBox.information(self, "완료", msg)
            self.file_list.clear()
            self.file_list.addItems(renamed_files)