import urllib.parse,urllib.error, urllib.request
import config
import json
def fetch():
    username = input("Enter GitHub Username: ")
    url = config.API_URL + username
    try:
        mydata = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        return
    except urllib.error.URLError:
        return
    data = json.loads(mydata)
    return data