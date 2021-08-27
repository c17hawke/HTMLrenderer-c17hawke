from IPython.display import IFrame, display, Markdown, Latex, HTML

def render_site(URL=None, width="100%", height="600"):
    """Renders HTML in the jupyter notebook

    Args:
        URL (str): URL of site to render in jupyter notebook. Defaults to None.
        width (str, optional): width of the html page to render_site. Defaults to "100%".
        height (str, optional): height of the html page to render. Defaults to 600.

    Returns:
        None
    """
    try:
        if URL is not None:
            display(IFrame(src=URL, width=width, height=height))
        else:
            print("pass valid URL!!")
    except Exception as e:
        raise e


def get_id(URL):
    return URL.split('/')[-1]

def render_YouTube_video(URL=None, width=780, height=600):
    try:
        if URL is not None:
            vid_ID = get_id(URL)
            iframe = f"""<iframe 
            width="{width}" height="{height}" 
            src="https://www.youtube.com/embed/{vid_ID}" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; clipboard-write; 
            encrypted-media; gyroscope; 
            picture-in-picture" allowfullscreen>
            </iframe>"""
            display(HTML(iframe))
        else:
            print("pass valid URL!!")
    except Exception as e:
        raise e

def render_Latex(LATEX=None):
    try:
        if LATEX is not None:
            display(Latex(LATEX))
        else:
            print("pass valid LATEX syntax!!")
    except Exception as e:
        raise e


def render_HTML(html=None):
    try:
        if html is not None:
            display(HTML(html))
        else:
            print("pass valid HTML syntax!!")
    except Exception as e:
        raise e

def render_URL(URL=None, Name=None):
    try:
        if (URL is not None):
          if (Name is not None):
            html = f"""<h3><a href="{URL}" target="_blank">{Name}</a></h3>"""
          else:
            html = f"""<h3><a href="{URL}" target="_blank">external link</a></h3>"""
            render_HTML(html=html)
        else:
            print("print valid URL!!")
    except Exception as e:
        raise e

def render_Markdown(markdown=None):
    try:
        if markdown is not None:
            display(Markdown(markdown))
        else:
            print("pass valid markdown syntax!!")
    except Exception as e:
        raise e