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



    # 일련번호 옵션
    serial_layout = QHBoxLayout()
    self.serial_checkbox = QCheckBox('일련번호 추가')
    self.serial_checkbox.setChecked(False)
    serial_layout.addWidget(self.serial_checkbox)
    serial_layout.addWidget(QLabel('시작값:'))
    self.serial_start = QSpinBox()
    self.serial_start.setMinimum(1)
    self.serial_start.setMaximum(99999)
    self.serial_start.setValue(1)
    serial_layout.addWidget(self.serial_start)
    serial_layout.addWidget(QLabel('자릿수:'))
    self.serial_digits = QSpinBox()
    self.serial_digits.setMinimum(1)
    self.serial_digits.setMaximum(6)
    self.serial_digits.setValue(2)
    serial_layout.addWidget(self.serial_digits)
    layout.addLayout(serial_layout)

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
        use_serial = self.serial_checkbox.isChecked()
        serial_start = self.serial_start.value()
        serial_digits = self.serial_digits.value()
        if not files:
            QMessageBox.warning(self, '경고', '파일을 선택하세요.')
            return
        success, msg = FileBatchRenamer.rename_files(
            files, prefix, suffix, use_serial, serial_start, serial_digits
        )
        if success:
            QMessageBox.information(self, '완료', msg)
            self.file_list.clear()
        else:
            QMessageBox.critical(self, '오류', msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileRenamerWindow()
    window.show()
    sys.exit(app.exec())
