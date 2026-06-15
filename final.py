import random


locations = [
    {
        "Name": "Cafeteria",
        "actions": "Emergency button, meetings, card swipe (common)",
        "vents": [],
        "impostor_routes": "Vent from Admin or Weapons nearby; high-traffic escape routes"
    },
    {
        "Name": "Weapons",
        "actions": "Clear asteroids, download data",
        "vents": ["O2", "Navigation"],
        "impostor_routes": "Vent chain to O2 → Nav; easy early-game kills + escape"
    },
    {
        "Name": "O2",
        "actions": "Clean filter, fix O2 sabotage",
        "vents": ["Weapons", "Navigation"],
        "impostor_routes": "Loop vent triangle with Weapons/Nav"
    },
    {
        "Name": "Navigation",
        "actions": "Chart course, stabilize steering",
        "vents": ["Weapons", "O2"],
        "impostor_routes": "Dead-end for crewmates, but vent escape available"
    },
    {
        "Name": "Shields",
        "actions": "Prime shields",
        "vents": [],
        "impostor_routes": "No vents—risky kill spot unless escaping to hallway"
    },
    {
        "Name": "Communications",
        "actions": "Fix comms, download data",
        "vents": [],
        "impostor_routes": "Low traffic, but no vent escape"
    },
    {
        "Name": "Storage",
        "actions": "Fuel engines, empty garbage",
        "vents": [],
        "impostor_routes": "Central hub; many escape paths but no vents"
    },
    {
        "Name": "Admin",
        "actions": "Swipe card, use admin table",
        "vents": ["Cafeteria", "Electrical"],
        "impostor_routes": "Strong info room; vent chain to Caf/Electrical"
    },
    {
        "Name": "Electrical",
        "actions": "Fix lights, wires, divert power",
        "vents": ["Admin", "Security", "Medbay"],
        "impostor_routes": "Best impostor room; multiple vent escapes"
    },
    {
        "Name": "Lower Engine",
        "actions": "Align engine output, refuel",
        "vents": ["Reactor"],
        "impostor_routes": "Connects to Reactor vent"
    },
    {
        "Name": "Upper Engine",
        "actions": "Align engine output, refuel",
        "vents": ["Reactor"],
        "impostor_routes": "Connects to Reactor vent"
    },
    {
        "Name": "Reactor",
        "actions": "Start reactor, fix meltdown",
        "vents": ["Upper Engine", "Lower Engine"],
        "impostor_routes": "Strong sabotage + vent mobility"
    },
    {
        "Name": "Security",
        "actions": "View cameras",
        "vents": ["Electrical", "Medbay"],
        "impostor_routes": "Camera bait; vent access to Electrical"
    },
    {
        "Name": "Medbay",
        "actions": "Submit scan, inspect sample",
        "vents": ["Security", "Electrical"],
        "impostor_routes": "Fake scan risk; vent escape available"
    }
]


