from IPython import display
from ensure import ensure_annotations
import urllib.request
from HTMLrenderer.custom_exception import InvalidURLException
from HTMLrenderer.logger import logger


@ensure_annotations
def get_id_and_start_time(URL: str) -> tuple:
    """get youtube video id

    Args:
        URL (str, optional): youtube URL. Defaults to None.

    Returns:
        str: video id
    """

    def _verify_vid_id_len(vid_id, __expected_vid_id_len=11):
        len_of_vid_id = len(vid_id)
        if len_of_vid_id != __expected_vid_id_len:
            raise InvalidURLException(
                f"Invalid video id with length: {len_of_vid_id}, expected {__expected_vid_id_len}"
            )

    logger.info(f"input URL: {URL}")
    split_val = URL.split("=")
    if "watch" in URL:
        if "&t" in URL:
            vid_id, time = split_val[-2][:-2], split_val[-1][:-1]
            _verify_vid_id_len(vid_id)
            logger.info(
                f"vid id: {vid_id}, and starts at: {time}, len of video id: {len(vid_id)}"
            )
            return vid_id, time
        else:
            vid_id, time = split_val[-1], "0"
            _verify_vid_id_len(vid_id)
            logger.info(
                f"vid id: {vid_id}, and starts at: {time}, len of video id: {len(vid_id)}"
            )
            return vid_id, time
    vid_id, time = URL.split("/")[-1], "0"
    _verify_vid_id_len(vid_id)
    logger.info(
        f"vid id: {vid_id}, and starts at: {time}, len of video id: {len(vid_id)}"
    )
    return vid_id, time


@ensure_annotations
def error_playing_video(
    URL: str,
    pattern: str = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"',
) -> bool:
    request = urllib.request.urlopen(URL)
    return pattern in str(request.read())


@ensure_annotations
def render_YouTube_video(URL: str, width: int = 780, height: int = 600):
    """render Youtube videos in notebook

    Args:
        URL (str, optional): Youtube video links. Defaults to None.
        width (int, optional): width of the Youtube video to render. Defaults to 780.
        height (int, optional): height of the Youtube video to render. Defaults to 600.
    Raises:
        e: Exception if youtube link is not valid
    """
    try:
        any_error = error_playing_video(URL)
        vid_ID, time = get_id_and_start_time(URL)
        embed_URL = f"https://www.youtube.com/embed/{vid_ID}?start={time}"
        any_error = error_playing_video(embed_URL)
        if URL is None:
            raise InvalidURLException("URL is None")
        elif not any_error:
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
            display.display(display.HTML(iframe))
            return "success"
    except Exception as e:
        raise e
