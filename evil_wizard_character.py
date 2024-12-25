from core_character import Character
import random

class EvilWizard(Character):
    def __init__(self, name="Mad Wizard"):
        """
        Initialize the Evil Wizard character with specific attributes.

        :param name: str - The name of the wizard.
        """
        super().__init__(name, health=200, attack_power=20, dodge_chance=0.2)  # High health, moderate dodge, moderate attack
        self.damage_reduction_active = False  # Tracks if frost bolt effect is active

    def taunt(self):
        """
        Say a random taunt or insult to the player.
        """
        taunts = [
            "Is that all you've got, pathetic fool?",
            "You dare challenge my power? Prepare to be annihilated!",
            "Your efforts are as weak as your will!",
            "Bow before me, or suffer a humiliating defeat!",
            "You should have stayed home, little hero."
        ]
        print(f"{self.name} taunts: '{random.choice(taunts)}'")

    def lightning_strike(self, target):
        """
        Perform a lightning strike attack that deals 1.5x base damage.

        :param target: Character - The target character being attacked.
        """
        self.taunt()
        damage = int(self.attack_power * 1.5)
        print(f"{self.name} casts Lightning Strike at {target.name}!")
        if random.random() > target.dodge_chance:
            print(f"The lightning strike hits for {damage} damage!")
            target.health -= damage
        else:
            print(f"{target.name} dodges the lightning strike!")

    def frost_bolt(self, target):
        """
        Perform a frost bolt attack, with a chance to halve the target's damage next turn.

        :param target: Character - The target character being attacked.
        """
        self.taunt()
        print(f"{self.name} hurls a Frost Bolt at {target.name}!")
        if random.random() > target.dodge_chance:
            print(f"The frost bolt hits for {self.attack_power} damage!")
            target.health -= self.attack_power
            if random.random() < 0.3:  # 30% chance to reduce damage
                print(f"{target.name} is chilled! Their damage will be halved next turn.")
                target.attack_power = max(1, target.attack_power // 2)  # Halve the attack power
            else:
                print(f"{target.name} resists the chill effect!")
        else:
            print(f"{target.name} dodges the frost bolt!")

    def regenerate_health(self):
        """
        Regenerate health at the start of each turn.
        """
        heal_amount = 5
        self.health += heal_amount
        print(f"{self.name} regenerates {heal_amount} health. Current health: {self.health}")

    def display_stats(self):
        """
        Display the current stats of the Evil Wizard character, including special abilities.
        """
        super().display_stats()
        print("Special Abilities: Lightning Strike (1.5x Damage), Frost Bolt (Damage + Chill Effect)")
        print("Passive: Regenerates 5 health per turn.")