class imposter:
    def __init__(self, name, color, suspicious, trust):
        self.name = name
        self.suspicious = suspicious
        self.trust = trust
        self.color = color
        
        self.crewmates = ["Cyan", "Yellow", "Brown", "Gray", "Purple"]  

        if color == "red":
            self.suspicious +=10
            self.trust -= 10
        elif color == "pink":
            self.trust += 5

    def select_color(self):
        color = input("What do you want your ingame name to be? ")
        if color not in self.crewmates:
            print("Please Select one of the options above.")


    
    def showrooms(self):
        for index, room in enumerate(locations):
            print(index,":", room["Name"])


    def emergency(self, random_item):
        if self.suspicious > 30:
            print("Your crewmates are suspicious of you. What are you gonna do? 1. Defend Yourself, 2. Accuse Someone else, 3. Stay silent")
            defence = int(input("..."))
            if defence == 1:
                print("Your crewmates believe you for now")
                self.trust += 5
                self.suspicious -= 5
            elif defence == 2:
                item = random.choice(self.crewmates)
                self.crewmates.remove(item)
                print({item}, "was voted out. He was innocent. You are now more suspicious")
                if random_item in self.crewmates:    
                    self.crewmates.remove(random_item)
                print(self.crewmates)
                self.trust -= 10
                self.suspicious += 20
            elif defence == 3:
                print("Your crewmates are wary of you.")
                self.trust -= 5
                self.suspicious += 15
        else:
            print("Your crewmates are not suspicious of you. What are you gonna do? 1. Accuse Someone else, 2. Skip")
            defence = int(input("..."))
            if defence == 1:
                item = random.choice(self.crewmates)
                self.crewmates.remove(item)
                print({item}, "Was voted out. He was innocent. You are now more suspicious")
                self.trust -= 5
                self.suspicious += 10
            elif defence == 2:
                print("Your crewmates agree to skip")

    def kill(self,random_item, random_body):
        self.suspicious += 10
        if random_item in self.crewmates:  
            self.crewmates.remove(random_item)
        print(random_item, "is dead")
        print("The body was", [random_body])
        print("There are",len(self.crewmates),"Crewmates left")
        
    def vent(self, pt1):
        print(locations[pt1]["vents"])
        pt1 = int(input("choose where to vent"))
        
        return pt1


              

    def startgame(self): 
        self.select_color
        game_status = ""
        print(self.suspicious, "is your suspision level")
        print(self.trust,"is your trust level")
        random_item = random.choice(self.crewmates)
        find_body = ["Found","Not found"]
        random_body = random.choice(find_body)
        self.showrooms()
        print("You are the imposter, your goal is to decieve and kill all the crewmates.")   
        print("where do you want to go? Please insert the #")

        pt1 = int(input("..."))

        while self.trust >= self.suspicious and len(self.crewmates) >= 1:
            random_item = random.choice(self.crewmates)
            find_body = ["Found","Not found"]
            random_body = random.choice(find_body)
            print("You are now in", locations[pt1]["Name"])
            print(f"Crewmate",{random_item}, "is also inside", locations[pt1]["Name"],"...")
            print("Your sus level is now.", self.suspicious)
            print("Your trust level is now.",self.trust)
            print(locations[pt1])

            if pt1 == 6 or pt1 == 5:
                action1 = input("What action would you like to do now? 1. Fake tasks, 2. Kill, or 3. Nothing? [No vents avaliable in this room] Insert the #   ")
                ventss = "none"
            elif pt1 == 0:
                action1 = input("What action would you like to do now? 1. Fake tasks, 2. Kill, 3. Nothing, 4. Vent, or 5. Emergency Button? Insert the #   ")
                ventss = "yes"
            else:
                action1 = input("What action would you like to do now? 1. Fake tasks, 2. Kill, 3. Nothing, or 4. Vent? Insert the #   ")
                ventss = "yes"



            if action1 == "1":
                print(f"Crewmate saw you fake tasks...")
                self.trust += 10
                print("where do you want to go? Please insert the #")
                pt1 = int(input("..."))
            elif action1 == "2":
                self.kill(random_item, random_body)
                
                if random_body == "Found":
                    print("[-EMERGENCY MEETING-]")
                    self.emergency(random_item)
                    
                print("where do you want to go? Please insert the #")
                self.showrooms()
                pt1 = int(input("..."))
            elif action1 == "3":
                print("You left", locations[pt1]["Name"],"...")
                self.showrooms()
                print("where do you want to go? Please insert the #")
                pt1 = int(input("..."))
            elif action1 == "4":
                pt1 = self.vent(pt1)


            elif action1 == "5":
                print("[-EMERGENCY MEETING-]")
                self.emergency(random_item)
                print("where do you want to go? Please insert the #")
                pt1 = int(input("..."))

            if self.suspicious > self.trust:
                game_status = "lost"
                
        if game_status == "lost":
            print("Your suspision is too high, you have been voted out by others!!!!!!! U SUCK")
        else:
            print("You have killed them all, omg youre so cool, awesome, and amazing!!")


name = input("what do you want to be called?   ")

check = True
while(check):
    color = ["red", "pink","white","blue","black"]
    select_color = input("What color do you want to be?   [red,pink,black,white, or blue]")
    if select_color in color:
        check = False
    else:
        print("Please select color in the list, small cap")


impopo = imposter(name, select_color, 0, 50)
print("You have loaded into the game.")

impopo.startgame()

