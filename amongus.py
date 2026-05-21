
import random




locations = [
        {
            "Name": "Cafeteria",
            "actions": "Emergency button, meetings, card swipe (common)",
            "visual_task": False,
            "vents": [],
            "impostor_routes": "Vent from Admin or Weapons nearby; high-traffic escape routes"
        },
        {
            "Name": "Weapons",
            "actions": "Clear asteroids, download data",
            "visual_task": True,
            "vents": ["O2", "Navigation"],
            "impostor_routes": "Vent chain to O2 → Nav; easy early-game kills + escape"
        },
        {
            "Name": "O2",
            "actions": "Clean filter, fix O2 sabotage",
            "visual_task": False,
            "vents": ["Weapons", "Navigation"],
            "impostor_routes": "Loop vent triangle with Weapons/Nav"
        },
        {
            "Name": "Navigation",
            "actions": "Chart course, stabilize steering",
            "visual_task": False,
            "vents": ["Weapons", "O2"],
            "impostor_routes": "Dead-end for crewmates, but vent escape available"
        },
        {
            "Name": "Shields",
            "actions": "Prime shields",
            "visual_task": True,
            "vents": [],
            "impostor_routes": "No vents—risky kill spot unless escaping to hallway"
        },
        {
            "Name": "Communications",
            "actions": "Fix comms, download data",
            "visual_task": False,
            "vents": [],
            "impostor_routes": "Low traffic, but no vent escape"
        },
        {
            "Name": "Storage",
            "actions": "Fuel engines, empty garbage",
            "visual_task": False,
            "vents": [],
            "impostor_routes": "Central hub; many escape paths but no vents"
        },
        {
            "Name": "Admin",
            "actions": "Swipe card, use admin table",
            "visual_task": False,
            "vents": ["Cafeteria", "Electrical"],
            "impostor_routes": "Strong info room; vent chain to Caf/Electrical"
        },
        {
            "Name": "Electrical",
            "actions": "Fix lights, wires, divert power",
            "visual_task": False,
            "vents": ["Admin", "Security", "Medbay"],
            "impostor_routes": "Best impostor room; multiple vent escapes"
        },
        {
            "Name": "Lower Engine",
            "actions": "Align engine output, refuel",
            "visual_task": False,
            "vents": ["Reactor"],
            "impostor_routes": "Connects to Reactor vent"
        },
        {
            "Name": "Upper Engine",
            "actions": "Align engine output, refuel",
            "visual_task": False,
            "vents": ["Reactor"],
            "impostor_routes": "Connects to Reactor vent"
        },
        {
            "Name": "Reactor",
            "actions": "Start reactor, fix meltdown",
            "visual_task": False,
            "vents": ["Upper Engine", "Lower Engine"],
            "impostor_routes": "Strong sabotage + vent mobility"
        },
        {
            "Name": "Security",
            "actions": "View cameras",
            "visual_task": False,
            "vents": ["Electrical", "Medbay"],
            "impostor_routes": "Camera bait; vent access to Electrical"
        },
        {
            "Name": "Medbay",
            "actions": "Submit scan, inspect sample",
            "visual_task": True,
            "vents": ["Security", "Electrical"],
            "impostor_routes": "Fake scan risk; vent escape available"
        }
    ]


class crewmate:
    def __init__(selfs,colors,names,amount):
        selfs.names = names
        selfs.colors = colors
        selfs.amount = amount
    

class imposter:
    def __init__(self, name, color, suspicious = 0, trust = 50):
        self.name = name
        self.suspicious = suspicious
        self.trust = trust
        self.color = color


def start(self):
    self.name = input("What do you want your ingame name to be? ")
    print("You are the imposter, your goal is to decieve and kill all the crewmates.")
    self.color = input("Choose your color, green, black, red, white or pink?   ")
    if self.color == "red":
        self.suspicious +=10
        self.trust -= 10
        print("Your trust level is now", self.trust)
        print("Your sus level is now", self.suspicious)
    elif self.color == "pink":
        trust += 5
        print("Your trust level is now", self.trust)
        print("Your sus level is now", self.suspicious)
    else:
        print("Your trust level is: ", self.trust)
        print("Your sus level is: ", self.suspicious)


    for index, room in enumerate(locations):


        print(index,":", room["Name"])
    print("You have loaded into the game.")




colors = ["cyan", "yellow", "brown", "gray", "purple"]  
random_item = random.choice(colors)
report =["found","not found"]
random_dead = random.choice(report)


def kill_novent(self):
        crewmatess -= 1
        self.suspicious += 35
        trust -= 20
        print("Your trust level is now", trust)
        print("Your suspicious level is now",self.suspicious)
        colors.remove(random_item)
        print(random_item, "is dead")
        print("The body was", random_dead)

def action():
    print("where do you want to go? Please insert the #")
    pt1 = int(input("..."))
    print("You are now in", locations[pt1]["Name"])
    print(locations[pt1])
    print(f"Crewmate",{random_item}, "is also inside", locations[pt1]["Name"],"...")
    if pt1 == 6 or pt1 == 5 or pt1 == 4:
        action1 = input("What action would you like to do now? 1. Fake tasks, 2. Kill, or 3. Nothing? [No vents avaliable in this room] Insert the #   ")
        ventss = "none"
    else:
        action1 = input("What action would you like to do now? 1. Fake tasks, 2. Kill, 3. Nothing, or 4. Vent? Insert the #   ")
        ventss = "yes"

def fake_tasks(self):
    print(f"Crewmate saw you fake tasks...")
    self.trust += 10
    print("Your trust level is now", self.trust)
    print("Your suspicious level is now",self.suspicious)     

def kill_vent(self):
        crewmatess -= 1
        self.suspicious += 10
        self.trust -=10
        print("Your trust level is now", self.trust)
        print("Your suspicious level is now",self.suspicious)
        colors.remove(random_item)
        print(random_item, "is dead")
        print("The body was", random_dead)
def leave(self,pt1):
        print("You left",locations[pt1]["Name"],"...")
        print("Your trust level is still", self.trust)
        print("Your suspicious level is still",self.suspicious)
def vent():
        print("Choose where to vent.")
        next1 = int(input("..."))
        print([locations][next1]["vents"])
def emergency(self,random_item):
    print("Emergency meeting!!")
    if self.suspicious > 30:
            print("Your crewmates are suspicious of you. What are you gonna do? 1. Defend Yourself, 2. Accuse Someone else, 3. Stay silent")
            defence = int(input("..."))
            if defence == 1:
                print("Your crewmates believe you for now")
                self.trust += 15
                self.suspicious -= 15
                print("they decided to skip...")
            elif defence == 2:
                print({random_item}, "was voted out. He was innocent. You are now more suspicious")
                self.trust -= 10
                self.suspicious += 20
            elif defence == 3:
                print("Your crewmates are wary of you.")
                self.trust -= 5
                self.suspicious += 5
            elif self.suspicious < 30:
                print("Your crewmates are not suspicious of you. What are you gonna do? 1. Accuse Someone else, 2. Skip")
            defence = int(input("..."))
            if defence == 1:
                print({random_item}, "Was voted out. He was innocent. You are now more suspicious")
                self.trust -= 5
                self.suspicious += 10
            elif defence == 2:
                print("Your crewmates agree to skip")
                self.trust += 15



    












