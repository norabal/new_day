from norutil.config import get_config

from check_ssl import check_ssl_expire_date
from definitions import CONFIG_PATH
from exception import MemoError
from memo import Memo
from twitter import get_twitter


def _main():
    config = get_config(CONFIG_PATH)

    check_ssl_expire_date(config)

    get_twitter(config)

    memo = Memo(config)

    if memo.is_exist_today_memo():
        print("Today's memo file has been created already.")
    else:
        print("Today's memo file does not exist.\n"
              "The latest memo will be copied.")
        try:
            memo.copy_memo_from_newest()
        except MemoError as err:
            print('Failed to copy memo file: {}'.format(err))
            exit(1)

        print("Did you fill out yesterday's attendance?")
        memo.open_excel()

    memo.open_today_memo()
    exit(0)


if __name__ == '__main__':
    _main()
