# American Airlines scraper in Python

## Overview
This project is an open-source tool developed in Python for extracting product information from American Airlines. It's designed to be easy to use, making it an ideal solution for developers looking for American Airlines product data.

## Features
- Full search support
- Extracts detailed product information from American Airlines
- Implemented in Python just because it's popular
- Easy to integrate with existing Python projects

### Install

```bash
$ pip install pyaair
```
## Examples

```Python
fromDir="miami"
toDir="texas"
airports1=pyaair.airports(fromDir,"")
airports2=pyaair.airports(toDir,"")
f = open("./airports1.json", "w")
f.write(json.dumps(airports1))
f.close()
f2 = open("./airports2.json", "w")
f2.write(json.dumps(airports2))
f2.close()
```

```Python
originAirport = "GYE"
destinationAirport = "MIA"
departDate = "2024-05-01"
returnDate = "2024-05-04"
passengers = 1
#locale: where you are located, probably for increasing the price or is just for statistics, I DON'T KNOW, do not say that I said this field is for incresing the price, it's jut a theory
locale = "es_EC" 
flights=pyaair.flights(locale, originAirport, destinationAirport, departDate, returnDate, passengers,"")
f2 = open("./flights.json", "w")
f2.write(json.dumps(flights))
f2.close()
```

```Python
fromDir = "new york"
toDir = "galapagos"
departDate = "2024-05-01"
returnDate = "2024-05-04"
passengers = 1
#locale: where you are located, probably for increasing the price or is just for statistics, I DON'T KNOW, do not say that I said this field is for incresing the price, it's jut a theory
locale = "es_EC" 
airports1=pyaair.airports(fromDir,"")
airports2=pyaair.airports(toDir,"")
flights=pyaair.flights(locale, airports1[0]["code"], airports2[0]["code"], departDate, returnDate, passengers,"")
f2 = open("./flights.json", "w")
f2.write(json.dumps(flights))
f2.close()
```
