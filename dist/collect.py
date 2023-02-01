from re import T
from time import sleep
import win32clipboard
import pandas as pd

coloumns = ["HP","ATK","DEF","SPA","SPD","SPE"]

finaldata = []


def getdata():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if "IVs" in data:
            return data
    except:
        return None

current =  getdata()



while True:
    t = getdata()
    if current != t and t != None and "ivs" in t.lower():
        line = t.split("\n")[5]
        print(line)
        line = line.split(" ")
        finaldata.append([int(line[1]),int(line[4]),int(line[7]),int(line[10]),int(line[13]),int(line[16])])
        df = pd.DataFrame(finaldata,columns=coloumns)
        df.to_csv("./dist/chansey.csv")
        current = t
    sleep(1)