from core_character import Character
import random

class Warrior(Character):
    def __init__(self, name):
        """
        Initialize the Warrior character with specific attributes.
        
        :param name: str - The name of the warrior.
        """
        super().__init__(name, health=150, attack_power=40, dodge_chance=0.1)  # High health, good attack, low dodge

    def power_attack(self, target):
        """
        Perform a powerful two-handed strike on the target.

        :param target: Character - The target character being attacked.
        """
        print(f"{self.name} performs a two-handed strike on {target.name}!")
        if random.random() > target.dodge_chance:
            damage = self.attack_power * 2
            print(f"The power attack hits for {damage} damage!")
            target.health -= damage
        else:
            print(f"{target.name} dodges the power attack!")

    def glance(self):
        """
        Glance an incoming attack off the warrior's armor, reducing damage.
        
        :return: int - The damage reduction.
        """
        reduction = random.randint(5, 15)
        print(f"{self.name} glances the blow off his armor, reducing damage by {reduction}!")
        return reduction

    def display_stats(self):
        """
        Display the current stats of the Warrior character, including special abilities.
        """
        super().display_stats()
        print("Special Abilities: Power Attack (Two-Handed Strike), Glance (Damage Reduction)")
