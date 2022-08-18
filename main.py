import  requests
import json
import urllib3
import conf

urllib3.disable_warnings()
url = "http://127.0.0.1:58000"
###########################Obtencion de ticket

cabecera ={"content-type":"application/json"}
respuesta = requests.post(url+"/api/v1/ticket", json.dumps(data), headers=cabecera, auth=(conf.username,conf.password),verify=False)
token = respuesta.json()["response"]["serviceTicket"]


##################Inventario de equipo

cabecera_inv = {"content-type":"application/json", "X-Auth-Token":token}
inventario = requests.get(url+"/api/v1/network-device", headers=cabecera_inv, auth=(conf.username,conf.password),verify=False)
print(json.dumps(inventario.json(), indent=2))

