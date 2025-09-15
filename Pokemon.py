# Scott's Pokemon Game #

### Moduels ###
from graphics import *
import random
import time
import pygame # Pygame is only used for sound

                ### Title Screen ###

pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/pokemonSong.wav") # Loads the theme

pygame.mixer.music.set_volume(0.5) # Plays the music at 50% volume
pygame.mixer.music.play(-1) # Loops the music

titleWin = GraphWin("Welcome to Pokemon!", 1200, 700)
titleScreen = Image(Point(600, 350), "assets/images/finaltitlewin.gif")
titleScreen.draw(titleWin)

### The cursor for the title screen ###
selector = Circle(Point(425, 420), 15)
selector.setWidth(5)
selector.setOutline("blue")
selector.setFill(color_rgb(255, 213, 0))
selector.draw(titleWin)

select = 1 # The variable for checking what the selector is hovering over
gameClose = False
battleCount = 0 # Checks how many battles the player has done

while True:
### Selector ###        
        k = titleWin.getKey()
 
        if k.lower() == "w" and select > 1: # Makes sure that the selector is not on the top
                select -= 1
                selector.move(0, -90) # Moves the selector up
                
        elif k.lower() == "s" and select < 2: # Makes sure that the selector is not on the bottom
                select += 1
                selector.move(0, 90) # Moves the selector down
                                 
        elif k.lower() == "e": # "e" selects the option that you are hovering over (Start or Exit)
                if select == 2: # If the player chose exit
                        gameClose = True 
                        break
                else: # If the player chose play
                        break
                
titleWin.close() # Ends the title screen

                ### Pokemon Selection Screen ###

win = GraphWin("Choose a Pokemon", 1200, 700)

if gameClose == True: # Checks if you pressed the option exit instead of start
        win.close()
        
background = Image(Point(600, 350), "assets/images/background.gif") # The image for the background
background.draw(win)

instructionFrame = Image(Point(275, 565), "assets/images/bigframe.gif") # The image for the instructions in the bottom left corner of the screen
instructionFrame.draw(win)

instructions = Text(Point(275, 565), "Press 'e' to\n select your Pokemon!") # The text for the instructions
instructions.setSize(25)
instructions.draw(win)

### The sprites for the starter Pokemon ###
pikachu = Image(Point(190, 250), "assets/images/pikachu.gif")
charmander = Image(Point(450, 265), "assets/images/charmander.gif")
squirtle = Image(Point(750, 250), "assets/images/squirtle.gif")
bulbasaur = Image(Point(1010, 250), "assets/images/bulbasaur.gif")

pikachu.draw(win)
charmander.draw(win)
squirtle.draw(win)
bulbasaur.draw(win)

### The buttons that go underneath the sprites for the buttons ###
button1 = Rectangle(Point(800, 550), Point(600, 450))
button2 = Rectangle(Point(1100, 550), Point(900, 450))
button3 = Rectangle(Point(800, 675), Point(600, 575))
button4 = Rectangle(Point(1100, 675), Point(900, 575))

button1.setFill("yellow")
button2.setFill("white")
button3.setFill("white")
button4.setFill("white")

button1.draw(win)
button2.draw(win)
button3.draw(win)
button4.draw(win)

### The sprites for the buttons ###
pButton = Image(Point(700, 500), "assets/images/pikachubutton.gif")
cButton = Image(Point(1000, 500), "assets/images/charmanderbutton.gif")
sButton = Image(Point(700, 625), "assets/images/squirtlebutton.gif")
bButton = Image(Point(1000, 625), "assets/images/bulbasaurbutton.gif")

pButton.draw(win)
cButton.draw(win)
sButton.draw(win)
bButton.draw(win)

    
pokemonChoiceX = 1 # Variables to check what Pokemon the user is selecting
pokemonChoiceY = 1

while True:
        
        k = win.getKey()

