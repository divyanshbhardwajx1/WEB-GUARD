import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def crawl(url):

    urls = []

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10,
            verify=False
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for link in soup.find_all("a"):

            href = link.get("href")

            if href:

                full_url = urljoin(url, href)

                if full_url.startswith("http"):

                    urls.append(full_url)

    except Exception as e:

        print("\n[CRAWLER ERROR]")
        print(e)

    return list(set(urls))