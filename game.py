from classes import card
from classes.deck import Deck
from classes.card import Card

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("Nombre del Jugador 1: ")
        name2 = input("Nombre del jugador 2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        print(f"{self.winner} wins this round")

    def draw(self):
        print(f"NOmbre: {self.p1.name} Points: {self.p1.wins} drew NOmbre: {self.p2.name} Points: {self.p2.wins}")
        
    def play_game(self):
        cards = self.deck.cards
        while len(cards) >= 2:
            print("************** Juego gana el mayor ***************")
            print("1.Para iniciar el juego")
            print("2.Para salir del juego")

            response = input("Ingresa opcion: ")
            if response == '2':
                break
            elif(response=="1"):
                cartas.suffle_cards()
                print(f"tamaño de la bajara es: {len(cards)}")
                print(f"********** Escojer carta jugador {self.p1.name} ************")
                escojer_carta_jugador1= input(f"Escoje una carta del 1 al {len(cards)}: ")
                carta_escojida_jugador1=cards[int(escojer_carta_jugador1)-1]
                cards.pop(int(escojer_carta_jugador1)-1)
                self.p1.card=carta_escojida_jugador1
                puntos_carta_jugador1=carta_escojida_jugador1.point_val
                print(f"tamaño de la bajara es: {len(cards)}")
                print(f"********** Escojer carta jugador {self.p2.name} ************")
                escojer_carta_jugador2= input(f"Escoje una carta del 1 al {len(cards)}: ")
                carta_escojida_jugador2=cards[int(escojer_carta_jugador2)-1]
                cards.pop(int(escojer_carta_jugador2)-1)
                self.p2.card=carta_escojida_jugador2
                puntos_carta_jugador2=carta_escojida_jugador2.point_val
                print("*******************************************************************")
                if puntos_carta_jugador1 > puntos_carta_jugador2:
                    self.p1.wins += 1
                    print(f"************* carta escojida jugador {self.p1.name} ******************")
                    carta_escojida_jugador1.card_info()
                    print(f"************* carta escojida jugador {self.p2.name} ******************")
                    carta_escojida_jugador2.card_info()
                    print(f"************ esta partida gana jugador {self.p1.name} *************")
                elif(puntos_carta_jugador1 < puntos_carta_jugador2):
                    print(f"************* carta escojida jugador {self.p1.name} ******************")
                    carta_escojida_jugador1.card_info()
                    print(f"************* carta escojida jugador {self.p2.name} ******************")
                    carta_escojida_jugador2.card_info()
                    self.p2.wins += 1
                    print(f"************ esta partida gana jugador {self.p2.name} *************")
                else:
                    self.p1.wins += 1
                    self.p2.wins += 1
                    print(f"************* carta escojida jugador {self.p1.name} ******************")
                    carta_escojida_jugador1.card_info()
                    print(f"************* carta escojida jugador {self.p2.name} ******************")
                    carta_escojida_jugador2.card_info()
                    print(f"************ esta partida es empate *************")
        
        if self.p1.wins > self.p2.wins:
            print(f"******************* gana el juego jugador {self.p1.name} ***********************")
        elif(self.p1.wins < self.p2.wins):
            print(f"******************* gana el juego jugador {self.p2.name} ***********************")
        else:
            print(f"******************* Empate ***********************")

cartas = Deck()
cartas.suffle_cards()
game = Game()
game.play_game()