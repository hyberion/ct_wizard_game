from core_character import Character
import random

class Archer(Character):
    def __init__(self, name):
        """
        Initialize the Archer character with specific attributes.

        :param name: str - The name of the archer.
        """
        super().__init__(name, health=120, attack_power=20, dodge_chance=0.4)  # Mid health, low attack, high dodge

    def single_arrow(self, target):
        """
        Fire a single arrow at the target.

        :param target: Character - The target character being attacked.
        """
        print(f"{self.name} fires a single arrow at {target.name}!")
        hit_chance = 0.9  # High chance to hit
        if random.random() < hit_chance:
            print(f"The arrow hits for {self.attack_power} damage!")
            target.health -= self.attack_power
        else:
            print(f"{target.name} dodges the arrow!")

    def arrow_barrage(self, target):
        """
        Fire a barrage of arrows at the target, dealing damage for each successful hit.

        :param target: Character - The target character being attacked.
        """
        num_arrows = random.randint(2, 6)  # Between 4 and 8 arrows
        print(f"{self.name} unleashes an arrow barrage of {num_arrows} arrows at {target.name}!")
        hits = 0
        for _ in range(num_arrows):
            if random.random() > target.dodge_chance:
                hits += 1
                print(f"An arrow hits for {self.attack_power} damage!")
                target.health -= self.attack_power
            else:
                print(f"{target.name} dodges an arrow!")
        print(f"{self.name}'s arrow barrage hits {hits} times!")

    def dancing_dodge(self):
        """
        Perform a dancing dodge to avoid an incoming attack.

        :return: bool - True if the dodge is successful, False otherwise.
        """
        success = random.random() < self.dodge_chance
        if success:
            print(f"{self.name} performs a dancing dodge and avoids the attack!")
        else:
            print(f"{self.name} fails to dodge and takes the hit!")
        return success

    def display_stats(self):
        """
        Display the current stats of the Archer character, including special abilities.
        """
        super().display_stats()
        print("Special Abilities: Single Arrow (High Accuracy), Arrow Barrage (Multi-Hit), Dancing Dodge (Avoid Attack)")