def emergency_button(random_item, suspicious):
        if suspicious > 30:
            print("Your crewmates are suspicious of you. What are you gonna do? 1. Defend Yourself, 2. Accuse Someone else, 3. Stay silent")
            defence = int(input("..."))
            if defence == 1:
                print("Your crewmates believe you for now")
                trust += 15
                suspicious -= 15
                print("they decided to skip...")
            elif defence == 2:
                print({random_item}, "was voted out. He was innocent. You are now more suspicious")
                trust -= 10
                suspicious += 20
            elif defence == 3:
                print("Your crewmates are wary of you.")
                trust -= 5
                suspicious += 5
        elif suspicious < 30:
            print("Your crewmates are not suspicious of you. What are you gonna do? 1. Accuse Someone else, 2. Skip")
            defence = int(input("..."))
            if defence == 1:
                print({random_item}, "Was voted out. He was innocent. You are now more suspicious")
                trust -= 5
                suspicious += 10
                
            elif defence == 2:
                print("Your crewmates agree to skip")
                trust += 15
emergency_button("Jiaxi", 31)