import IPython
from src.HTMLrenderer.render import render_site


def test_render_site(URL="https://pytorch.org"):
    res = render_site(URL)
    assert isinstance(res, IPython.lib.display.IFrame) == True
