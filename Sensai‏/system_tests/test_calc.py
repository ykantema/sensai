import pytest
import requests

baseurl = "127.0.0.1:5000/"


def test_add():
    res = requests.get(url='http://{0}add?x=1&y=2'.format(baseurl))
    assert(res.text == '3')
