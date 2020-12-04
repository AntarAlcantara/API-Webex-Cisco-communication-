

import requests
import json

opc = 0 
while opc != 4: 
    print("_________________________") 
    print("| 1.-Enlistar Membership|")
    print("_________________________")
    print("| 2.- Crear Membership  |")
    print("_________________________")
    print("| 3.-Detalles Membership|")
    print("_________________________")
    opc = int(input("Opcion a elegir: ")) 
    accessToken = input("Ingresar el token porfa: ")
    accessToken = "Bearer " + accessToken
    if opc == 1:
      apiUri = "https://api.ciscospark.com/v1/memberships?roomId="
      roomid = input("ID del room a ver quien ta' dentro xd: ")
      apiUri = apiUri+roomid
      resp = requests.get( apiUri, headers = {"Authorization":accessToken})
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("Miembros de la sala y no de los que piensa jsjsjsjs: ")
      print(json.dumps(json_data, indent = 4))

    if opc == 2:
      apiUri = "https://api.ciscospark.com/v1/memberships"
      roomid = input("ID del room pa ponerle otro miembro: ")
      personId = input("personID del miembro a meter: ")
      data = {
        'roomId' : roomid,
        'personId' : personId
      }
      resp = requests.post( apiUri, headers =  {"Authorization":accessToken}, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("Detalles del nuevo miembro introducido: ")
      print(json.dumps(json_data, indent = 4))

    if opc == 3:
      apiUri = "https://api.ciscospark.com/v1/memberships/"
      membershipId = input("ID del miembro a revisar: ")
      apiUri = apiUri+membershipId
      resp = requests.get( apiUri, headers = {"Authorization":accessToken})
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("Detalles del miembro: ")
      print(json.dumps(json_data, indent = 4))
