from youtube_dl import YoutubeDL
from helpers import get_logger

logger = get_logger("u2bdownload")

def download(url):
    """
    This function returns name and download links of given youtube url.
    Args:
        url (string)
    Returns:
        result tuple -> (name -> str, links -> list)
    """
    logger.info(url)
    links = list()
    name = None
    formats = {
                '480p':'18',
                '720p':'136',
              }
    for format_name, format_id in formats.items():
        try:
            options = {
                'format': format_id,
            }
            with YoutubeDL(options) as ydl:
                video = ydl.extract_info(url, download=False)
                download_link = video.get('url')
                if not name:
                    name = video.get('title')
                links.append({format_name: download_link})
        except Exception as e:
            logger.error(f"format id: {format_id}")
            logger.error(e)
    return name, links

if __name__ == "__main__":
    # test
    url = "https://youtube.com/watch?v=YkgkThdzX-8"
    links = download(url)
    for link in links:
        print(link)
        print("\n"*3)
