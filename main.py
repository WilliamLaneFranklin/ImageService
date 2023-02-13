import json                                           #for JSON -> Python objects
import requests                                       #HTTP Requests library
import os                                             #checking the file path
import time                                           #for sleep function

def getImgUrl(cityName):
    endPoint = 'https://en.wikipedia.org/w/api.php'   #create wikipedia API endpoint
    jsonParams = {                                    #this will be passed as parameter to the HTTP GET request
        'action': 'query',                            #https://www.mediawiki.org/wiki/API:Data_formats
        'format': 'json',                             #https://www.mediawiki.org/wiki/API:Data_formats
        'formatversion': 2,                           #1 or 2, 2 is the modern one
        'prop': 'pageimages|pageterms',               #https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bpageimages
        'piprop': 'original',                         #URL and original dimensions associated with page if any
        'pilimit': '1',                               #Page return limit 1
        'pilicense': 'free',                          #free images only
        'titles': cityName                            #parameter of Query action see https://www.mediawiki.org/wiki/API:Query
                }

    result = requests.get(endPoint, jsonParams)       #HTTP GET request with predefined parameters and city name passed in
    parsed = json.loads(result.text)                  #json to python objects https://docs.python.org/3/library/json.html#json-to-py-table

    #print(result.content)

    length = len(parsed['query']['pages'])
    if length > 0:
        return parsed['query']['pages'][0]['original']['source'] #you can uncomment print(result.content) above and see the path to get to the url value
    else:
        return ""

def main():
    while True:
        file = open('readIn.txt', 'r+')              #open file read-only
        line = file.readline()

        if (os.path.getsize('readIn.txt') != 0):    #is there something in the file?
            splitLine = line.split(',')             #split city, state or city, country
            city = splitLine[0]                     #city will be at the first index
            file.close()                            #so we can clear file
            fileToClear = open('readIn.txt', 'w')
            fileToClear.close()
            try:
                url = getImgUrl(line)               #1. First try city, state or city, country
                print(url)
            except:
                try:                                #2. second try just the city name
                    url = getImgUrl(city)
                    print(url)
                except:                             #3. third try city name plus ' City',i.e. New York = New York City
                    city = city + ' City'
                    url = getImgUrl(city)
                    print(url)
            file = open('writeOut.txt', 'w')                      #open file thus clearing city, state/city, country
            file.write(url)                                     #write the url to the file
            file.close()
        time.sleep(5)
        print("slept for 5 seconds...")
main()