### Checks for inputs and changes the pokemonChoice variables based on the new information
        if k.lower() == "w":
            pokemonChoiceY -= 1            
            if pokemonChoiceY < 1:
                pokemonChoiceY = 1
            
        elif k.lower() == "a":
            pokemonChoiceX -= 1            
            if pokemonChoiceX < 1:
                pokemonChoiceX = 1
            
        elif k.lower() == "s":
            pokemonChoiceY += 1            
            if pokemonChoiceY > 2:
                pokemonChoiceY = 2
            
        elif k.lower() == "d":
            pokemonChoiceX += 1            
            if pokemonChoiceX > 2:
                pokemonChoiceX = 2
            
        elif k.lower() == "e": # If the user presses "e" it selects the Pokemon they are hovering over
            break
        
        if pokemonChoiceX == 1 and pokemonChoiceY == 1: # Pikachu
### The code below will highlight one of the buttons yellow and make sure that all of the other buttons are white ###
            button1.undraw()
            button1.setFill("yellow")
            button1.draw(win)
            button2.undraw()
            button2.setFill("white")
            button2.draw(win)
            button3.undraw()
            button3.setFill("white")
            button3.draw(win)
            button4.undraw()
            button4.setFill("white")
            button4.draw(win)
### Re-draws the sprites on top of the buttons ###            
            pButton.undraw()
            cButton.undraw()
            sButton.undraw()
            bButton.undraw()
        
            pButton.draw(win)
            cButton.draw(win)
            sButton.draw(win)
            bButton.draw(win)
            
            for i in range(3): # Small animation for the selected Pokemon
                            pikachu.move(10, 0)
                            time.sleep(0.1)
                            pikachu.move(-10, 0)
                            time.sleep(0.1)
                            
        if pokemonChoiceX == 2 and pokemonChoiceY == 1: # Charmander
### The code below will highlight one of the buttons yellow and make sure that all of the other buttons are white ###
            button2.undraw()
            button2.setFill("yellow")
            button2.draw(win)
            button1.undraw()
            button1.setFill("white")
            button1.draw(win)
            button3.undraw()
            button3.setFill("white")
            button3.draw(win)
            button4.undraw()
            button4.setFill("white")
            button4.draw(win)
### Re-draws the sprites on top of the buttons ###                
            pButton.undraw()
            cButton.undraw()
            sButton.undraw()
            bButton.undraw()
        
            pButton.draw(win)
            cButton.draw(win)
            sButton.draw(win)
            bButton.draw(win)
            
            for i in range(3): # Small animation for the selected Pokemon
                            charmander.move(10, 0)
                            time.sleep(0.1)
                            charmander.move(-10, 0)
                            time.sleep(0.1)
                            
        if pokemonChoiceX == 1 and pokemonChoiceY == 2: # Squirtle\
### The code below will highlight one of the buttons yellow and make sure that all of the other buttons are white ###
            button3.undraw()
            button3.setFill("yellow")
            button3.draw(win)
            button2.undraw()
            button2.setFill("white")
            button2.draw(win)
            button1.undraw()
            button1.setFill("white")
            button1.draw(win)
            button4.undraw()
            button4.setFill("white")
            button4.draw(win)
### Re-draws the sprites on top of the buttons ###                
            pButton.undraw()
            cButton.undraw()
            sButton.undraw()
            bButton.undraw()
        
            pButton.draw(win)
            cButton.draw(win)
            sButton.draw(win)
            bButton.draw(win)
            
            for i in range(3): # Small animation for the selected Pokemon
                            squirtle.move(10, 0)
                            time.sleep(0.1)
                            squirtle.move(-10, 0)
                            time.sleep(0.1)
                            
        if pokemonChoiceX == 2 and pokemonChoiceY == 2: # Bulbasaur
### The code below will highlight one of the buttons yellow and make sure that all of the other buttons are white ###
            button4.undraw()
            button4.setFill("yellow")
            button4.draw(win)
            button2.undraw()
            button2.setFill("white")
            button2.draw(win)
            button3.undraw()
            button3.setFill("white")
            button3.draw(win)
            button1.undraw()
            button1.setFill("white")
            button1.draw(win)
