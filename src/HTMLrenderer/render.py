from IPython.display import IFrame

def render_site(URL, width="100%", height="600"):
  """Renders HTML in the jupyter notebook

  Args:
      URL (str): URL of site to render in jupyter notebook
      width (str, optional): width of the html page to render_site. Defaults to "100%".
      height (str, optional): height of the html page to render. Defaults to 600.

  Returns:
      IFrame: Renders HTML in the jupyter notebook
  """
  return IFrame(src=URL, width=width, height=height)