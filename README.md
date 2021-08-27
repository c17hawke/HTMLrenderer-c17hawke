# HTMLrenderer-c17hawke
A small package for rendering HTML pages in jupyter notebooks

# How to use -

run below snippet of code -

## default use case -
```python
from HTMLrenderer.render import render_site

URL="use your https URL here"
render_site(URL)
```

## custom use case -
```python
from HTMLrenderer.render import render_site

URL="use your https URL here"
render_site(URL, width="100%", height=600)
```