### Re-draws the sprites on top of the buttons ###                
            pButton.undraw()
            cButton.undraw()
            sButton.undraw()
            bButton.undraw()
        
            pButton.draw(win)
            cButton.draw(win)
            sButton.draw(win)
            bButton.draw(win)
            
            for i in range(3): # Small animation for the selected Pokemon
                            bulbasaur.move(10, 0)
                            time.sleep(0.1)
                            bulbasaur.move(-10, 0)
                            time.sleep(0.1)

# Gives the Pokemon that the user chose a value        
# Pikachu = 1, Charmander = 2, Squirtle = 3, Bulbasaur = 4
if pokemonChoiceX == 1 and pokemonChoiceY == 1:
        pokemonChoice = 1
elif pokemonChoiceX == 2 and pokemonChoiceY == 1:
        pokemonChoice = 2
elif pokemonChoiceX == 1 and pokemonChoiceY == 2:
        pokemonChoice = 3
elif pokemonChoiceX == 2 and pokemonChoiceY == 2:
        pokemonChoice = 4

### Uses the value of the Pokemon that the user chose to give their Pokemon values based on the value ###
if pokemonChoice == 1: # Pikachu
        pokemonName = "Pikachu"
        specialAttack1 = "Thunderbolt"
        specialAttack2 = "Volt Tackle"
        sAttack1 = Image(Point(700, 625), "assets/images/thunderbolt.gif")
        sAttack2 = Image(Point(1000, 625), "assets/images/volttackle.gif")
        
if pokemonChoice == 2: # Charmander
        pokemonName = "Charmander"
        specialAttack1 = "Blast Burn"
        specialAttack2 = "Ember"
        sAttack1 = Image(Point(700, 625), "assets/images/blastburn.gif")
        sAttack2 = Image(Point(1000, 625), "assets/images/ember.gif")
        
elif pokemonChoice == 3: # Squirtle
        pokemonName = "Squirtle"
        specialAttack1 = "Waterfall"
        specialAttack2 = "Water Gun"
        sAttack1 = Image(Point(700, 625), "assets/images/waterfall.gif")
        sAttack2 = Image(Point(1000, 625), "assets/images/watergun.gif")
        
elif pokemonChoice == 4: # Bulbasaur
        pokemonName = "Bulbasaur"
        specialAttack1 = "Poison Powder"
        specialAttack2 = "Razor Leaf"
        sAttack1 = Image(Point(700, 625), "assets/images/poisonpowder.gif")
        sAttack2 = Image(Point(1000, 625), "assets/images/razorleaf.gif")

win.close()

                ### Main Movement Window ###

win = GraphWin("Pokemon", 1200, 700)
gym = Image(Point(600, 350), "assets/images/gym.gif")
gym.draw(win)

loseGame = False

def pokemonBattle ():
        
                ### Battle Graphics ###

        global battleCount
        
        battleWin = GraphWin("Battle Window", 1200, 700)

        battleBackground = Image(Point(600, 350), "assets/images/battlebackground.gif") # The background for the battle window
        battleBackground.draw(battleWin)

        pShadow = Oval(Point(300, 500), Point(100, 600)) # The shadows for the Pokemon
        eShadow = Oval(Point(1100, 350), Point(900, 450))

        pShadow.setOutline("green")
        eShadow.setOutline("green")

        pShadow.setFill("green")
        eShadow.setFill("green")

        pShadow.draw(battleWin)
        eShadow.draw(battleWin)

### Checks what Pokemon the user chose at the start then draws it in the battle window ###        
        if pokemonChoice == 1:
                pikachu = Image(Point(200, 450), "assets/images/pikachu.gif")
                pikachu.draw(battleWin)
        elif pokemonChoice == 2:
                charmander = Image(Point(200, 450), "assets/images/charmander.gif")
                charmander.draw(battleWin)
        elif pokemonChoice == 3:
                squirtle = Image(Point(200, 450), "assets/images/squirtle.gif")
                squirtle.draw(battleWin)
        elif pokemonChoice == 4:
                bulbasaur = Image(Point(200, 450), "assets/images/bulbasaur.gif")
                bulbasaur.draw(battleWin)
