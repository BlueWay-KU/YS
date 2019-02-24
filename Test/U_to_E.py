import copy
import random
import requests
import json

def FromWeb(ID):
    data = {"ID":ID} 
    r = requests.get("http://dbwo4011.cafe24.com/KO/KOREA/loadData.php",params = data)

    r.encoding = 'UTF-8'
    Data = json.loads(r.text)

    length = len(Data)

    return Data[length-1]['DATA']

departure_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

departure = '12' # drone location / server

F = FromWeb(2)
fire=str(F) # fire sensor / server

landscape = {

    '1':   {'2':1},
    '2':   {'1':1, '3':1},
    '3':   {'2':1, '4':1},
    '4':   {'3':1, '5':1, '13':1},
    '5':   {'4':1, '6':1},
    '6':   {'5':1, '7':1, '9':1},
    '7':   {'6':1, '8':1},
    '8':   {'7':1},
    '9':   {'6':1, '10':1},
    '10':  {'9':1, '11':1},
    '11':  {'10':1, '12':1},
    '12':  {'11':1},
    '13':  {'4':1}
}

for acc_1,acc_2 in landscape.items():

    for acc_3 in acc_2.keys():

        if acc_3==fire:

            landscape[acc_1][acc_3]=100
routing = {}

for place in landscape.keys():
    routing[place]={'shortestDist':0, 'route': [], 'visited': 0}

def visitPlace(visit):

    routing[visit]['visited'] = 1

    for toGo, betweenDist in landscape[visit].items():

        toDist = routing[visit]['shortestDist'] + betweenDist

        if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:

            routing[toGo]['shortestDist'] = toDist

            routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])

            routing[toGo]['route'].append(visit)

def UtoE():
    visitPlace(departure)

    exit_dis=100

    exit_n=''

    while 1:

        minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']

        toVisit = ''

        for name, search in routing.items():

            if 0 < search['shortestDist'] <= minDist and not search['visited']:

                minDist = search['shortestDist']

                toVisit = name

        if toVisit == '':

            break

        visitPlace(toVisit)

        if toVisit=='1' or toVisit=='8' or toVisit=='13':

            if exit_dis>minDist:

                exit_dis=minDist

                exit_n=toVisit

        #print("[" + toVisit + "]")

        #print("Dist :", minDist)
    #print('fire: ', fire)

    if departure=='1' or departure=='8' or departure=='13':

        #print("[", departure, "->", departure, "]")

        #print("Route : ", departure)
        return departure

        #print("ShortestDistance : ", 0)
    else:

       # print("[", departure, "->", exit_n, "]")
        routing[exit_n]['route'].append(exit_n)
        return routing[exit_n]['route']
        #print("Route : ", routing[exit_n]['route'])
        #print("ShortestDistance : ", routing[exit_n]['shortestDist'])

    
