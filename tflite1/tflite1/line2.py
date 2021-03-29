import requests
from datetime import datetime
from datetime import date
now = datetime.now()
date_time = now.strftime("%d/%m/%Y")
hour = now.strftime("%H:%M:%S")
text = "ตรวจพบอาวุธปืน" +' วันที่ :'+ date_time + '\n'+ ' เวลา :'+ hour
exp="%d-%m-%Y-%H:%M:%S"
LINE_ACCESS_TOKEN="5AuKDGZxLD3D6H4sdVR12K8TarVeyckS3Tws6Zv192M"
url = "https://notify-api.line.me/api/notify"
file = {'imageFile':open('images/get.jpg','rb')}
data = ({
        'message': text
    })
LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
r=session.post(url, headers=LINE_HEADERS, files=file, data=data)
print(r.text)