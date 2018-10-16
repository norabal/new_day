import os
import shutil
import unittest

from config import get_config
from definitions import TEST_DIR, TEST_CONFIG_PATH
from memo import Memo
from tests.base import BaseTest
from util import make_empty_dir


class MemoTest(BaseTest):
    test_memo_dir = os.sep.join([TEST_DIR, 'memo'])

    @classmethod
    def setUpClass(cls):
        super(MemoTest, cls).setUpClass()
        make_empty_dir(cls.test_memo_dir)

    def test_create_first_memo(self):
        self.config = get_config(TEST_CONFIG_PATH)
        self.config.set('memo', 'memo_dir', self.test_memo_dir)

        memo = Memo(self.config)
        memo.create_first_memo()
        self.assertTrue(os.path.exists(memo.new_memo_path))

    @classmethod
    def tearDownClass(cls):
        super(MemoTest, cls).tearDownClass()
        shutil.rmtree(cls.test_memo_dir)


if __name__ == "__main__":
    unittest.main()
