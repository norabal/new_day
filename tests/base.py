import unittest

from definitions import TEST_CONFIG_PATH
from util import remove_path_if_exists, copy_config_ini_from_sample


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        remove_path_if_exists(TEST_CONFIG_PATH)
        copy_config_ini_from_sample()

    @classmethod
    def tearDownClass(cls):
        remove_path_if_exists(TEST_CONFIG_PATH)
