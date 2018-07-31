from youtube_dl import YoutubeDL

def download(url):
    links = []
    formats = [18,22]
    name = None
    try:
        for i in formats:
            with YoutubeDL({'format':str(i)}) as ydl:
                r = ydl.extract_info(url,download=False)
                links.append((i,r['url']))
                name = r.get('title',None)
    except Exception as e:
        print(e)
    return (name,links)

if __name__ == "__main__":
    url = input()
    links = download(url)
    for link in links:
        print(link)
        print("\n"*3)
