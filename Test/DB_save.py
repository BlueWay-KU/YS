import requests
import json
import fire_alarm


while True:
    ID = 2
    node = fire_alarm.alarm()
    print("fire: "+str(node))
    if node !=0:
        DATA = node
    else:
        continue

    data = {"ID":ID,"DATA":DATA}
    r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/saveData.php",params = data)
    print(r.text)
