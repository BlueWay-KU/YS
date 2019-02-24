import requests
import json

ID = 2 
data = {"ID":ID} 
r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)
#print(r.text)
r.encoding = 'UTF-8'
Data = json.loads(r.text)

print(Data)
length = len(Data)
print(length)

print(Data[length-1]['ID']+" // "+Data[length-1]['DATA']) 
