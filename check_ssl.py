import subprocess


def check_ssl_expire_date(config):
    """
    Check when SSL's validation will be expired.
    :param config: configuration file
    :return: expire datetime
    """
    domains = config.get('ssl', 'target_domains').split(',')
    for d in domains:
        string = "openssl s_client -connect {domain}:443 < /dev/null 2> /dev/null | openssl x509 -text " \
                 "| grep 'Not After'"
        command = string.format(domain=d)
        expire_datetime = subprocess.getoutput(command).replace('Not After : ', '').strip()
        print('SSL of {} will be expired at "{}"'.format(d, expire_datetime))