### Checks what battle you are on to find the corresponding Pokemon to fight ###                
        if battleCount == 0:
                pidgey = Image(Point(1000, 300), "assets/images/pidgey.gif")
                pidgey.draw(battleWin)
        elif battleCount == 1:
                diglet = Image(Point(1000, 300), "assets/images/diglet.gif")
                diglet.draw(battleWin)
        elif battleCount == 2:
                onyx = Image(Point(1000, 300), "assets/images/onyx.gif")
                onyx.draw(battleWin)

        pFrame = Image(Point(200, 250), "assets/images/frame.gif")
        eFrame = Image(Point(1000, 100), "assets/images/frame.gif")

        pFrame.draw(battleWin)
        eFrame.draw(battleWin)

        enemyHp = 1000 # The health of the enemy Pokemon
        pokemonHp = 1000 # The health of your Pokemon

        if battleCount == 1: # Increases the enemy Pokemon's health if it is the second battle
                enemyHp = 1250
        elif battleCount == 2: # Increases the enemy Pokemon's health greatly if it is the third battle
                enemyHp = 1500

        pokemonHealth = Text(Point(200, 250), pokemonHp) # The display for your Pokemon's health
        pokemonHealth.setSize(36)
        pokemonHealth.draw(battleWin)
        
        enemyHealth = Text(Point(1000, 100), enemyHp) # The display for the enemy Pokemon's health
        enemyHealth.setSize(36)
        enemyHealth.draw(battleWin)

        attack1 = Image(Point(700, 500), "assets/images/quickattack.gif")
        attack2 = Image(Point(1000, 500), "assets/images/tackle.gif")

### The buttons ###
        button1 = Rectangle(Point(800, 550), Point(600, 450))
        button2 = Rectangle(Point(1100, 550), Point(900, 450))
        button3 = Rectangle(Point(800, 675), Point(600, 575))
        button4 = Rectangle(Point(1100, 675), Point(900, 575))
            
        button1.draw(battleWin)
        button2.draw(battleWin)
        button3.draw(battleWin)
        button4.draw(battleWin)
        
                ### Player Attack Selection / Player Attack ###
        
        attackChoiceX = 1 # Checks what attack the user is hovering over
        attackChoiceY = 1

### The code below will highlight one of the buttons yellow and make sure that all of the other buttons are white depending on the attack you are hovering over###        
        if attackChoiceX == 1 and attackChoiceY == 1:
                    button1.undraw()
                    button1.setFill("yellow")
                    button1.draw(battleWin)
                    button2.undraw()
                    button2.setFill("white")
                    button2.draw(battleWin)
                    button3.undraw()
                    button3.setFill("white")
                    button3.draw(battleWin)
                    button4.undraw()
                    button4.setFill("white")
                    button4.draw(battleWin)
                    
        elif attackChoiceX == 2 and attackChoiceY == 1:
                    button2.undraw()
                    button2.setFill("yellow")
                    button2.draw(battleWin)
                    button1.undraw()
                    button1.setFill("white")
                    button1.draw(battleWin)
                    button3.undraw()
                    button3.setFill("white")
                    button3.draw(battleWin)
                    button4.undraw()
                    button4.setFill("white")
                    button4.draw(battleWin)
                    
        elif attackChoiceX == 1 and attackChoiceY == 2:
                    button3.undraw()
                    button3.setFill("yellow")
                    button3.draw(battleWin)
                    button2.undraw()
                    button2.setFill("white")
                    button2.draw(battleWin)
                    button1.undraw()
                    button1.setFill("white")
                    button1.draw(battleWin)
                    button4.undraw()
                    button4.setFill("white")
                    button4.draw(battleWin)
                    
        elif attackChoiceX == 2 and attackChoiceY == 2:
                    button4.undraw()
                    button4.setFill("yellow")
                    button4.draw(battleWin)
                    button2.undraw()
                    button2.setFill("white")
                    button2.draw(battleWin)
                    button3.undraw()
                    button3.setFill("white")
                    button3.draw(battleWin)
                    button1.undraw()
                    button1.setFill("white")
                    button1.draw(battleWin)

