import requests
import zipfile
import sys
import io
import os

class colours:
    header = "\033[95m"
    blue = "\033[94m"
    cyan = "\033[96m"
    green = "\033[92m"
    warn = "\033[93m"
    error = "\033[91m"
    end = "\033[0m"
    bold = "\033[1m"
    underline = "\033[4m"

argsIndexIncrement = 0

def clone(args):
    url = args[2 + argsIndexIncrement]
    dir = ""

    if len(args) >= 4:
        dir = args[3 + argsIndexIncrement]

    if url.startswith("https://") == False:
        url = "https://" + url

    try:
        r = requests.get(url + "/archive/refs/heads/main.zip")
        if r.headers['Content-Type'] != 'application/zip':
            raise Exception("Not a valid zip file")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        if dir != "":
            z.extractall(dir)
        else:
            z.extractall(url.split("github.com/")[1].split("/")[0])
        print(f"{colours.green}cloned repository successfully{colours.end}")
    except Exception as err:
        print(f"{colours.error}pit encountered an error\n[ clone {err} ]\nplease report this at:\nhttps://github.com/camelCasing/pit/issues{colours.end}")

args = sys.argv

try:
    if args[1 + argsIndexIncrement] == "clone":
        clone(args)
    elif args[1 + argsIndexIncrement] == "help":
        print(f"{colours.green}pit,{colours.end}a python implementation of git.\n\npit help\npit clone <repo-url> <output>")
except Exception as err:
    print(f"{colours.error}pit encountered an error\n[ main {err} ]\nplease report this at:\nhttps://github.com/camelCasing/pit/issues{colours.end}")
