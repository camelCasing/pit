import requests
import zipfile
import sys
import os

class colours:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    warn = '\033[93m'
    error = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def clone(url):
    url = str(url).replace("github.com", "api.github.com/repos")
    request = requests.get(url)

    try:
        repo = request.json()
        cloned = repo["clone_url"]
        name = repo["name"]

        request = requests.get(url, "/zipball")

        f = open(os.getcwd()+f"/{name}.zip", "wb")
        f.write(request.content)

        if os.path.exists(os.getcwd()+f"/{name}") == False:
            os.mkdir(os.getcwd()+f"/{name}")

        zipf = zipfile.ZipFile(os.getcwd()+f"/{name}.zip", "r")
        zipf.extractall(os.getcwd()+f"/{name}")

        print(f"{colours.green}Successfully{colours.end} cloned {name} to {os.getcwd()+f}/{name}")


    except Exception as err:
        print(err)
# https://api.github.com/repos/username/repo
def main(args):
    try:
        if args[1] == "clone":
            clone(args[2])
    except Exception as err:
        pass

clone("https://github.com/camelCasing/pit")
