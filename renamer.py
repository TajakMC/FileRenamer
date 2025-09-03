import os

class FileBatchRenamer:
    @staticmethod
    def rename_files(files, prefix, suffix):
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
                return False, f'오류: {e}'
        return True, f'{renamed}개 파일 이름 변경 완료!'
