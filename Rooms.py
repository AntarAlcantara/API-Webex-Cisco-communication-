


import requests
import json

opc = 0 
while opc != 4: 
    print("_________________________") 
    print("| 1.-  Enlistar Rooms   |")
    print("_________________________")
    print("| 2.- Crear un Room     |")
    print("_________________________")
    print("| 3.- Obtener detalles  |")
    print("_________________________")
    print("| 4.-detalles de reunion|")
    print("_________________________")
    opc = int(input("Opcion a elegir: ")) 
    accessToken = input("Ingresar el token porfa: ")
    accessToken = "Bearer " + accessToken
    if opc == 1: 
      apiUri = "https://api.ciscospark.com/v1/rooms"
      resp = requests.get( apiUri, headers = {"Authorization":accessToken} ) 
                         
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json() 
      print("Webex Teams Response Data:") 
      print( json.dumps(json_data, indent = 4) ) 

    if opc == 2:
      apiUri = "https://api.ciscospark.com/v1/rooms"
      nombreRoom = input("Nombre de sala: ")
      data = {
        'title' : nombreRoom
      }
      resp = requests.post( apiUri, headers = {"Authorization":accessToken}, data=data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("info del Room")
      print(json.dumps(json_data, indent = 4))

    if opc == 3:
      apiUri = "https://api.ciscospark.com/v1/rooms/"
      roomid = input("ID del room a consultar: ")
      apiUri = apiUri+roomid
      resp = requests.get( apiUri, headers = {"Authorization":accessToken})
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("detalles del Room")
      print(json.dumps(json_data, indent = 4))
    
    if opc == 4:
      apiUri = "https://api.ciscospark.com/v1/rooms/"
      roomid = input("ID del room a consultar: ")
      apiUri = apiUri+roomid+"/meetingInfo"
      resp = requests.get( apiUri, headers = {"Authorization":accessToken})
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del Webex Teams API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      json_data = resp.json()
      print("detalles de la reunion")
      print(json.dumps(json_data, indent = 4))
