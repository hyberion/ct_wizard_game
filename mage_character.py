from core_character import Character
import random

class Mage(Character):
    def __init__(self, name):
        """
        Initialize the Mage character with specific attributes.

        :param name: str - The name of the mage.
        """
        super().__init__(name, health=100, attack_power=25, dodge_chance=0.25)  # Low health, moderate attack, moderate dodge
        self.mana = 100  # Mana starts at full (100%)

    def firebolt(self, target):
        """
        Cast a firebolt spell that strikes the target twice.

        :param target: Character - The target character being attacked.
        """
        print(f"{self.name} casts Firebolt at {target.name}, striking twice!")
        for _ in range(2):
            if random.random() > target.dodge_chance:
                print(f"Firebolt hits for {self.attack_power} damage!")
                target.health -= self.attack_power
            else:
                print(f"{target.name} dodges the Firebolt!")

    def fireball(self, target):
        """
        Cast a powerful fireball spell on the target, consuming mana.

        :param target: Character - The target character being attacked.
        """
        mana_cost = 30
        if self.mana >= mana_cost:
            print(f"{self.name} casts Fireball at {target.name}!")
            self.mana -= mana_cost
            if random.random() > target.dodge_chance:
                damage = self.attack_power * 3
                print(f"Fireball hits for {damage} damage!")
                target.health -= damage
            else:
                print(f"{target.name} dodges the Fireball!")
        else:
            print(f"{self.name} tries to cast Fireball but doesn't have enough mana!")

    def phase(self):
        """
        Attempt to magically phase and avoid an incoming attack.

        :return: bool - True if phasing is successful, False otherwise.
        """
        success = random.random() < self.dodge_chance
        if success:
            print(f"{self.name} phases out of reality and avoids the attack!")
        else:
            print(f"{self.name} fails to phase and takes the hit!")
        return success

    def regenerate_mana(self):
        """
        Regenerate mana by 10% of the maximum per turn.
        """
        regen_amount = 10
        self.mana = min(100, self.mana + regen_amount)
        print(f"{self.name} regenerates {regen_amount} mana. Current mana: {self.mana}")

    def display_stats(self):
        """
        Display the current stats of the Mage character, including special abilities.
        """
        super().display_stats()
        print(f"Mana: {self.mana}")
        print("Special Abilities: Firebolt (Double Strike), Fireball (High Damage, Mana Cost), Phase (Avoid Attack)")