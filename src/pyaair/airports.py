import requests
import json
from urllib.parse import urlencode, quote_plus


def airports(search_text: str, proxy_url: str):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    params = {
        "searchText": search_text,
        "onlyAirportsIfNotNull": "false"
    }
    query_string = urlencode(params, quote_via=quote_plus)
    full_url = f"https://www.aa.com/home/ajax/airportLookup?{query_string}"
    
    response = requests.get(full_url, headers=headers, proxies=proxies)
    response.raise_for_status()
    data = json.loads(response.text)
    return data