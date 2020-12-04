print(" _________________________")
print("|   1.-    Rooms         |")
print("|_________________________|")
print("|   2.-   Messages        |")
print("|_________________________|")
print("|   3.-  Memberships      |")
print("|_________________________|")
print("|   4.-     Salir         |")
print("|_________________________|")

opc=int(input("Elige una opcion: "))
if opc == 1:
  exec(open("Rooms.py").read())
if opc == 2:
  exec(open("Messages.py").read())
if opc ==3:
  exec(open("Membership.py").read())
if opc ==4:
  print("Fin de la evaluacion")
