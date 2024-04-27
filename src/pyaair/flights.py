import requests

def flights(locale:str, originAirport:str, destinationAirport:str, departDate:str, returnDate:str, passengers: int, proxy_url:str):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en",
        "Content-Type": "application/json",
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
    inputData ={
        "metadata":{
            "tripType":"RoundTrip",
            "udo":{
                "search_method":"Lowest",
            },
        },
        "passengers":[
            {"type":"adult","count": passengers},
        ],
        "requestHeader":{
            "clientId": "AAcom",
        },
        "slices":[
            {"allCarriers":True,"departureDate":departDate,"destination":destinationAirport,"origin":originAirport},
            {"allCarriers":True,"departureDate":returnDate,"destination":originAirport,"origin":destinationAirport},
        ],
        "tripOptions":{"fareType":"Lowest","locale":locale,"searchType":"Revenue"},
        "queryParams": {"sliceIndex": 0,"sessionId": "", "solutionSet": "", "solutionId": ""},
        "loyaltyInfo": None,
        "version":""
    }
    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    response = requests.post("https://www.aa.com/booking/api/search/itinerary", json = inputData, headers=headers, proxies=proxies)
    data = response.json()
    return data