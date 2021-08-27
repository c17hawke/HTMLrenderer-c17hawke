from IPython.display import IFrame

def render_site(URL, width=700, height=600):
  return IFrame(src=URL, width="100%", height=600)