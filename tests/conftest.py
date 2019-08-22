from collections import namedtuple
from os import environ
from socket import socket
from subprocess import Popen, PIPE
from sys import executable
from time import monotonic, sleep


import pytest
import requests

Server = namedtuple('Server', ['url', 'process'])


@pytest.fixture
def server(timeout_sec=30):
    port = random_port()
    print(f'\nserver port: {port}')
    env = environ.copy()
    env['NLPD_PORT'] = str(port)

    cmd = [executable, '-m', 'nlp.httpd']
    proc = Popen(cmd, env=env, stdout=PIPE, stderr=PIPE)
    url = f'http://localhost:{port}'
    if not wait_for_server(url + '/health', timeout_sec):
        raise ValueError(f'server did not start after {timeout_sec} seconds')
    yield Server(url, proc)
    proc.kill()


def wait_for_server(url, timeout_sec):
    start = monotonic()
    while monotonic() - start <= timeout_sec:
        try:
            resp = requests.get(url)
            if resp.ok:
                return True
        except requests.ConnectionError:
            continue
        sleep(0.1)
    return False


def random_port():
    with socket() as sock:
        sock.listen(0)
        return sock.getsockname()[1]
