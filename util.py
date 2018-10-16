import os
import shutil

from definitions import ROOT_DIR, TEST_CONFIG_PATH


def adjust_for_expanduser(dir_path):
    """replace '~' as $HOME path for python os module"""
    if dir_path.startswith('~/'):
        return dir_path.replace('~', os.path.expanduser('~'), 1)
    else:
        return dir_path


def remove_path_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        pass


def make_empty_dir(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

    os.mkdir(dir_path)


def copy_config_ini_from_sample():
    """'test_config.ini' will be created from 'config.ini.sample'"""
    source = os.sep.join([ROOT_DIR, 'config.ini.sample'])
    shutil.copyfile(source, TEST_CONFIG_PATH)
