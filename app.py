import sys
import requests

def username():
    if len(sys.argv) < 2:
        print("Usage: python test1.py <username>")
    else:
        return sys.argv[1]


def data(username):
    if not username:
        print("Try again")
    else:
        url = "https://api.github.com/users/" + username + "/events"
        response = requests.get(url)

        if response.status_code == 200:
            dat = response.json()
            return dat
        else:
            print("Error:", response.status_code)


def display(value):
    for event in value:
        repo=event.get("repo", {}).get("name")
        task=event.get("type")
        if repo:
            if task == "PushEvent":
                print(repo+"-->User pushed commits")
            elif task == "CreateEvent":
                print(repo + "-->User created repo.")
            elif task == "ForkEvent":
                print(repo + "-->User forked.")






def main():
    value = username()
    dat = data(value)
    if dat:
        display(dat)
    else:
        print("ERROR")


if '__main__' ==  __name__:
    main()
else:
    pass
