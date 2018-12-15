import requests
import threading

def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.status_code}')

urls = [
    'http://www.python.org/',
    'http://www.packtpub.com/',
    'http://www.w3resource.com/',
    'http://www.python.org/psf/'
]

if __name__ == '__main__':
    threads = []
    for url in urls:
        thread = threading.Thread(target=ping, args=(url,))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