### Re-draws the sprites for the buttons ###                 
        attack1.draw(battleWin)
        attack2.draw(battleWin)
        sAttack1.draw(battleWin)
        sAttack2.draw(battleWin)

        endGame = False # Checks if the game should end
        
        while True:
                
            if endGame == True: # Checks if the game should end
                break
       
            while True: ### The code for the attack selector ###                       
                k = battleWin.getKey()
                if k.lower() == "w":
                    attackChoiceY -= 1
                    if attackChoiceY < 1:
                        attackChoiceY = 1
                elif k.lower() == "a":
                    attackChoiceX -= 1
                    if attackChoiceX < 1:
                        attackChoiceX = 1
                elif k.lower() == "s":
                    attackChoiceY += 1
                    if attackChoiceY > 2:
                        attackChoiceY = 2
                elif k.lower() == "d":
                    attackChoiceX += 1
                    if attackChoiceX > 2:
                        attackChoiceX = 2
                elif k.lower() == "e":
                    break
                
### The code below will highlight one of the buttons yellow and make sure that all of the other buttons are white depending on the attack you are hovering over###                
                if attackChoiceX == 1 and attackChoiceY == 1:
                    button1.undraw()
                    button1.setFill("yellow")
                    button1.draw(battleWin)
                    button2.undraw()
                    button2.setFill("white")
                    button2.draw(battleWin)
                    button3.undraw()
                    button3.setFill("white")
                    button3.draw(battleWin)
                    button4.undraw()
                    button4.setFill("white")
                    button4.draw(battleWin)
                    
                elif attackChoiceX == 2 and attackChoiceY == 1:
                    button2.undraw()
                    button2.setFill("yellow")
                    button2.draw(battleWin)
                    button1.undraw()
                    button1.setFill("white")
                    button1.draw(battleWin)
                    button3.undraw()
                    button3.setFill("white")
                    button3.draw(battleWin)
                    button4.undraw()
                    button4.setFill("white")
                    button4.draw(battleWin)
                    
                elif attackChoiceX == 1 and attackChoiceY == 2:
                    button3.undraw()
                    button3.setFill("yellow")
                    button3.draw(battleWin)
                    button2.undraw()
                    button2.setFill("white")
                    button2.draw(battleWin)
                    button1.undraw()
                    button1.setFill("white")
                    button1.draw(battleWin)
                    button4.undraw()
                    button4.setFill("white")
                    button4.draw(battleWin)
                    
                elif attackChoiceX == 2 and attackChoiceY == 2:
                    button4.undraw()
                    button4.setFill("yellow")
                    button4.draw(battleWin)
                    button2.undraw()
                    button2.setFill("white")
                    button2.draw(battleWin)
                    button3.undraw()
                    button3.setFill("white")
                    button3.draw(battleWin)
                    button1.undraw()
                    button1.setFill("white")
                    button1.draw(battleWin)

### Re-draws all of the buttons ###                    
                attack1.undraw()
                attack2.undraw()
                sAttack1.undraw()
                sAttack2.undraw()
                
                attack1.draw(battleWin)
                attack2.draw(battleWin)
                sAttack1.draw(battleWin)
                sAttack2.draw(battleWin)

                ### Attack Logic ###
