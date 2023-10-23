class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        return damage

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.health -= damage
        return damage

def main():
    # Get player's name
    name = input("Welcome to Eldritch Realms! Please enter your name: ")
    player = Player(name)

    print(f"Welcome, {player.name}!")

    # Create an enemy
    enemy = Enemy("Goblin", health=30, attack=8, defense=2)
    print(f"A wild {enemy.name} appears!")

    # Game loop
    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}: HP {player.health}, {enemy.name}: HP {enemy.health}")
        action = input("What will you do? (Attack/Run): ").lower()

        if action == "attack":
            damage_to_enemy = player.attack_enemy(enemy)
            damage_to_player = enemy.attack_player(player)
            print(f"You dealt {damage_to_enemy} damage to {enemy.name}!")
            print(f"{enemy.name} dealt {damage_to_player} damage to you!")

        elif action == "run":
            print("You managed to escape!")
            break

        else:
            print("Invalid action! Try again.")

        if enemy.health <= 0:
            print(f"\nYou defeated the {enemy.name}!")

    if player.health <= 0:
        print("You were defeated. Game over.")
    else:
        print("You won! Congratulations!")

if __name__ == "__main__":
    main()
