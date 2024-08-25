from pytubefix import YouTube
from helpers import get_logger

logger = get_logger("pytube_download")


def get_stream_attributes():
    return {
        "type": {"display_name": "Type", "type": str},
        "quality": {"display_name": "Quality", "type": str},
        "format": {"display_name": "Format", "type": str},
        "codec": {"display_name": "Codec", "type": str},
        "filesize_mb": {"display_name": "File Size (MB)", "type": float},
        "url": {"display_name": "URL", "type": "url"},
    }


def parse_streams(streams):
    """
    This function parses all streams from pytube and returns detailed information about each stream.
    Args:
        pytube streams
    Returns:
        result list -> [dict]
    """
    stream_info = []

    for stream in streams:
        info = {
            "type": "Video" if stream.includes_video_track else "Audio",
            "quality": stream.resolution if stream.includes_video_track else stream.abr,
            "format": stream.mime_type.split("/")[-1],
            "codec": stream.video_codec
            if stream.includes_video_track
            else stream.audio_codec,
            "filesize_mb": round(stream.filesize / (1024 * 1024), 2),
            "url": stream.url,
        }

        if stream.is_progressive:
            info["type"] = "Video + Audio"

        stream_info.append(info)

    return stream_info


def get_video_information(url):
    """
    This function returns video information of given URL.

    Args:
        url (string): The URL of the video
    Returns:
        dict: A dictionary containing video information
            {'title': string, 'streams': dict, 'error': string}
    """
    logger.info(f"Getting links for {url}")

    video_information = {"title": None, "streams": {}, "error": None}

    try:
        yt = YouTube(url)
        video_information["title"] = yt.title
        streams = parse_streams(yt.streams)
        if streams:
            video_information["streams"] = streams
        else:
            video_information["error"] = f"No streams found for {url}."
    except Exception:
        logger.exception(f"Exception for {url}")
        video_information["error"] = "Unable to process the given url."

    return video_information


if __name__ == "__main__":
    # test
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    video_information = get_video_information(url)
    title = video_information["title"]
    video_streams = video_information["streams"]
    error = video_information["error"]
    assert title == "Rick Astley - Never Gonna Give You Up (Official Music Video)"
    assert video_streams
    assert not error
