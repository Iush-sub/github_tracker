import sys
import requests

def username():
    if len(sys.argv) < 2:
        print("Usage: python test1.py <username>")
    else:
        return sys.argv[1]


def data(username):
    url = "https://api.github.com/users/" + username + "/events"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("data fetch sucessfully")
    else:
        print("Error:", response.status_code)






def main():
        username()

if '__main__' ==  __name__:
    main()
else:
    pass
