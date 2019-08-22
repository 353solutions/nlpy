import requests


def test_nlpd_tokenize(server):
    text = 'Mary had a little lamb'
    url = server.url + '/tokenize'
    resp = requests.post(url, data=text)
    assert resp.ok, f'bad status - {resp.status_code}'
    reply = resp.json()
    assert reply['tokens'] == ['mary', 'little', 'lamb'], 'bad tokenize'
