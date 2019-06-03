import json

class Player():
    def __init__(self):
        self.first_name = input("Introduce el nombre del jugador: ")
        self.last_name = input("Introduce el apellido: ")
        self.height_cm = float(input("Introduce la altura en cms: "))
        self.weight_kg = float(input("Introduce el peso en kgs: "))
        self.haircolor = input("Introduce el color del pelo: ")

    def __str__(self):
        return 'Player: %s %s' % (self.first_name, self.last_name)

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self):
        super().__init__()
        self.points = input("Introduce el numero de puntos: ")
        self.rebounds = input("Introduce el numero de rebotes: ")
        self.assists = input("Introduce el numer de asistencias")

class FootballPlayer(Player):
    def __init__(self):
        super().__init__()
        self.goals = input("Introduce el numero de goles: ")
        self.yellow_cards = input("Introduce el numero de tarjetas amarillas: ")
        self.red_cards = input("Introduce el numero de tarjetas rojas: ")

with open("results_list.txt", "r") as results_file:
    results_list = json.loads(results_file.read())

while True:
    opcion = input("Desea: 1)añadir un jugador? o, 2)Salir del programa?")
    if opcion == "1":
        veces=int(input("cuantos jugadores quieres añadir?"))  #preguntamos al usuario cuantos jugadores quiere añadir y lo guardamos en veces
        for i in range(veces):  #creamos un for que haga tantas pasadas como veces
            jugador = FootballPlayer()
            jugador_dic = jugador.__dict__   #creamos una variable que tenga el valor de el diccionario de la clase instanciada
            if jugador_dic["first_name"] not in results_list: #si el campo "first_name" del diccionario no esta en la lista:
                results_list.append(jugador_dic)
                print("Has añadido los datos de: ", jugador_dic["first_name"], jugador_dic["last_name"])
                with open("results_list.txt", "w") as results_file:
                    results_file.write(json.dumps(results_list))
            else:  #si el "first_name" esta en la lista:
                print(jugador_dic["first_name"], jugador_dic["last_name"], "Ya estaba en la base de datos")
                pass
    elif opcion == "2":
        break
    else:
        opcion = input("Desea: 1)añadir un jugador o,2)Salir del programa?")




