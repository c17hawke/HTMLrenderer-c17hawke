from IPython.display import IFrame

def render_site(URL, width="100%", height=600):
  return IFrame(src=URL, width=width, height=height)