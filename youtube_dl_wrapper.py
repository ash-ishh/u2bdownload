from youtube_dl import YoutubeDL
from helpers import get_logger

logger = get_logger("u2bdownload")


def parse_video_urls(formats):
    """
    This function parses format dict of Youtube DL and  returns allowed video URLs as value with custom format name as key.
    Args:
        _formats (dict)
    Returns:
        result dict -> {format -> string: url -> string}
    """

    allowed_video_formats = ['360p', '480p', '720p', '1080p']
    video_urls = {}

    for _format in formats:
        format_id = _format.get('format_id')
        format_note = _format.get('format_note')
        height = _format.get('height')
        width = _format.get('width')
        ext = _format.get('ext')
        url = _format.get('url')
        acodec = _format.get('acodec')
        vcodec = _format.get('vcodec')

        if format_note in allowed_video_formats and acodec.lower() != 'none':
            # if format code is allowed and sound encoder exists for it
            format_name = f"{format_note} {ext.upper()} ({width}x{height}) - {vcodec.upper()}"
            video_urls[format_name] = url

    return video_urls


def get_video_information(url):
    """
    This function returns video information of given URL.
    Right now only video extraction is supported and returned.

    Args:
        url (string)
    Returns:
        result dict -> {'title'-> string, 'video_urls' -> dict, 'error_message' -> string}
    """
    logger.info(f"Getting links for {url}")

    options = {}
    video_information = {'title': None, 'video_urls': {}, 'error_message': None}
    title = None

    with YoutubeDL(options) as ydl:
        try:
            video = ydl.extract_info(url, download=False)
        except Exception as e:
            logger.error(f"{url} - {e}")
            video_information['error_message'] = f'Unable to fetch information for {url}'
            return video_information
    title = video.get('title')
    video_information['title'] = title
    formats = video['formats']
    video_urls = parse_video_urls(formats)
    video_information['video_urls'] = video_urls
    return video_information

if __name__ == "__main__":
    # test
    url = "https://www.youtube.com/watch?v=dQw4w9WgXc"
    video_information = get_video_information(url)
    title = video_information['title']
    video_urls = video_information['video_urls']
    error = video_information['error_message']
    print(title)
    print(video_urls)
    print(error)