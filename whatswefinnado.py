def start(self):
    action = input("what do you want to do: vent, fake wires, kill")
    cont = True
    sus = 0
    truss = 0
    while cont == True:
        if action == "vent":
            sus += 50
            truss += -20
            print('')
        elif action == "fake wires":
            sus -= 20
            truss += 35
            print('')
        elif action == "kill":
            sus += -100
            truss += -50
            print('')
        self.suspicious += sus
        self.trust += truss

        cont_ = input("do you want to continue: yes or no")
        if cont_ == "yes":
            cont = True
            action = input("what do you want to do:")
        elif cont_ == "no":
            cont = False
            break 
        
start()
