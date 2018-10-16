import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.sep.join([ROOT_DIR, 'config.ini'])

TEST_DIR = os.sep.join([ROOT_DIR, 'tests'])
TEST_CONFIG_PATH = os.sep.join([TEST_DIR, 'test_config.ini'])