### All of the battleText variables will change the text that appears on the screen while battling the opponent ###                
            if attackChoiceX == 1 and attackChoiceY == 1:
                attackChance = random.randint(0, 5)
                if attackChance == 5: # Critical hit chance
                    enemyHp -= 200 # This attack will deal 200 damage
                    battleText = Text(Point(600, 350), f"Critical hit! {pokemonName} \nused Quick Attack!")
                else: 
                    enemyHp -= 100 # This attack will deal 100 damage                
                    battleText = Text(Point(600, 350), f"Nice hit! {pokemonName} \nused Quick Attack!")
            elif attackChoiceX == 1 and attackChoiceY == 2:
                attackChance = random.randint(0, 5)
                if attackChance == 5:
                    enemyHp -= 350 # This attack will deal 350 damage
                    battleText = Text(Point(600, 350), "Critical hit!")
                elif attackChance <= 2:
                    battleText = Text(Point(600, 350), "You missed!")
                else:
                    enemyHp -= 200 # This attack will deal 200 damage
                    battleText = Text(Point(600, 350), f"Nice hit! {pokemonName} \nused {specialAttack1}!")
            elif attackChoiceX == 2 and attackChoiceY == 2:
                attackChance = random.randint(0, 5)
                if attackChance == 5:
                    enemyHp -= 400 # This attack will deal 400 damage
                    pokemonHp -= 150 # This attack will deal 150 damage to your own Pokemon
                    battleText = Text(Point(600, 350), "Critical hit!")
                else:
                    enemyHp -= 300 # This attack will deal 300 damage
                    pokemonHp -= 150 # This attack will deal 150 damage to your own Pokemon
                    battleText = Text(Point(600, 350), f"Nice hit! {pokemonName} \nused {specialAttack2}!")
            else:
                attackChance = random.randint(0, 5)
                if attackChance >= 3:
                    enemyHp -= 300 # This attack will deal 300 damage
                    battleText = Text(Point(600, 350), "Critical hit!")
                else:
                    enemyHp -= 50 # This attack will deal 50 damage
                    battleText = Text(Point(600, 350), f"Nice hit! {pokemonName} \nused Tackle!")

                ### Attack Animations ###
                    
            if pokemonChoice == 1: # Pikachu
                    for i in range(3):
                            pikachu.move(10, 0)
                            time.sleep(0.1)
                            pikachu.move(-10, 0)
                            time.sleep(0.1)
            elif pokemonChoice == 2: # Charmander
                    for i in range(3):
                            charmander.move(10, 0)
                            time.sleep(0.1)
                            charmander.move(-10, 0)
                            time.sleep(0.1)
            elif pokemonChoice == 3: # Squirtle
                    for i in range(3):
                            squirtle.move(10, 0)
                            time.sleep(0.1)
                            squirtle.move(-10, 0)
                            time.sleep(0.1)
            elif pokemonChoice == 4: # Bulbasaur
                    for i in range(3):
                            bulbasaur.move(10, 0)
                            time.sleep(0.1)
                            bulbasaur.move(-10, 0)
                            time.sleep(0.1)
                            
            attackSound = pygame.mixer.Sound("assets/sounds/pokemonAttack.wav") # Plays an attack sound
            attackSound.play()

                ### Display Text ###
                            
            textFrame = Image(Point(600, 350), "assets/images/bigframe.gif") # The box that stores the text
            textFrame.draw(battleWin)
            
            battleText.setSize(25)
            battleText.draw(battleWin)

### Re-draws the health texts ###            
            pokemonHealth.undraw()
            pokemonHealth = Text(Point(200, 250), pokemonHp)
            pokemonHealth.setSize(36)
            pokemonHealth.draw(battleWin)
            
            enemyHealth.undraw()
            enemyHealth = Text(Point(1000, 100), enemyHp)
            enemyHealth.setSize(36)
            enemyHealth.draw(battleWin)

### Checks if one of the Pokemon have fainted ###
            if enemyHp < 1:
                endGame = True
                break
            if pokemonHp < 1:
                endgame = True
                loseGame = True
                break

            enemyAttack = random.randint(0, 4)
            
            time.sleep(1)

            battleText.undraw()

                ### Enemy Attack ###
