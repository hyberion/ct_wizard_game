import random

class Character:
    def __init__(self, name, health, attack_power, dodge_chance):
        """
        Initialize the core attributes of a character.
        
        :param name: str - The name of the character.
        :param health: int - The health points of the character.
        :param attack_power: int - The attack power of the character.
        :param dodge_chance: float - The dodge chance of the character (0.0 to 1.0).
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.dodge_chance = dodge_chance
        self.healing_potions = random.randint(2, 6)

    def base_attack(self, target):
        """
        Perform a base attack on a target character.

        :param target: Character - The target character being attacked.
        """
        print(f"{self.name} attacks {target.name} with a base attack!")
        if random.random() > target.dodge_chance:
            print(f"The attack hits for {self.attack_power} damage!")
            target.health -= self.attack_power
        else:
            print(f"{target.name} dodges the attack!")

    def heal(self):
            """
            Heal the character using a health potion if available.
            """
            if self.healing_potions > 0:
                if random.random() < 0.1:  # 10% chance for critical success
                    self.health = self.max_health
                    print(f"{self.name} uses a health potion and achieves a CRITICAL SUCCESS! Fully healed to {self.max_health} health! ({self.healing_potions - 1} potions left)")
                else:
                    heal_amount = random.randint(30, 75)
                    self.health += heal_amount
                    self.health = min(self.health, self.max_health)  # Cap at max health
                    print(f"{self.name} uses a health potion and heals for {heal_amount} points! ({self.healing_potions - 1} potions left)")
                self.healing_potions -= 1
            else:
                print(f"{self.name} has no health potions left!")

    def display_stats(self):
        """
        Display the current stats of the character.
        """
        print(f"--- {self.name} Stats ---")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Dodge Chance: {self.dodge_chance * 100:.1f}%")
        print(f"Healing Potions: {self.healing_potions}")
