import urllib.parse,urllib.error, urllib.request
import config
import json
def fetch():
    username = input("Enter GitHub Username: ")
    url = config.API_URL + username
    try:
        user_data = urllib.request.urlopen(url).read()
        repo_data = urllib.request.urlopen(url+"/repos").read()
    except urllib.error.HTTPError:
        return
    except urllib.error.URLError:
        return
    r_data = json.loads(repo_data)
    u_data = json.loads(user_data)
    return u_data,r_data