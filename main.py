from ui import FileRenamerWindow

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = FileRenamerWindow()
    window.show()
    sys.exit(app.exec())
