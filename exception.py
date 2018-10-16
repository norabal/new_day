class MemoError(Exception):
    """Base error class"""


class FileIsNotExistedError(MemoError):
    """Expected file did not existed"""
