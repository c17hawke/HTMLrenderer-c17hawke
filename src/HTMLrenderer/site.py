from IPython import display
from ensure import ensure_annotations
import urllib.request
from HTMLrenderer.custom_exception import InvalidURLException
from HTMLrenderer.logger import logger


@ensure_annotations
def is_valid(URL: str) -> bool:
    """Checks existence of a valid URL

    Args:
        URL (str): input URL

    Returns:
        bool: boolean existence of the URL
    """
    try:
        response_status = urllib.request.urlopen(URL).getcode()
        assert response_status == 200
        logger.debug(f"response_status: {response_status} OK")
        return True
    except Exception as e:
        logger.exception(e)
        return False


@ensure_annotations
def render_site(URL: str, width: str = "100%", height: str = "600") -> str:
    """renders site in the notebook

    Args:
        URL (str): input URL
        width (str, optional): width in percentage. Defaults to "100%".
        height (str, optional): height in nums. Defaults to "600".

    Raises:
        InvalidURLException: if URL is not is_valid
        e: other exceptions

    Returns:
        str: "success if site rendered"
    """
    try:
        if is_valid(URL):
            response = display.IFrame(src=URL, width=width, height=height)
            display.display(response)
            return "success"
        else:
            raise InvalidURLException
    except Exception as e:
        raise e
