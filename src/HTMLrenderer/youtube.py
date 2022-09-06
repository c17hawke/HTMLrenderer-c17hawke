from IPython import display
from ensure import ensure_annotations
from HTMLrenderer.custom_exception import InvalidURLException
from HTMLrenderer.logger import logger
from py_youtube import Data


@ensure_annotations
def get_id_and_start_time(URL: str) -> int:
    """returns video id and start time of youtube URL

    Args:
        URL (str): input youtube URL

    Returns:
        int: start time in seconds
    """
    def _verify_vid_id_len(vid_id, __expected_vid_id_len=11):
        len_of_vid_id = len(vid_id)
        if len_of_vid_id != __expected_vid_id_len:
            raise InvalidURLException(
                f"Invalid video id with length: {len_of_vid_id}, expected {__expected_vid_id_len}"
            )
    logger.info(f"input URL: {URL}")
    try:
        split_val = URL.split("=")
        if "watch" in URL:
            if "&t" in URL:
                vid_id, time = split_val[-2][:-2], int(split_val[-1][:-1])
                _verify_vid_id_len(vid_id)
                logger.info(
                    f"video starts at: {time}"
                )
                return time
            else:
                vid_id, time = split_val[-1], 0
                _verify_vid_id_len(vid_id)
                logger.info(
                    f"vid starts at: {time}"
                )
                return time
        vid_id, time = URL.split("/")[-1], 0
        _verify_vid_id_len(vid_id)
        logger.info(
            f"vid starts at: {time}"
        )
        return time
    except Exception:
        raise InvalidURLException


@ensure_annotations
def render_YouTube_video(URL: str, width: int = 780, height: int = 600):
    try:
        if URL is None:
            raise InvalidURLException("URL is None")
        data = Data(URL).data()
        if data["publishdate"] is not None:
            time = get_id_and_start_time(URL)
            vid_ID = data["id"]
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
            display.display(display.HTML(iframe))
            return "success"
        else:
            raise InvalidURLException("URL is not valid, Kindly verify")
    except Exception as e:
        raise e