### All of the battleText variables will change the text that appears on the screen while battling ###            
            if enemyAttack == 1:
                battleText = Text(Point(600, 350), "The opponent \nused Quick Attack!")
                pokemonHp -= 100 # This attack will deal 100 damage to your Pokemon
                
            elif enemyAttack == 2:
                battleText = Text(Point(600, 350), "The opponent \nused Body Slam!")
                pokemonHp -= 200 # This attack will deal 200 damage to your Pokemon
                
            elif enemyAttack == 3:
                battleText = Text(Point(600, 350), "The opponent \nused Earthquake!")
                pokemonHp -= 300 # This attack will deal 300 damage to your Pokemon
                
            else:
                battleText = Text(Point(600, 350), "The opponent missed \ntheir attack!")

            for i in range(3): # Enemy Animation
                if battleCount == 0:
                        pidgey.move(10, 0)
                        time.sleep(0.1)
                        pidgey.move(-10, 0)
                        time.sleep(0.1)
                elif battleCount == 1:
                        diglet.move(10, 0)
                        time.sleep(0.1)
                        diglet.move(-10, 0)
                        time.sleep(0.1)
                elif battleCount == 2:
                        onyx.move(10, 0)
                        time.sleep(0.1)
                        onyx.move(-10, 0)
                        time.sleep(0.1)

            attackSound.play() # Plays the attack sound
                            
            battleText.setSize(25)
            battleText.draw(battleWin)

            time.sleep(1)

            textFrame.undraw()
            battleText.undraw()

### Checks if one of the Pokemon have faintd ###        
            if enemyHp < 1:
                endGame = True
                break
            if pokemonHp < 1:
                endgame = True
                break

            pokemonHealth.undraw()
            pokemonHealth = Text(Point(200, 250), pokemonHp)
            pokemonHealth.setSize(36)
            pokemonHealth.draw(battleWin)
            
            enemyHealth.undraw()
            enemyHealth = Text(Point(1000, 100), enemyHp)
            enemyHealth.setSize(36)
            enemyHealth.draw(battleWin)
            
                ### Checks if one of the pokemon have fainted ###

        time.sleep(1)

### Checks who won ###        
        if enemyHp < 1: # If you won
            outcomeFrame = Image(Point(600, 350), "assets/images/bigframe.gif")
            outcomeFrame.draw(battleWin)
            winText = Text(Point(600, 350), "You Win!")
            winText.setSize(36)
            winText.draw(battleWin)
            outcomeMusic = pygame.mixer.Sound("assets/sounds/winMusic.wav")
            
        elif pokemonHp < 1: # If your opponent won
            battleCount -= 1
            outcomeMusic = pygame.mixer.Sound("assets/sounds/loseMusic.wav")
            loseWin = GraphWin("You Lose :(", 1200, 700)
            loseWinImage = Image(Point(600, 350), "assets/images/loseWinImage.gif")
            loseWinImage.draw(loseWin)

            loseMusic = pygame.mixer.Sound("assets/sounds/loseMusic.wav")
            loseMusic.play()
            time.sleep(3)

            loseWin.close()

        pygame.mixer.music.pause()
        outcomeMusic.play()
        time.sleep(1)
        pygame.mixer.music.unpause()
        battleWin.close()
        
                ### Graphics for the trainers ###

trainer1 = Image(Point(465, 390), "assets/images/redr.gif")
trainer2 = Image(Point(510, 295), "assets/images/redr.gif")
trainer3 = Image(Point(690, 480), "assets/images/redl.gif")

trainer1.draw(win)
trainer2.draw(win)
trainer3.draw(win)

