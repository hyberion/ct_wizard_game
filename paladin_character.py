from core_character import Character
import random

class Paladin(Character):
    def __init__(self, name):
        """
        Initialize the Paladin character with specific attributes.

        :param name: str - The name of the paladin.
        """
        super().__init__(name, health=220, attack_power=30, dodge_chance=0.1)  # High health, moderate attack, low dodge

    def sword_swipe(self, target):
        """
        Perform a sword swipe attack that deals 1.5x base damage.

        :param target: Character - The target character being attacked.
        """
        damage = int(self.attack_power * 1.5)
        print(f"{self.name} swings their sword at {target.name}!")
        if random.random() > target.dodge_chance:
            print(f"The sword swipe hits for {damage} damage!")
            target.health -= damage
        else:
            print(f"{target.name} dodges the sword swipe!")

    def holy_strike(self, target):
        """
        Perform a holy strike attack, dealing base damage + 30, with a chance to stun the target.

        :param target: Character - The target character being attacked.
        """
        print(f"{self.name} strikes {target.name} with a divine holy strike!")
        if random.random() > target.dodge_chance:
            damage = self.attack_power + 30
            print(f"The holy strike hits for {damage} damage!")
            target.health -= damage
            if random.random() < 0.4:  # 40% chance to stun
                print(f"{target.name} is stunned and cannot attack next round!")
                return True  # Indicates the target is stunned
            else:
                print(f"{target.name} resists the stun!")
        else:
            print(f"{target.name} dodges the holy strike!")
        return False  # Indicates the target is not stunned

    def display_stats(self):
        """
        Display the current stats of the Paladin character, including special abilities.
        """
        super().display_stats()
        print("Special Abilities: Sword Swipe (1.5x Damage), Holy Strike (Damage + Stun Chance)")
