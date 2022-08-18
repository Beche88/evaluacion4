import  requests
import json
import urllib3
import conf
ata = {"password":"admin123!",
        "username":"admin"}
urllib3.disable_warnings()
url = "http://127.0.0.1:58000"
###########################Obtencion de ticket

cabecera ={"content-type":"application/json"}
respuesta = requests.post(url +"/api/v1/ticket", json.dumps(conf.data), headers=cabecera)
token = respuesta.json()["response"]["serviceTicket"]


##################Inventario de equipo

cabecera_inv = {"content-type":"application/json", "X-Auth-Token":token}
inventario = requests.get(url+"/api/v1/network-device", headers=cabecera_inv)
print(json.dumps(inventario.json(), indent=2))

