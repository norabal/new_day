import datetime
import glob
import os
import shutil

from norutil.util import adjust_for_expanduser

from exception import FileIsNotExistedError


class Memo:
    def __init__(self, config):
        self.memo_dir = adjust_for_expanduser(config.get('memo', 'memo_dir'))
        self.excel_file = config.get('excel', 'file_name')
        self.excel_dir = adjust_for_expanduser(config.get('excel', 'excel_dir'))
        self.today = datetime.date.today()
        self.new_memo_name = self.today.strftime('%Y%m%d') + '.md'
        self.new_memo_path = os.path.join(self.memo_dir, self.new_memo_name)

    def open_today_memo(self):
        if self.is_exist_today_memo:
            os.system('open ' + self.new_memo_path)
        else:
            raise FileIsNotExistedError("Today's memo is not created yet")

    def copy_memo_from_newest(self):
        """
        The file that has the latest date as name will be copied.
        if no memo file found, first memo file will be created automatically.
        """
        exists = [os.path.basename(r) for r in glob.glob(self.memo_dir + '/*')]
        if not exists:
            self.create_first_memo()

        else:
            lists = sorted(exists, reverse=True)
            source = os.path.join(self.memo_dir, lists[0])
            shutil.copyfile(source, self.new_memo_path)

    def create_first_memo(self):
        with open(self.new_memo_path, 'w') as first_memo:
            first_memo.write('This is your first memo file.')

    def is_exist_today_memo(self):
        return os.path.exists(self.new_memo_path)

    def open_excel(self):
        """ex. this month's attendance excel file"""
        year = self.today.strftime('%Y')
        month = self.today.strftime('%m')
        excel_file = self.excel_file.format(year=year, month=month)
        excel_file_path = os.path.join(self.excel_dir, excel_file)
        if os.path.exists(excel_file_path):
            os.system('open ' + excel_file_path)
        else:
            raise FileIsNotExistedError("This month's excel file is not created yet: {}".format(excel_file_path))
