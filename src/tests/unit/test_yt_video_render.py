import pytest
from HTMLrenderer import get_id_and_start_time
from HTMLrenderer.custom_exception import InvalidURLException



URL_id_good_data = [
    ("https://youtu.be/roO5VGxOw2s", ("roO5VGxOw2s", "0")),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s", ("roO5VGxOw2s", "0")),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", ("roO5VGxOw2s", "42")),
]

URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"), # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"), # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"), # exception
]


@pytest.mark.parametrize("URL, response", URL_id_good_data)
def test_get_id_and_start_time(URL, response):
    assert get_id_and_start_time(URL) == response

@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_id_and_start_time_failed(URL):
    with pytest.raises(InvalidURLException):
        get_id_and_start_time(URL)

