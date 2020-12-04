

import requests
import json

opc = 0 
while opc != 4: 
    print("_________________________") 
    print("| 1.- Enlistar Messages |")
    print("_________________________")
    print("| 2.- Enlistar DM       |")
    print("_________________________")
    print("| 3.- Crear Messages    |")
    print("_________________________")
    print("| 4.-detalles   Messages|")
    print("_________________________")
    opc = int(input("Opcion a elegir: ")) 
    accessToken = input("Ingresar el token porfa: ")
    accessToken = "Bearer " + accessToken
    if opc == 1:
      apiUri = "https://api.ciscospark.com/v1/messages?roomId="
      roomid = input("ID del room a ver los mensajes: ")
      apiUri = apiUri+roomid
      resp = requests.get( apiUri, headers = {"Authorization":accessToken})
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("Mensajes")
      print(json.dumps(json_data, indent = 4))

    if opc == 2:
      apiUri = "https://api.ciscospark.com/v1/messages/direct?personId="
      usuario = input("personID de usuario a consultar DM: ")
      apiUri = apiUri+usuario
      resp = requests.get( apiUri, headers = {"Authorization":accessToken})
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("Mensajes enviados")
      print(json.dumps(json_data, indent = 4))

    if opc == 3:
      apiUri = "https://api.ciscospark.com/v1/messages"
      roomid = input("ID del room: ")
      menssage = input("escriba el mensaje: ")
      data = {
        'roomId': roomid,
        'text': menssage
      }
      resp = requests.post( apiUri, headers = {"Authorization":accessToken}, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print(json.dumps(json_data, indent = 4))
    
    if opc == 4:
      apiUri = "https://api.ciscospark.com/v1/messages/"
      idmensaje = input("ID del mensaje para ver los detalles: ")
      apiUri = apiUri+idmensaje
      resp = requests.get( apiUri, headers = {"Authorization":accessToken})
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("detalles del mensaje")
      print(json.dumps(json_data, indent = 4))
