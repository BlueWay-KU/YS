import requests
import json

ID = 1
data = {"ID":ID} 
r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)
#print(r.text)

r.encoding = 'UTF-8'
Data = json.loads(r.text)

print(Data)
length = len(Data)

print(Data[length]['ID']+" // "+Data[length]['DATA']) 
