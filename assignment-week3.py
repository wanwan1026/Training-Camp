#抓取網頁原始碼(HTML)
import urllib.request as req
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
#建立一個Request物件,附加Headers的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import json
data=json.loads(data)
data=data["result"]["results"]
for i in range(len(data)):
    stitle=data[i]["stitle"]
    longitude=data[i]["longitude"]
    latitude=data[i]["latitude"]
    file=data[i]["file"]
    file=file[file.rfind('www'):]
    # print(stitle,longitude,latitude,file)
    fp=open('data.txt','a',encoding="utf-8")
    fp.writelines(stitle)
    fp.writelines(",")
    fp.writelines(longitude)
    fp.writelines(",")
    fp.writelines(latitude)
    fp.writelines(",")
    fp.writelines(file)
    fp.writelines("\n")
    fp.close()