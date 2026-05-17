import requests


payloads = [

    "<script>alert(1)</script>",

    "\"><script>alert(1)</script>",

    "<img src=x onerror=alert(1)>"

]


def scan_xss(url):

    vulnerable_urls = []

    for payload in payloads:

        test_url = url + "?input=" + payload

        try:

            response = requests.get(
                test_url,
                timeout=5
            )

            if payload in response.text:

                vulnerable_urls.append({

                    "url": test_url,

                    "payload": payload,

                    "severity": "Medium"

                })

        except:
            pass

    return vulnerable_urls