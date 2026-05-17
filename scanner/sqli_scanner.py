import requests


payloads = [

    "'",

    "' OR '1'='1",

    "\" OR \"1\"=\"1",

    "'--",

    "' OR 1=1--"

]


errors = [

    "sql syntax",

    "mysql",

    "syntax error",

    "unclosed quotation",

    "sqlite",

    "oracle"

]


def scan_sqli(url):

    vulnerable_urls = []

    for payload in payloads:

        test_url = url + "?id=" + payload

        try:

            response = requests.get(
                test_url,
                timeout=5
            )

            response_text = response.text.lower()

            for error in errors:

                if error in response_text:

                    vulnerable_urls.append({

                        "url": test_url,

                        "payload": payload,

                        "severity": "Critical"

                    })

                    break

        except:
            pass

    return vulnerable_urls