def MovePlayer():

        global battleCount
        
        moveSpeed = 5 # The speed of the player

        playerX = 600 # Tracks the players x value
        playerY = 680 # Tracks the players y value

        player = Image(Point(playerX, playerY), "assets/images/front.gif") # The front view of the player
        player.draw(win)

        trophy = Image(Point(600, 200), "assets/images/trophy.gif") # The sprite for the trophy
        trophy.draw(win)
              
        while True:
                
            k = win.checkKey() # Checks if the user is pressing a key
            l = "aa" # Initiates the varibale "l" (last pressed key)
            
                ### Player Movement ###
            
            if k.lower() == "w":
                player.move(0, -moveSpeed)
                playerY -= moveSpeed
                if l != "w": # Checks if the last pressed key is not the same as the currently pressed key to save undrawing and redrawing
                        player.undraw() # Changes the sprite of the player when the player changes direction
                        player = Image(Point(playerX, playerY), "assets/images/back.gif")
                        player.draw(win)
                
            elif k.lower() == "a":
                player.move(-moveSpeed, 0)
                playerX -= moveSpeed
                if l != "a": # Checks if the last pressed key is not the same as the currently pressed key to save undrawing and redrawing
                        player.undraw() # Changes the sprite of the player when the player changes direction
                        player = Image(Point(playerX, playerY), "assets/images/facingleft.gif")
                        player.draw(win)
                
            elif k.lower() == "s":
                player.move(0, moveSpeed)
                playerY += moveSpeed
                if l != "s": # Checks if the last pressed key is not the same as the currently pressed key to save undrawing and redrawing
                        player.undraw() # Changes the sprite of the player when the player changes direction
                        player = Image(Point(playerX, playerY), "assets/images/front.gif")
                        player.draw(win)
                
            elif k.lower() == "d":
                player.move(moveSpeed, 0)
                playerX += moveSpeed
                if l != "d": # Checks if the last pressed key is not the same as the currently pressed key to save undrawing and redrawing
                        player.undraw() # Changes the sprite of the player when the player changes direction
                        player = Image(Point(playerX, playerY), "assets/images/facingright.gif")
                        player.draw(win)

            l = k.lower() # The last pressed key

                ### Battle Check ###
### Checks the players X and Y values to check if they are in the boundaries to activate a trainer battle ###
            if playerY > 475 and playerY < 485 and battleCount == 0: # Bottom
                alert = Text(Point(690, 450), "!")
                alert.setFill("red")
                alert.setSize(36)
                alert.draw(win)
                time.sleep(1)
                alert.undraw()
                pokemonBattle()
                battleCount += 1
                break
                
            elif playerY > 385 and playerY < 395 and battleCount == 1: # Middle
                alert = Text(Point(465, 360), "!")
                alert.setFill("red")
                alert.setSize(36)
                alert.draw(win)
                time.sleep(1)
                alert.undraw()
                pokemonBattle()
                battleCount += 1
                break
                
            elif playerY > 290 and playerY < 300 and battleCount == 2: # Top
                alert = Text(Point(505, 265), "!")
                alert.setFill("red")
                alert.setSize(36)
                alert.draw(win)
                time.sleep(1)
                alert.undraw()
                pokemonBattle()
                battleCount += 1
                break
                       
            elif playerY > 195 and playerY < 205 and battleCount == 3: # The boundaries for the trophy
                    battleCount += 1
                    break
           
while battleCount <= 3: # Loops until the player has reached the trophy
### Loops the game every time the player fights another trainer ###
        MovePlayer()
        win.close()
        win = GraphWin("Pokemon", 1200, 700)
        gym = Image(Point(600, 350), "assets/images/gym.gif")
        gym.draw(win)

        trophy = Image(Point(600, 200), "assets/images/trophy.gif")
        trophy.draw(win)

        trainer1.draw(win)
        trainer2.draw(win)
        trainer3.draw(win)
        
### The window that plays when the player completes the game ###
exitWin = GraphWin("Thanks for playing Pokemon!", 1200, 700)
exitScreen = Image(Point(600, 350), "assets/images/thanks4playin.gif")
exitScreen.draw(exitWin)

winMusic = pygame.mixer.Sound("assets/sounds/winMusic.wav")
pygame.mixer.music.stop()
winMusic.play()
time.sleep(3)

exitWin.close()
win.close()