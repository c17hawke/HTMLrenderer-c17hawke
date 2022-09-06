import pytest
from HTMLrenderer import is_valid


URL_test_data = [
    ("http://pytorch.org", True),
    ("https://pytorch.org", True),
    ("http://pytorch", False),
    ("http//pytorch", False),
    ("http:/pytorch", False),
    ("http/pytorch", False),
    ("http/pytorch", False),
    ("pytorch.org", False),
]


@pytest.mark.order(2)
@pytest.mark.parametrize("URL, response", URL_test_data)
def test_is_valid(URL, response):
    assert is_valid(URL) == response
