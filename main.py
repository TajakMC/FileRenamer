from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
import os

class FileRenamer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.file_chooser = FileChooserListView(path='/', filters=['*.*'], multiselect=True)
        self.add_widget(self.file_chooser)

        self.prefix_input = TextInput(hint_text='접두어(prefix)', size_hint_y=None, height=40)
        self.add_widget(self.prefix_input)
        self.suffix_input = TextInput(hint_text='접미어(suffix)', size_hint_y=None, height=40)
        self.add_widget(self.suffix_input)

        self.rename_btn = Button(text='이름 일괄 변경', size_hint_y=None, height=50)
        self.rename_btn.bind(on_press=self.rename_files)
        self.add_widget(self.rename_btn)

        self.status_label = Label(text='', size_hint_y=None, height=40)
        self.add_widget(self.status_label)

    def rename_files(self, instance):
        prefix = self.prefix_input.text
        suffix = self.suffix_input.text
        files = self.file_chooser.selection
        if not files:
            self.status_label.text = '파일을 선택하세요.'
            return
        renamed = 0
        for file_path in files:
            dir_name, base = os.path.split(file_path)
            name, ext = os.path.splitext(base)
            new_name = f"{prefix}{name}{suffix}{ext}"
            new_path = os.path.join(dir_name, new_name)
            try:
                os.rename(file_path, new_path)
                renamed += 1
            except Exception as e:
                self.status_label.text = f'오류: {e}'
                return
        self.status_label.text = f'{renamed}개 파일 이름 변경 완료!'

class FileRenamerApp(App):
    def build(self):
        return FileRenamer()

if __name__ == '__main__':
    FileRenamerApp().run()
