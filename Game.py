import random
import pygame

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        hit = self.attack_power
        other.health -= hit
        print(f"{self.name} атаковал {other.name} и нанёс {hit} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name):
        self.player = player_name
        self.computer = computer_name

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer_turn()

        self.declare_winner()

    def player_turn(self):
        print(
            f"{self.player.name} (Здоровье: {self.player.health}) атакует {self.computer.name} (Здоровье: {self.computer.health})")
        self.player.attack(self.computer)
        print(f"{self.computer.name} (Здоровье: {self.computer.health})")

    def computer_turn(self):
        print(
            f"{self.computer.name} (Здоровье: {self.computer.health}) атакует {self.player.name} (Здоровье: {self.player.health})")
        self.computer.attack(self.player)
        print(f"{self.player.name} (Здоровье: {self.player.health})")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(player_name)
    computer = Hero("Компьютер")
    game = Game(player, computer)
    game.start()

pygame.quit()