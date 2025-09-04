import os

class FileBatchRenamer:
    @staticmethod
    def rename_files(files, prefix, suffix, use_serial=False, serial_start=1, serial_digits=2, keep_name=True):
        renamed = 0
        serial = serial_start
        total = len(files)
        width = serial_digits if serial_digits else len(str(total))
        changed_files = []
        for idx, file_path in enumerate(files):
            dir_name, base = os.path.split(file_path)
            name, ext = os.path.splitext(base)
            serial_str = f"{serial:0{width}d}" if use_serial else ''
            new_name = prefix + (name if keep_name else '') + suffix
            if use_serial:
                new_name = new_name.replace('{OrderNo}', serial_str)
            new_name += ext
            new_path = os.path.join(dir_name, new_name)
            try:
                os.rename(file_path, new_path)
                renamed += 1
                changed_files.append((base, new_name))
            except Exception as e:
                return False, f'오류: {e}', []
            serial += 1
        return True, f'{renamed}개 파일 이름 변경 완료!', changed_files
