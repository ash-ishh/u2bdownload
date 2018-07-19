from youtube_dl import YoutubeDL

def download(url):
    links = []
    formats = [134,136]
    try:
        for i in formats:
            with YoutubeDL({'format':str(i)}) as ydl:
                r = ydl.extract_info(url,download=False)
                links.append(r['url'])
    except Exception as e:
        print(e)
    return links

if __name__ == "__main__":
    url = input()
    links = download(url)
