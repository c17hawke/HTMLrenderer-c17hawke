# HTMLrenderer-c17hawke
A small package for rendering HTML pages in jupyter notebooks

# How to use -

* install the latest package 

> * in jupyter notebook -
```
    !pip install HTMLrenderer
```

> * in command prompt -
```bash    
    pip install HTMLrenderer
```

* Now run below snippets of code in your jupyter-notebooks cell to render your website as an IFrame-

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
