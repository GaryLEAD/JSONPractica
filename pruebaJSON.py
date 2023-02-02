import json

with open("1prueba.json", "r") as j:
    mydata = json.load(j)
    print(mydata["carro_compras"])