from IPython.display import IFrame, display, Markdown, Latex, HTML
from ensure import ensure_annotations
import urllib.request
from HTMLrenderer.custom_exception import InvalidURLException
from HTMLrenderer.logger import logger

@ensure_annotations
def is_valid(URL: str) -> bool:
    try:
        response_status = urllib.request.urlopen(URL).getcode()
        print(f"response_status: {response_status} OK")
        assert response_status == 200
        return True
    except Exception as e:
        return False


@ensure_annotations
def render_site(
    URL: str = None, width: str = "100%", height: str = "600", source: bool = True
) -> str:
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
            if source:
                print("\n")
                render_URL(URL=URL, Name="Source: click here to open in new tab")
                print("\n")
            return "success"
        else:
            raise InvalidURLException
    except Exception as e:
        raise e


@ensure_annotations
def get_id_and_start_time(URL: str = None) -> tuple:
    """get youtube video id

    Args:
        URL (str, optional): youtube URL. Defaults to None.

    Returns:
        str: video id
    """
    logger.info(f"input URL: {URL}")
    split_val = URL.split("=")
    if "watch" in URL:
        if "&t" in URL:
            
            vid_id, time = split_val[-2][:-2],split_val[-1][:-1] 
            logger.info(f"vid id: {vid_id}, and starts at: {time}")
            return vid_id, time
        else:
            vid_id, time = split_val[-1], "0"
            logger.info(f"vid id: {vid_id}, and starts at: {time}")
            return vid_id, time
    vid_id, time = URL.split("/")[-1], "0"
    logger.info(f"vid id: {vid_id}, and starts at: {time}")
    return vid_id, time



@ensure_annotations
def try_video(URL: str = None, pattern: str='"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"') -> bool:
    request = urllib.request.urlopen(URL)
    return pattern in str(request.read())


@ensure_annotations
def render_YouTube_video(URL: str = None, width: int = 780, height: int = 600):
    """render Youtube videos in notebook

    Args:
        URL (str, optional): Youtube video links. Defaults to None.
        width (int, optional): width of the Youtube video to render. Defaults to 780.
        height (int, optional): height of the Youtube video to render. Defaults to 600.
    Raises:
        e: Exception if youtube link is not valid
    """
    try:
        URL_not_accessible = try_video(URL)
        if URL_not_accessible:
            raise InvalidURLException("URL is not accessible")
        if URL is None:
            raise InvalidURLException("URL is None")
        else:
            vid_ID, time = get_id_and_start_time(URL)
            embed_URL = f"https://www.youtube.com/embed/{vid_ID}?start={time}"
            logger.info(f"embed_URL: {embed_URL}")
            iframe = f"""<iframe 
            width="{width}" height="{height}" 
            src="{embed_URL}" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; clipboard-write; 
            encrypted-media; gyroscope; 
            picture-in-picture" allowfullscreen>
            </iframe>"""
            display(HTML(iframe))
            # return IFrame(iframe, width=width, height=height)
    except Exception as e:
        raise e


@ensure_annotations
def render_Latex(LATEX: str = None):
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
def render_HTML(html: str = None):
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
def render_URL(URL: str = None, Name: str = None):
    """render URL in notebook

    Args:
        html (str, optional): URL in string format. Defaults to None.

    Raises:
        e: raise exception if URL input is not valid
    """
    try:
        if URL is not None:
            if Name is not None:
                html = f"""<h3><a href="{URL}" target="_blank">{Name}</a></h3>"""
            else:
                html = f"""<h3><a href="{URL}" target="_blank">external link</a></h3>"""
                return render_HTML(html=html)
        else:
            print("print valid URL!!")
    except Exception as e:
        raise e


@ensure_annotations
def render_Markdown(markdown: str = None):
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
