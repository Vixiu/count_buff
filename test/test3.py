import os

with open(rf'{os.getenv("APPDATA")}/count-buff/data.json', "r") as f:
    data = eval(f.read())
    print(type(data))