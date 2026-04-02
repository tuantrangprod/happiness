# i really love coding
# it started when i was 7th grade
# PASCAL. The first programming language i've learned
# The first thing i tried to do was game programming
# Years passed by, i still follow my heart
print("My 7th grade game!")

# Now i will try to code the game I did when I was a teenager
# a RPG combat/tactic game
# I dont know how to do py_game for shit so I'll log shit to the Terminal

import random

### INIT
game_over = False
days = 1
hero = None

class Hero:
    def __init__(self):
        self.hp = 100
        self.atk = 10
        self.coin = random.randint(10,50)

class GameEvent:
    def __init__(self, message, options):
        self.message = message
        self.options = options

    def process(self, choice, hero):
        pass

class EnemyEvent(GameEvent):
    def __init__(self):
        super().__init__("An enemy appeared!", {1: "attack", 2: "negotiate", 3: "flee"})

class TreasureEvent(GameEvent):
    def __init__(self):
        super().__init__("You found a treasure!", {1: "open", 2: "ignore"})

### MAIN
def init():
    hero = Hero()
    game_events = 2 # 2 type of events for now
    days = 1
    print("You started as a poor man.")
    print("Your HP: ", hero.hp)
    print("Your atk: ", hero.atk)
    print("Your coins: ", hero.coin)

def game_event():
    match random.randint(1,2):
        case 1:
            return EnemyEvent()
        case 2:
            return TreasureEvent()

def display_event(current_event):
    print("### DAY ", days)
    print(current_event.message)
    choices = [f"{num}: {label}" for num, label in current_event.options.items()]
    print("You choice: " + ", ".join(choices)) 

def main():
    init()
    # main game loop
    while not game_over:
        # game event
        current_event = game_event()
        # output display
        display_event(current_event)
        # wait for user input
        choice = input()
        if choice == "q" or "quit":
            exit
        # im tired. I will stop working here. Let me continue to feed my inner child tomorrow
        # process
        
        # outcome display
        break

if __name__ == "__main__":
    main()





