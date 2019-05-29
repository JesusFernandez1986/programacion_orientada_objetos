import json

with open("results_file.txt", "r") as result:
    results_file = json.loads(result.read())

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg, haircolor):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.haircolor = haircolor

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists, haircolor):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg, haircolor=haircolor)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards, haircolor):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg, haircolor=haircolor)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4,
                           haircolor=input("introduce el color de pelo de Kevin Durant: "))
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0,
                       haircolor=input("introduce el color de pelo de Messi "))

jugador1=kev_dur.__dict__ #creo dos variables que guardan las caracteristicas de cada jugador en formato diccionario
jugador2=messi.__dict__

jugadores=[jugador1, jugador2] #creo una lista con los diccionarios de cada jugador
num_jugadores=len(jugadores)

results_file = [] #vacio el archivo results_file.txt

for x in jugadores: #bucle que recorre la lista jugadores y si alguno de esos jugadores no esta en la lista, los añade
    player= str(x)
    if player not in results_file:
        results_file.append(player)

with open("results_file.txt", "w") as result:
    result.write(json.dumps(results_file))
