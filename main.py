from kivy.app import App
from ui import FileRenamer

class FileRenamerApp(App):
    def build(self):
        return FileRenamer()

if __name__ == '__main__':
    FileRenamerApp().run()
