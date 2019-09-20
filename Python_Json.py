import urllib.request, json

def main():
    #url = "https://jsonplaceholder.typicode.com/photos/1"
    url = "https://jsonplaceholder.typicode.com/photos?albumId=1"
    data = urllib.request.urlopen(url).read()
    jsonData = json.loads(data.decode("utf-8"))
    #print(jsonData)
    for i in jsonData:
        print("Title: {}, Url:{}, Thumbnail:{}".format(i["title"], i["url"], i["thumbnailUrl"]))

if __name__ == '__main__': main()
