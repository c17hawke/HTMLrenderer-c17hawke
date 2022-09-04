import IPython
from IPython.display import IFrame, display, Markdown, Latex, HTML
from ensure import ensure_annotations
import urllib.request

min_attributes = ('scheme', 'netloc')

@ensure_annotations
def is_valid(URL: str) -> bool:
    try:
        response_status = urllib.request.urlopen(URL).getcode()
        print(f"response_status: {response_status} OK")
        assert response_status == 200
        return True
    except Exception as e:
        return False

class InvalidURLException(Exception):
    def __init__(self, message: str="URL is not valid"):
        self.message = message
        super().__init__(self.message)


@ensure_annotations
def render_site(URL: str=None, width: str="100%", height: str="600", source: bool=True):
    """Renders HTML in the jupyter notebook

    Args:
        URL (str): URL of site to render in jupyter notebook. Defaults to None.
        width (str, optional): width of the html page to render_site. Defaults to "100%".
        height (str, optional): height of the html page to render. Defaults to 600.

    Returns:
        None
    """
    try:
        if is_valid(URL):
            response = IFrame(src=URL, width=width, height=height)
            display(response)
        else:
            raise InvalidURLException
        if source:
            print("\n")
            render_URL(URL=URL, Name="Source: click here to open in new tab")
            print("\n")
            
        else:
            raise InvalidURLException("URL is None. Enter a valid URL")
    except Exception as e:
        raise e

@ensure_annotations
def get_id(URL: str=None) -> str:
    """get youtube video id

    Args:
        URL (str, optional): youtube URL. Defaults to None.

    Returns:
        str: video id
    """
    if "watch" in URL:
        return URL.split("=")[-1]
    return URL.split('/')[-1]

@ensure_annotations
def render_YouTube_video(URL: str=None, width: int=780, height: int=600):
    """render Youtube videos in notebook

    Args:
        URL (str, optional): Youtube video links. Defaults to None.
        width (int, optional): width of the Youtube video to render. Defaults to 780.
        height (int, optional): height of the Youtube video to render. Defaults to 600.
    Raises:
        e: Exception if youtube link is not valid
    """
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

@ensure_annotations
def render_Latex(LATEX: str=None):
    """render latex docs in notebook

    Args:
        LATEX (str, optional): LATEX content. Defaults to None.

    Raises:
        e: Exception if latex code is not valid
    """
    try:
        if LATEX is not None:
            display(Latex(LATEX))
        else:
            print("pass valid LATEX syntax!!")
    except Exception as e:
        raise e

@ensure_annotations
def render_HTML(html: str=None):
    """render HTML strings

    Args:
        html (str, optional): HTML like strings. Defaults to None.

    Raises:
        e: raise exception is HTML input is not valid
    """
    try:
        if html is not None:
            display(HTML(html))
        else:
            print("pass valid HTML syntax!!")
    except Exception as e:
        raise e

@ensure_annotations
def render_URL(URL: str=None, Name: str=None):
    """render URL in notebook

    Args:
        html (str, optional): URL in string format. Defaults to None.

    Raises:
        e: raise exception if URL input is not valid
    """
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

@ensure_annotations
def render_Markdown(markdown: str=None):
    """render markdown like strings

    Args:
        markdown (str, optional): markdown as strings. Defaults to None.

    Raises:
        e: if not a valid markdown syntax
    """
    try:
        if markdown is not None:
            display(Markdown(markdown))
        else:
            print("pass valid markdown syntax!!")
    except Exception as e:
        raise e
