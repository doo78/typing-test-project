#Modules to be used
import pygame, time, random, sqlite3, datetime, os, webbrowser

#Preparing the program

pygame.init() #initialises pygame
screen = pygame.display.set_mode([800, 700]) #creates the screen
pygame.display.set_caption("Pygame test program") #names the program
textfont = pygame.font.SysFont("monospace", 20) #Sets the font
primaryKey = "a" #Initialises the variable for later



import pygame, time

pygame.init() #Initialises pygame
screen = pygame.display.set_mode([800, 700]) #Sets the size of the screen
pygame.display.set_caption("Pygame test program") #Names the program
textfont = pygame.font.SysFont("monospace", 20) #Sets the font




#Creating the user database

new_db = sqlite3.connect("typingtest.db")
c = new_db.cursor()

#Used to clear the table contents during testing (commented out)

##c.execute("DROP TABLE Previous10")
##c.execute("DROP TABLE User")
##c.execute("DROP TABLE CustomerFeedback")
##c.execute("DROP TABLE HighScore")
##c.execute("DROP TABLE PowerUps")


##c.execute("DROP TABLE Text")


#Creates the tables

c.execute('''CREATE TABLE IF NOT EXISTS User
    (user_ID int IDENTITY(1,1) primary key,
        username text,
        password text,
        money int,
        highScore_ID text,
        foreign key(highScore_ID) REFERENCES HighScore(highScore_ID)
        foreign key(user_ID) REFERENCES Previous10(user_ID)
        foreign key(user_ID) REFERENCES PowerUps(user_ID) )''')
    
c.execute('''CREATE TABLE IF NOT EXISTS PowerUps
    (user_ID int,
    name text,
    quantity text,
    PRIMARY KEY(user_ID,name)
    foreign key(user_ID) REFERENCES User(user_ID))''')
    
c.execute('''CREATE TABLE IF NOT EXISTS HighScore
    (highScore_ID text primary key,
    wpm text,
    accuracy text,
    category text,
    difficulty text,
    dateRecord datetime,
    minigameHighScore int)''')

c.execute('''CREATE TABLE IF NOT EXISTS Previous10
    (previous10_ID int primary key,
    score int,
    accuracy int,
    dateRecord datetime,
    user_ID)''')

c.execute('''CREATE TABLE IF NOT EXISTS CustomerFeedback
    (user_ID int primary key,
    rating int,
    review text)''')

#Filling the database removed hashtag

new_db.commit()



#Creating the text database

if not os.path.isfile("text.db"): #Checks if the database already exists
    newtext_db = sqlite3.connect("text.db")
    c_new = newtext_db.cursor() #Initialises the cursor to be used
    c_new.execute('''CREATE TABLE Text
        (category text,
            difficulty text,
            example_text text,
            PRIMARY KEY(category,difficulty))''')
    
    music_easy = ("Music goes past limits and everyone can understand it. It can make you feel happy or sad or even scared. Many people live for music and it is easy to see why that is.")
    music_medium = ("Music transcends walls and boundaries and is the language that everyone understands. It has the ability to create powerful emotions and therefore it is easy to see why people live for it.")
    music_hard = ("Music surpasses all borders and boundaries; it is the language everyone can comprehend. Its attribute to illicit significant emotions convey substantially why it is a profession for many.")
    sports_easy = ("Boxing is seen as dangerous but somehow it is still popular and is the favorite sport of many people. These people see it as exciting and entertaining and it is easy to see why.")
    sports_medium = ("Boxing is seen as brutal and primitive with sometimes deadly consequences but it has survived and is a favorite sport among many fans and people who see it as exciting and entertaining.")
    sports_hard = ("By some, boxing has been portrayed as brutal, primitive, and even outright deadly and yet it has survived and continues to be a favorite sport among fans and fitness enthusiasts who see it as a thing of beauty.")
    science_easy = ("Science lets us make new technology and solve problems together or on our own. This is why it is important to teach children and as adults learn about general science and to be informed.")
    science_medium =("Science allows us to develop technology, solve problems and make important decisions together or on our own. This is exactly the reason why we should teach young people and ourselves about the topic.")
    science_hard =("Scientific knowledge allows us to develop new technologies, solve practical problems, and make informed decisions — both individually and collectively. This is precisely why it is essential for us to be involved in it.")
    animals_easy =("The rhino is one of the biggest animals. Their size and armor as well as their large horns make them very dangerous. The white rhino can weigh over 5 tonnes and stand at 6 feet tall.")
    animals_medium =("The rhino is one of the biggest animals in the animal kingdom. Their size, armor and horns make them a terrifying opponent. The white rhino can weigh over 5000 pounds and can stand at 6 feet tall.")
    animals_hard =("A Rhino is the tank of the animal kingdom. Their imposing size, their armor like skin and deadly horns makes them a formidable opponent. The white rhino can exceed over 5000 pounds, are 13 feet long, 6 feet tall and can achieve speeds of 31mph.")
    food_easy =("French cooking is seen as the most posh type of cooking in the world. It has great techniques and places importance on fresh food to cook with as well as simple flavors and pride in presentation.")
    food_medium =("French cooking is deemed to be the most respectable and posh cuisine in the world. It has technique, emphasis on cooking with fresh food and simple flavors. It is also presented very well.")
    food_hard =("French cooking is considered by many to be the most prestigious and respectable cuisine in the world. It has formal techniques, emphasis on fresh ingredients and simple flavors, pride in presentation, and rich and colorful history.")
    geography_easy =("For there to be a hurricane, there has to be warm water and wet air. When the air is flowing up in an area of low pressure over warm water, the water is release and creates the rotating storm.")
    geography_medium =("For a hurricane to form, there needs to be warm ocean water and moist, humid air in the region. When humid air is flowing upward at a zone of low pressure over warm ocean water, the water is released from the air, as creating the clouds of the storm.")
    geography_hard =("For a hurricane to manifest, it is required for there to be warm ocean water and moist, as well as humid air in the surrounding region. When the humid air is moving vertically upward at a zone of which has low pressure, the water is release, creating the clouds.")
    entertainment_easy =("Movies are exciting and give people knowledge. They let people learn about different people and places. Also, as they are easy to come across they will always be popular and always give people entertainment and knowledge.")
    entertainment_medium =("Movies provide entertainment and knowledge to people. They give people a chance to learn about different cultures and religions. Also, due to easy access, movies will continue to be popular and a great source of knowledge and entertainment.")
    entertainment_hard =("Movies provide entertainment as well as knowledge to people. They give people an opportunity to learn about different cultures, religions, and histories. In addition, due to easy accessibility, movies will continue to be popular and a great source of entertainment for many people.")
    randomWords_easy =("this wife can but is might cat house cup in to India but all your tea easy too quite lick boss yes time quite wreck time happy leg word food music egg cell country state pea mat snake")
    randomWords_medium =("should but quite mighty inside country Canada timely frame kettle punish school headmaster sprint happy trouble guitar maybe together blinds earphones scissors ruler spray lamp blind charger")
    randomWords_hard =("perhaps indiscrimately prestigous however fathom sometimes always television primitive scintillating ordeal moisture mighty suffragette party telephone recording galloping decisive measure cautiously redact")


                     
    text_tmp = [('Music','Easy',music_easy),
                    ('Music','Medium',music_medium),
                    ('Music','Hard',music_hard),
                    ('Sports','Easy',sports_easy),
                    ('Sports','Medium',sports_medium),
                    ('Sports','Hard',sports_hard),
                    ('Science','Easy',science_easy),
                    ('Science','Medium',science_medium),
                    ('Science','Hard',science_hard),
                    ('Animals','Easy',animals_easy),
                    ('Animals','Medium',animals_medium),
                    ('Animals','Hard',animals_hard),
                    ('Food','Easy',food_easy),
                    ('Food','Medium',food_medium),
                    ('Food','Hard',food_hard),
                    ('Geography','Easy',geography_easy),
                    ('Geography','Medium',geography_medium),
                    ('Geography','Hard',geography_hard),
                    ('Entertainment','Easy',entertainment_easy),
                    ('Entertainment','Medium',entertainment_medium),
                    ('Entertainment','Hard',entertainment_hard),
                    ('RandomWords','Easy',randomWords_easy),
                    ('RandomWords','Medium',randomWords_medium),
                    ('RandomWords','Hard',randomWords_hard)]

    #Inserts the texts into the database with the corresponding composite primary key               
    c_new.executemany("INSERT INTO Text VALUES (?,?,?)",text_tmp) 
    newtext_db.commit()

#Initialises the variables for use during the program
newtext_db = sqlite3.connect("text.db")
c_new = newtext_db.cursor()


#Text focusing on each part of the keyboard for the Lessons and Analysis section
top_left1 = ("neet edee jeef baed jeqee ands eegs happeeq eemda assd heen fad geed ristress eef baed jeqee ands eegs")
top_left2 = ("eef baed rest ands eegs gea uhaa dead haaq risit heea fesda jeed neet edee jeef jeqee ands eegs")
top_left3 = ("feed was dead sad said want eat assd heen fad geed stresent eef heea fesda jeed neet ands eegs")
top_left = [top_left1, top_left2, top_left3]

bottom_left1 = ("and come sack dance have zen zad faz xad xac zackal pozzing jazz zimba hazmat calm zed")
bottom_left2 = ("zack said cats have exact dance zimba zen cadence xeno salsa zackal pozzing")
bottom_left3 = ("dance have zen zad faz cats have exact zimba hazmat cadence xeno salsa")
bottom_left = [bottom_left1, bottom_left2, bottom_left3]

top_right1 = ("jelly inside pop lick jumper pay underlying jack lump kill jop list jill open oval kull pull")
top_right2 = ("jump lick open kill pull oppress junk lips inside pop lick hunk jill pull")
top_right3 = ("underlying jack lump kill pull oppress junk lips lick open kill list jill open oval")
top_right = [top_right1, top_right2, top_right3]

bottom_right1 = ("number leg len klobb number lumber basken khardi man jem mail hand mend link vann loan")
bottom_right2 = ("junk number embalm munch number vintage many ban man milk number lumber basken")
bottom_right3 = ("embalm munch number khardi man jem mail ban man milk number leg len klobb")
bottom_right = [bottom_right1, bottom_right2, bottom_right3]

middle1 = ("tonight this bust hag vat bob berry fabby hat hen great tray yes barry jav been fun grape")
middle2 = ("very get hurry punt bubble terry fit carry tour knight tray big fly berry bust")
middle3 = ("get hurry punt bubble fabby hat hen great hag vat bob berry tray yes barry jav")
middle = [middle1, middle2, middle3]

randomText = random.randint(0,2)            


#Class for a button 
class Button():
    def __init__ (self,color,x,y,width,height,text):
        #Initialises all the variables to be used in the class
        self.color=color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
    def display(self, screen, textfont, outline, outlineColor):
        if outline == True:
            pygame.draw.rect(screen, outlineColor, (self.x-2, self.y-2, self.width+4, self.height+4))
            #The dimensions have added or subtracted values so the box is bigger than the
            #next box to be drawn.
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        #Putting a smaller box over the box already made fills in the larger box
        #with the smaller box color making the larger box appear an outline instead.
        text_on_screen(self.text,self.x,self.y)
        
    def hovering(self, mousePosition):
        if mousePosition[0] > self.x and mousePosition[0] < (self.x + self.width):
            if mousePosition[1] > self.y and mousePosition[1] < (self.y + self.height):
                return True
        
        return False


#Powerups
def time_stop():

    c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Time-stop"])
    quantity = int(removeBracketsAndCommas(str(c.fetchall())))

    if quantity != 0:
    
        global timeStop_ticks
        timeStop_ticks = pygame.time.get_ticks()/1000
        
        if minigameDifficulty == "easy":
            easyBlock1.set_speed(0)
            easyBlock2.set_speed(0)
            easyBlock3.set_speed(0)
            easyBlock4.set_speed(0)
            
        if minigameDifficulty == "medium" or minigameDifficulty == "survival":
            mediumBlock1.set_speed(0)
            mediumBlock2.set_speed(0)
            mediumBlock3.set_speed(0)
            mediumBlock4.set_speed(0)
            
        if minigameDifficulty == "hard":
            hardBlock1.set_speed(0)
            hardBlock2.set_speed(0)
            hardBlock3.set_speed(0)
            hardBlock4.set_speed(0)   

        c.execute("UPDATE PowerUps SET quantity = (?) WHERE PowerUps.user_ID = (?) and PowerUps.name = (?)",[(quantity-1), user_id, "Time-stop"])
        new_db.commit()
    else:
        pass



    
def bomb():

    c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Bomb"])
    quantity = int(removeBracketsAndCommas(str(c.fetchall())))

    if quantity != 0:
        
        global bombExploding
        global bomb_ticks
        bombExploding = True
        bomb_ticks = pygame.time.get_ticks()/1000
        
        if minigameDifficulty == "easy":
            easyBlock1.explode()
            easyBlock2.explode()
            easyBlock3.explode()
            easyBlock4.explode()
            
        if minigameDifficulty == "medium" or minigameDifficulty == "survival":
            mediumBlock1.explode()
            mediumBlock2.explode()
            mediumBlock3.explode()
            mediumBlock4.explode()
            
        if minigameDifficulty == "hard":
            hardBlock1.explode()
            hardBlock2.explode()
            hardBlock3.explode()
            hardBlock4.explode()

        c.execute("UPDATE PowerUps SET quantity = (?) WHERE PowerUps.user_ID = (?) and PowerUps.name = (?)",[(quantity-1), user_id, "Bomb"])
        new_db.commit()
    else:
        pass
    




def slow_blocks():
    
    c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Slow Blocks"])
    quantity = int(removeBracketsAndCommas(str(c.fetchall())))

    if quantity != 0:
    
        global slowBlocks_ticks
        slowBlocks_ticks = pygame.time.get_ticks()/1000

        if minigameDifficulty == "easy":
            easyBlock1.half_or_double_speed("half")
            easyBlock2.half_or_double_speed("half")
            easyBlock3.half_or_double_speed("half")
            easyBlock4.half_or_double_speed("half")
            
        if minigameDifficulty == "medium" or minigameDifficulty == "survival":
            mediumBlock1.half_or_double_speed("half")
            mediumBlock2.half_or_double_speed("half")
            mediumBlock3.half_or_double_speed("half")
            mediumBlock4.half_or_double_speed("half")
            
        if minigameDifficulty == "hard":
            hardBlock1.half_or_double_speed("half")
            hardBlock2.half_or_double_speed("half")
            hardBlock3.half_or_double_speed("half")
            hardBlock4.half_or_double_speed("half")    

        c.execute("UPDATE PowerUps SET quantity = (?) WHERE PowerUps.user_ID = (?) and PowerUps.name = (?)",[(quantity-1), user_id, "Slow Blocks"])
        new_db.commit()
    else:
        pass


#Class for the block used in the minigame    
class Block():
    def __init__(self,x,y,text,speed,difficulty):

        #Initalises the variables
        self.difficulty = difficulty
        self.x = x
        self.y = y
        self.text = text
        self.speed = speed
        self.storeSpeed = speed

    #Getter and setter methods
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_text(self):
        return self.text

    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y

    def set_speed(self, speed):
        self.speed = speed
        
    def set_text(self, text):
        self.text = text

    #Displays the block using the text, x and y values.
    def display(self):
        text_on_screen(self.text,self.x,self.y)

    #Increments the y value (moving it down) by the speed
    def fall(self):
        self.y += self.speed
    
    #Checks if the block has reached the bottom of the screen
    def hitGround(self):
        
        #Global so that they are affected outside the function
        global minigameStop
        global showMinigameResults
        global rewardMoney
        
        if self.y > 650: #if the block passes the bottom
            minigameStop = True
            showMinigameResults = True
            rewardMoney = True
            
    #Checks if the user typed the correct word        
    def typed(self,input_text):
        global points
        global easy_words
        global medium_words
        global hard_words
        
        if input_text == self.text:
            self.y = 0      #Resets the block to the top of the screen
            self.x = random.randrange(0,600) #Randomly places the block along the x axis
            points +=1

            #Changes the word when it returns to the top of the screen
            if self.difficulty == "easy":                
                self.text = easy_words[random.randrange(0,9)]
                
            if self.difficulty == "medium":                
                self.text = medium_words[random.randrange(0,9)]
                
            if self.difficulty == "hard":                
                self.text = hard_words[random.randrange(0,9)]

            #Confirms that the word has been typed    
            return True
        
        else:
            return False

    def explode(self):
        
        global input_text
        
        self.y = 0
        self.x = random.randrange(0,600)
        
        if self.difficulty == "easy":                
            self.text = easy_words[random.randrange(0,9)]
            
        if self.difficulty == "medium":                
            self.text = medium_words[random.randrange(0,9)]
            
        if self.difficulty == "hard":
            self.text = hard_words[random.randrange(0,9)]

        input_text = ""
    
    def increase_speed(self, speed):

        #Used to add to the speed as oppossed to changing it
        self.speed += speed

    def half_or_double_speed(self, half_or_double):
        
        if half_or_double == "half":  #To half the speed
            self.speed = self.speed/2

        if half_or_double == "double": #To reset the speed to what it was
            self.speed = self.speed*2

    def resetSpeed(self):
        self.speed = self.storeSpeed

            
#Results procedure
def results():
    if showResults == True:
        screen.fill((255,255,255)) #To create a blank white screen
        amountOfWords = round(len(calculateAmountOfCharacters (sample_text))/5) #The average word length is 5 characters
        correct_words = accuracyCheck(input_text.split(),amountOfWords)
        accuracy = round((correct_words/amountOfWords)*100) 
        if accuracy >49:
            wpm = round(correct_words*(60/(clock-currentTime)))
            displayed_wpm = "Your typing speed is",wpm,"words per minute."
            displayed_wpm2 = str(displayed_wpm)
            text_on_screen(displayed_wpm2, 100, 100)
            highScoreUpdater(wpm, accuracy)
            recordResults(wpm, accuracy)
            
            
        else:
            accuracy_too_low = "Your accuracy must be at least 50% for your test to be valid."
            text_on_screen(accuracy_too_low, 100, 100)
        highScore()
        displayPrevious10()
        displayAverage("speed")
        displayAverage("accuracy")
        resetButton = Button((255,255,255), 600,600,100,30,"RESTART")
        resetButton.display(screen,textfont,False,(255,255,255))
        settingsButton = Button((255,255,255),400,600,100,30,"SETTINGS")
        settingsButton.display(screen,textfont,False,(255,255,255))
        pygame.display.update()

        
#Procedure to display the average typing speed
def displayAverage(speedOrAccuracy): #Using this parameter allows for code reuse
    
    #Temporary variables used to calculate the averages
    scores= []
    total = 0
    
    if speedOrAccuracy == "speed":
        a = c.execute("SELECT score FROM Previous10 WHERE Previous10.user_ID = (?) ORDER BY dateRecord",(user_id))
        b = "WPM: "
        #Will be used to make the speed and accuracy averages positionally different
        y = 0
        x = 0
    else:
        a = c.execute("SELECT accuracy FROM Previous10 WHERE Previous10.user_ID = (?) ORDER BY dateRecord",(user_id))
        b = "Accuracy: "
        y = 50
        x = 40

    #Just like in the displayPrevious10 function it
    #Displays it with brackets and a comma
        
    for row in a:

        removeFirstBracket = str(row)[1:]
        removeCommaAndBracket = removeFirstBracket[0:-2]
        scores.append(int(removeCommaAndBracket)) #Adds to the list
        
    for i in range(0,len(scores)): #Uses list values to calculate the average
        total = total + scores[i]
        
    if len(scores) != 0: #Ensures you are not dividing by 0 on the next line
        average = str(round(total/len(scores)))
        text_on_screen(b,125, 425 + y)
        text_on_screen(average,210 + x,425 + y)
        
    text_on_screen("Average:",125, 375)   
    
        

#Displays the Highscore
def highScore():
    #I used MAX to avoid the error I got before
    #and it doesn't make any difference because
    #there is only one value in the column
    c.execute("SELECT MAX(wpm) FROM HighScore WHERE highScore_ID = (?) ",(user_id))
    text_on_screen("WPM: ",125,250)
    text_on_screen(c.fetchone()[0],210,250)
    text_on_screen("High Score:",125,200)
    text_on_screen("Accuracy: ",125,300)
    c.execute("SELECT MAX(accuracy) FROM HighScore WHERE highScore_ID = (?) ",(user_id))
    text_on_screen(c.fetchone()[0],250,300)
    
#Displays the previous 10 results
def displayPrevious10():
    global record #global so that the record functions do not repeat
    global scores #this variable resets outside of the function
    global accuracies
    text_on_screen("Recent Results",470,175)
    text_on_screen("WPM", 375, 220)
    text_on_screen("Accuracy", 495, 220)
    text_on_screen("Time", 665, 220)
 
    wpmAccuracyDateDisplayer(scores,'score',0)
    wpmAccuracyDateDisplayer(accuracies,'accuracy',150)
    wpmAccuracyDateDisplayer(dates, 'dateRecord', 250)
        
    record = False


#Displays the accuracy and date of each test in the previous 10 results
def wpmAccuracyDateDisplayer(score,header,xAdder):
    global scores
    global accuracies
    global dates
    
    if record == True:  #Ensures it does not repeat after it has calculated
        if header == "score":
            
            a = c.execute("SELECT score FROM Previous10 WHERE user_ID = (?)ORDER BY dateRecord",(user_id,))
            for row in a:
                #this would return the value with brackets and commas
                #e.g. 68 would return as (68,)
                removeFirstBracket = str(row)[1:]
                removeCommaAndBracket = removeFirstBracket[0:-2]
                score = score + " " + removeCommaAndBracket
                #adding a space allows for the split function to separate them
                scores = score
            
        elif header == "accuracy":

            a = c.execute("SELECT accuracy FROM Previous10 WHERE user_ID = (?) ORDER BY dateRecord",(user_id,))
            for row in a:
                removeFirstBracket = str(row)[1:]
                removeCommaAndBracket = removeFirstBracket[0:-2]
                score = score + " " + removeCommaAndBracket +"%"
                accuracies = score
        else:

            a = c.execute("SELECT dateRecord FROM Previous10 WHERE user_ID = (?) ORDER BY dateRecord",(user_id,))
            for row in a:
                removeFirstBracket = str(row)[1:]
                removeCommaAndBracket = removeFirstBracket[0:-2]
                dateAndTime = removeCommaAndBracket [6:17] 
                b = (dateAndTime).replace(" ","|")
                score = score + " " + b

                
                
                dates = score
            
            
            
    #x adder is for accuracy because it needs a different x value
    if len(score.split()) >0:
        text_on_screen(score.split()[0], xAdder +375, 250)
    if len(score.split()) >1:
        text_on_screen(score.split()[1], xAdder +375, 280)
    if len(score.split()) >2:
        text_on_screen(score.split()[2], xAdder +375, 310)
    if len(score.split()) >3:
        text_on_screen(score.split()[3], xAdder +375, 340)
    if len(score.split()) >4:
        text_on_screen(score.split()[4], xAdder +375, 370)
    if len(score.split()) >5:
        text_on_screen(score.split()[5], xAdder +375, 400)
    if len(score.split()) >6:
        text_on_screen(score.split()[6], xAdder +375, 430)
    if len(score.split()) >7:
        text_on_screen(score.split()[7], xAdder +375, 460)
    if len(score.split()) >8:
        text_on_screen(score.split()[8], xAdder +375, 490)
    if len(score.split()) >9:
        text_on_screen(score.split()[9], xAdder +375, 520)
    
    

#Gives money for playing the minigame
def updateMoney(minigameDifficulty, points):
    global rewardMoney

    #Retrieves the user's money
    c.execute("SELECT money FROM User WHERE User.user_ID = (?)",(user_id,))
    money = int(removeBracketsAndCommas(str(c.fetchall())))

    #Money earned depends on the difficulty 
    if minigameDifficulty == "easy":
        moneyToAdd = points*10
        
    if minigameDifficulty == "medium":
        moneyToAdd = points*20
        
    if minigameDifficulty == "hard":
        moneyToAdd = points*30
        
    if minigameDifficulty == "survival":
        moneyToAdd = points*30

    newMoney = moneyToAdd + money

    #The money is updated in the database
    c.execute("UPDATE User SET money = (?) WHERE User.user_ID = (?)",[newMoney, user_id])
    new_db.commit()


    rewardMoney = False #Ensures the money is only added once
        
    return newMoney

#Records the results in the database
def recordResults(wpm, accuracy):
    global record #Retrieves and affects the global values
    global primaryKey

    if record == True and sample_text != custom_text: #This condition is used to ensure the function does not loop endlessly 
        if primaryKey<11:
            c.execute("INSERT INTO Previous10 VALUES (?,?,?,?,?)",(primaryKey,wpm,accuracy, datetime.datetime.now(),user_id))         
            new_db.commit()
            primaryKey +=1

        else:
            c.execute("SELECT previous10_ID FROM Previous10 WHERE dateRecord = (select MIN(dateRecord) from Previous10)")
            newPrimaryKey = c.fetchone()[0] #Stores the primary key of the oldest record
            
            c.execute("DELETE FROM Previous10 WHERE previous10_ID = (?)",(newPrimaryKey,)) #Deletes the oldest record
            new_db.commit() #I cannot add a value with the same primary key unless I delete the one with that primary key first

            c.execute("INSERT INTO Previous10 VALUES (?,?,?,?,?)",(newPrimaryKey,wpm,accuracy, datetime.datetime.now(),user_id))
            new_db.commit()


#Highscore Updater
def highScoreUpdater(wpm, accuracy):
    if record == True and sample_text != custom_text: #To ensure it does not infinitely occur
        
        c.execute("SELECT MAX(wpm) FROM HighScore")
        
        if c.fetchone()[0] is None: #Ensures highScore has a value as if the table is empty the value would be nothing
            highScore = 0
        else:
            c.execute("SELECT wpm FROM HighScore WHERE highScore_ID = (?)",(user_id,))
            highScore = c.fetchone()[0]
            
        if wpm > int(highScore): #Updates the highscore

            c.execute("UPDATE HighScore SET wpm = (?) WHERE highScore_ID = (?)", [wpm,user_id])
            c.execute("UPDATE HighScore SET accuracy = (?) WHERE highScore_ID = (?) ", [accuracy,user_id])
            c.execute("UPDATE HighScore SET category = (?) WHERE highScore_ID = (?)", [category,user_id])
            c.execute("UPDATE HighScore SET difficulty = (?) WHERE highScore_ID = (?)", [difficulty,user_id])
            c.execute("UPDATE HighScore SET dateRecord = (?) WHERE highScore_ID = (?)", [datetime.datetime.now(),user_id])
            new_db.commit()
            

#Retrieves from the database the sample text chosen by the user 
def retrieveSampleText():
    global sample_text
    global category
    global difficulty
    
    mycategory = (category)
    mydifficulty = (difficulty)
    
    c_new.execute("SELECT example_text FROM Text WHERE category IN (?) AND difficulty IN(?)",[mycategory,mydifficulty])
    
    #The command would return the text surrounded in brackets, commas and square brackets so I removed them
    #using the built-in replace function.
    actualText = str(c_new.fetchall())
    actualText = actualText.replace("[","")
    actualText = actualText.replace("]","")
    actualText = actualText.replace("'","")
    actualText = actualText.replace("(","")
    actualText = actualText.replace(",)","")
    sample_text = actualText

#Remove brackets and commas when retreived from database
def removeBracketsAndCommas(text):
    
    text = text.replace("[","")
    text = text.replace("]","")
    text = text.replace("'","")
    text = text.replace("(","")
    text = text.replace(",)","")

    return text
    
    
#Accuracy checker    
def accuracyCheck(input_text,amountOfWords):
    words_correct = 0
    words_incorrect = 0
    correct_words = "" #all the correct characters are added to this string
    
    words_in_example_text = sample_text.split()

    #Loops for the amount of characters in whichever out of the sample text or input text has the most characters
    if len(input_text)<len(sample_text.split()):
        for i in range (0,len(input_text)):
            
            if input_text[i] == words_in_example_text[i]:
                words_correct +=1
                correct_words = correct_words + words_in_example_text[i]
            else:
                words_incorrect +=1
    else:
        for i in range (0,len(words_in_example_text)):
            
            if input_text[i] == words_in_example_text[i]:
                words_correct +=1
                correct_words = correct_words + words_in_example_text[i]
            else:
                words_incorrect +=1        
    correct_words2 = round(len(correct_words)/5)

    

    accuracy = round((correct_words2/amountOfWords)*100)
    #displayedAccuracy = str(("Accuracy:",str(accuracy),"%"))
    displayedAccuracy = "Accuracy: " + str(accuracy) + "%"
    text_on_screen(displayedAccuracy, 100, 600)
    return correct_words2
            
#Procedure that runs when the restart button is clicked
def restartTest():
    global enter
    global start_ticks
    global input_text
    global start
    
    enter = False
    start_ticks = pygame.time.get_ticks()/1000
    input_text = ""
    start = False



#Input box
input_box = pygame.Rect(20,400,770,150)#(X,Y,Width,Height) - W and H by pixels
customerFeedback_box = pygame.Rect(20,250,770,300)


#Images
bombImg = pygame.image.load('explosion.png')
bombImg = pygame.transform.scale(bombImg,(700,700))

        
#Intro text (shown as the default sample text)
sample_text = ("Hello and welcome to the typing test that improves and tests your typing speed")


#Calculates the amount of characters in the sample_text
def calculateAmountOfCharacters (sample_text):
    amountOfCharacters = ""
    i = 0
    while i < len(sample_text):   
        if sample_text[i] != " ":
            amountOfCharacters = amountOfCharacters + sample_text[i]
        i = i+1
    return amountOfCharacters


#Procedure for buying from the minigame shop
def minigameShopPurchase(powerUpName, price):
    global displayCannotAffordMessage #So that the variable is affected outside the procedure
    
    c.execute("SELECT money FROM User WHERE User.user_ID = (?)",(user_id,)) #Retrieves the money of the user
    moneyToBeFetched = str(c.fetchall()) #Stores the money (with the commas and brackets) in a string
    money = int(removeBracketsAndCommas(moneyToBeFetched)) #Removes the commas and brackets
    
    if money >= price: #(if they can afford it)
        
        money = money - price
        c.execute("UPDATE User SET money = (?) WHERE User.user_ID = (?)",[money,user_id]) #Updates the user's money
        c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) and PowerUps.name = (?)",[user_id,powerUpName])
        quantity = 1 + int(str(removeBracketsAndCommas(str(c.fetchall())))) #Adds 1 to the quantity of the user's powerup
        c.execute("UPDATE PowerUps SET quantity = (?) WHERE PowerUps.user_ID = (?) and PowerUps.name = (?)",[quantity,user_id, powerUpName])
        new_db.commit()
        
    else:
        displayCannotAffordMessage = True
    


input_text = ("")


#block movement
def movement(block,x,y):
    screen.blit(block,(x,y))

def displayImage(image,x,y):
    screen.blit(image,(x,y))
    
#generate text
def text_on_screen(text, width, height):

    drawnText = textfont.render(text, True, (0,0,0)) #Generates the text to be drawn - True is for antialias
    text_width = drawnText.get_width()
    if width + text_width > screen.get_width(): #If the initial position plus the width
        start_position_of_next_word = 0         #is greater than the screen width...
        for x in text.split(): #Loops through each letter
            word = textfont.render(x+" ",True,(0,0,0)) #Renders word with a space
            if width + start_position_of_next_word + word.get_width() < screen.get_width(): #If the word does not go off the screen
                screen.blit(word,(width + start_position_of_next_word, height)) #Draws the word
                start_position_of_next_word = start_position_of_next_word + word.get_width() #position of next word updates by adding
                #the next word width
            else:

                start_position_of_next_word = 0 #Occurs if the word does go off the screen
                height = height +40 #Adjusts the height by 40 pixels so it is displayed under the previous text
                screen.blit(word,(width + start_position_of_next_word, height)) #Same process except with adjusted height
                start_position_of_next_word = start_position_of_next_word + word.get_width()

                
    else:
        screen.blit(drawnText,(width, height))

                
#Statistics for the analysis
def calculateAnalysisResults(section):

    global analysisResultsList #Permanently affects the nested list

    #Uses the same calculations as the main typing test
    amountOfWords = round(len(calculateAmountOfCharacters (sample_text))/5) 
    correct_words = accuracyCheck(input_text.split(),amountOfWords)
    accuracy = round((correct_words/amountOfWords)*100)
    wpm = round(correct_words*(60/(clock-currentTime)))
    
    analysisResultsList[section][1] = wpm #Changes that element of the list to the wpm
    analysisResultsList[section][2] = accuracy

#Caesur cipher encrypt   
def encode(plaintext,key):
    
    ciphertext = ""
    for c in plaintext:

        #Checks if the letter is in the alphabet
        if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": 

            ascii2 = ord(c)

           #Applies the key to the ascii value
            num = ascii2 + int(key)

            if c.isupper() == True: #Checks if it is uppercase
                if num > ord("Z"):
                    num = num -26 #Wraps around to the beginning 
            else:
                 if num > ord("z"):
                     num = num - 26

                
            ciphertext = ciphertext + chr(num)    
        else:
            ciphertext = ciphertext + c #non-letter characters are unchanged
    return ciphertext            

#Controls the movement of the blocks in the minigame
def minigameExecution(block1,block2,block3,block4):
    global input_text
    block1.display()
    block2.display()
    block3.display()
    block4.display()


    block1.fall()
    block2.fall()
    block3.fall()
    block4.fall()

    block1.hitGround()
    block2.hitGround()
    block3.hitGround()
    block4.hitGround()

    text_on_screen(input_text,300,550)

    if block1.typed(input_text) == True:
        input_text = ""
    if block2.typed(input_text) == True:
        input_text = ""
    if block3.typed(input_text) == True:
        input_text = ""
    if block4.typed(input_text) == True:
        input_text = ""


        
#Initialising variables#
#(unorganised because all they are required to do is to be stated before use)
running = True
clock = 15
enter = True
start_ticks = 0
start = False
currentTime = clock
showResults = False
showSettings = False
showSelectCategoryPage = False
showSelectTextPage = False
letterPosition = 0
showCustomiseTextPage = False
showMenu = False
showLessonOptions = False
showAnalysis = False
showTrainingOptions = False
showTraining = False
custom_text = ("")
record = True
showAnalysisResults = False
showLogin = True
showBadReviewMessage = False
scores = ""
accuracies = ""
dates = ""
difficulty = ""
category = ""
next_line = 0
trainingText = ""
section = 0 #Initialises this variable which I will use to iterate through each area of the keyboard
analysisResultsList = (["top left",0,0],["bottom left",0,0],["top right",0,0],["bottom right",0,0],["middle",0,0])
currentBox = ""
usernameText = ""
passwordText = ""
newPasswordText = ""
newUsernameText = ""
username = ""
password = ""
newPassword = ""
newUsername = ""
incorrectDetails = False
oneAccountMessage = False
add = True
usernameTaken = False
addedMessage = False
showCustomerFeedback = False
showRating = False
customerFeedbackAdded = False
showLeaderboard = False
showTypingTestLeaderboard = False
showMinigameDifficulties = False
showMinigame = False
points = 0
minigameStop = True
showTipsAndTricks = False
showMinigameResults = False
showMinigameLeaderboard = False
showMinigameShop = False
showSlowBlocksDesc = False
displayCannotAffordMessage = False
showTimeStopDesc = False
showBombDesc = False
rewardMoney = False
nextLine = True
detailsTooShort = False
rating = -1
rankingUsernames = ['N/A','N/A','N/A','N/A','N/A']
rankings = [('N/A','N/A','N/A','N/A','N/A'),('N/A','N/A','N/A','N/A','N/A'),('N/A','N/A','N/A','N/A','N/A'),('N/A','N/A','N/A','N/A','N/A'),('N/A','N/A','N/A','N/A','N/A')]
category = "N/A"
difficulty = "N/A"
minigameUsernames = ['N/A','N/A','N/A','N/A','N/A']
minigameRankings = [('N/A','N/A'),('N/A','N/A'),('N/A','N/A'),('N/A','N/A'),('N/A','N/A')]
#User_ID


#Minigame variables
slowBlocks_ticks = 100000000
timeStop_ticks = 10000000000
bombExploding = False
bomb_ticks = 1000000

#Instantiates the block objects
block1 = Block (100,100,"hello",0.1,"easy")
block2 = Block (200,100,"bow",0.2,"medium")
block3 = Block (300,100,"gun",0.25,"hard")
block4 = Block (400,100,"tower",0.15,"easy")

#Lists of words for each difficulty
easy_words = ("bob","hello","hi","yes","bark","able","free","tell","live")
medium_words =("still","jail","chair","table","boxer","piano","backpack","glass","ruler")
hard_words = ("although","sometimes","happen","industry","extreme","surprising","geography","killer","laptop")

#Determines what the primary key starts as
c.execute("SELECT MAX(previous10_ID) FROM Previous10") #Selects the max value of the primary key
if c.fetchone()[0] is None: #If there is no primary key yet it starts at 1
    primaryKey = 1
else:
    c.execute("SELECT MAX(previous10_ID) FROM Previous10")
    primaryKey =(c.fetchone()[0])+1 #Makes the next primary key 1 more than the last one

    
#Creates primary key for user 
def createPrimaryKey():    

    c.execute("SELECT MAX(user_ID) FROM User") #Selects the max value of the primary key
    if c.fetchone()[0] is None: #If there is no primary key yet it starts at 1
        userPrimaryKey = 1
    else:
        c.execute("SELECT MAX(user_ID) FROM User")
        userPrimaryKey =(c.fetchone()[0])+1 #Makes the next primary key 1 more than the last one

    return userPrimaryKey


    
# Game loop
while running == True:

    
    #Starts the main test)    
    if enter == False and start == True:

        accuracies = ""
        scores = ""
        dates = ""
        record = True
        currentTime = clock - (pygame.time.get_ticks()/1000 - start_ticks) 

        #Stops the test
        if currentTime <0:
            enter = True

    #Reverses the effects of the powerups
    if showMinigame == True:

        if  pygame.time.get_ticks()/1000 - slowBlocks_ticks > 2:
            
            if minigameDifficulty == "easy":
                easyBlock1.half_or_double_speed("double") #Reverses the powerup
                easyBlock2.half_or_double_speed("double")
                easyBlock3.half_or_double_speed("double")
                easyBlock4.half_or_double_speed("double")
                
            if minigameDifficulty == "medium" or minigameDifficulty == "survival":
                mediumBlock1.half_or_double_speed("double")
                mediumBlock2.half_or_double_speed("double")
                mediumBlock3.half_or_double_speed("double")
                mediumBlock4.half_or_double_speed("double")
                
            if minigameDifficulty == "hard":
                hardBlock1.half_or_double_speed("double")
                hardBlock2.half_or_double_speed("double")
                hardBlock3.half_or_double_speed("double")
                hardBlock4.half_or_double_speed("double")
                
            slowBlocks_ticks = 10000000000000000000000 #explained in documentation

        if  pygame.time.get_ticks()/1000 - timeStop_ticks > 2:
            
            if minigameDifficulty == "easy":
                easyBlock1.resetSpeed()
                easyBlock2.resetSpeed()
                easyBlock3.resetSpeed()
                easyBlock4.resetSpeed()
                
            if minigameDifficulty == "medium" or minigameDifficulty == "survival":
                mediumBlock1.resetSpeed()
                mediumBlock2.resetSpeed()
                mediumBlock3.resetSpeed()
                mediumBlock4.resetSpeed()
                
            if minigameDifficulty == "hard":
                hardBlock1.resetSpeed()
                hardBlock2.resetSpeed()
                hardBlock3.resetSpeed()
                hardBlock4.resetSpeed()
                
            timeStop_ticks = 10000000000000000000000
            
    for event in pygame.event.get():

        
        mousePosition = pygame.mouse.get_pos() # Returns the x and y position of the mouse
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:#When a key is pressed
            
            if showCustomiseTextPage == True:
                if event.key == pygame.K_BACKSPACE:
                    custom_text = custom_text[0:-1] 
                    
                else:
                    custom_text += event.unicode

            #Variables for the test
            if start == False:
                start_ticks = pygame.time.get_ticks()/1000

            if enter == False:
                start = True

            #Activates the powerups
            if event.key == pygame.K_1 and showMinigame == True:
                slow_blocks()
                
            if event.key == pygame.K_2 and showMinigame == True:
                time_stop()
                
            if event.key == pygame.K_3 and showMinigame == True:
                bomb()

            
            #Allows backspace to work as intended    
            if event.key == pygame.K_BACKSPACE:
                
                if showLogin == True:

                    #Ensures the backspace applies to the login page as well
                    if currentBox == "username":
                        usernameText = usernameText[0:-1]
                        
                    elif currentBox == "password":
                        passwordText = passwordText[0:-1]
                        
                    elif currentBox == "new password":
                        newPasswordText = newPasswordText[0:-1]
                        
                    elif currentBox == "new username":
                        newUsernameText = newUsernameText[0:-1]
                else:
                    input_text = input_text[0:-1]      


                  
                  
            elif event.key == pygame.K_RETURN:

                if showMinigame == True:
                    
                    if minigameStop == True: #If it hasn't started
                        minigameStop = False #then start
                        input_text = ""      #Removes the "press enter to start" text
                        
                            
                        if minigameDifficulty == "easy":
                            easyBlock1.set_y(0)
                            easyBlock2.set_y(0)
                            easyBlock3.set_y(0)
                            easyBlock4.set_y(0)
                            
                        if minigameDifficulty == "medium":
                            mediumBlock1.set_y(0)
                            mediumBlock2.set_y(0)
                            mediumBlock3.set_y(0)
                            mediumBlock4.set_y(0)
                            
                        if minigameDifficulty == "hard":
                            hardBlock1.set_y(0)
                            hardBlock2.set_y(0)
                            hardBlock3.set_y(0)
                            hardBlock4.set_y(0)

                        if minigameDifficulty == "survival":
                            mediumBlock1.set_y(0)
                            mediumBlock2.set_y(0)
                            mediumBlock3.set_y(0)
                            mediumBlock4.set_y(0)
                            
                            mediumBlock1.set_speed(0.1)
                            mediumBlock2.set_speed(0.2)
                            mediumBlock3.set_speed(0.25)
                            mediumBlock4.set_speed(0.15)
                            
                            
                        showMinigameResults == False
                        points = 0

                    if showMinigameResults == True:
                        showMinigameResults == False
                       
                #Calculations for the anaylsis section
                if start == True:
                    #Ensures the results are only displayed for the main typing test
                    if showAnalysis != True and showAnalysisResults != True and showMenu != True:
                        showResults = True
                        enter = True

                    
                        
                    elif section == 0:
                        
                        sample_text = top_left[0] #Changes the display text
                                                  #to the next section
                        start = False
                        enter = False
                        input_text = "" #Resets the input box
                        
                       
                    elif section == 1:
                        calculateAnalysisResults(0) #Calculates and records
                                                    #the results for that
                                                    #section
                        sample_text = bottom_left[0]
                        start = False
                        enter = False
                        input_text = ""
                        
                        
                    elif section == 2:
                        calculateAnalysisResults(1)
                        sample_text = top_right[0]
                        start = False
                        enter = False
                        input_text = ""
                        
                        
                    elif section == 3:
                        calculateAnalysisResults(2)
                        sample_text = bottom_right[0]
                        start = False
                        enter = False
                        input_text = ""
                        

                    elif section == 4:
                        calculateAnalysisResults(3)
                        sample_text = middle[0]
                        start = False
                        enter = False
                        input_text = ""
                        

                    elif section == 5:
                        calculateAnalysisResults(4)
                        start = False
                        
                        showAnalysisResults = True
                        

                    section = section +1
                    

                  
            else:

                #Ignores powerup inputs and the spacebar as part of the input text
                if showMinigame == True and (event.key == pygame.K_SPACE or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3):
                    pass
                else:
                    input_text += event.unicode#Adds the character pushed to the string

                if currentBox == "username":    #Checks which box is being typed in
                    if len(usernameText)<17:    #Limits the length of the username
                        usernameText += event.unicode
                        
                elif currentBox == "password":
                    if len(passwordText)<17:
                        passwordText += event.unicode #Adds the character typed to
                                                      #the variable
                        
                elif currentBox == "new password":
                    if len(newPasswordText)<17:
                        newPasswordText += event.unicode
                        
                elif currentBox == "new username":
                    if len(newUsernameText)<17:
                        newUsernameText += event.unicode


             

                

        #When you click...
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            #Results page
            resetButton = Button((255,255,255),600,600,100,30,"RESTART")
            settingsButton = Button((255,255,255),400,600,100,30,"SETTINGS")
            if resetButton.hovering(mousePosition) == True and enter == True:
                enter = False
                start_ticks = pygame.time.get_ticks()/1000
                input_text = ""
                start = False
            if settingsButton.hovering(mousePosition) == True and enter == True:
                showResults = False
                showSettings = True
                screen.fill((255,255,255))
         
            #Main typing test buttons
            backButton = Button ((255,255,255),100,600,100,30,"BACK")

            ##Buttons##

            #(Required to be within the game loop to work)
            
            #Tips and tricks buttons
            tipsAndTricksBackButton = Button ((255,255,255),600,650,50,30,"BACK")
            generalTips1Button = Button ((255,255,255),250,400,70,30,"CLICK")
            generalTips2Button = Button ((255,255,255),350,400,70,30,"CLICK")
            generalTips3Button = Button ((255,255,255),450,400,70,30,"CLICK")
            benefits1Button = Button ((255,255,255),500,500,70,30,"CLICK")
            benefits2Button = Button ((255,255,255),600,500,70,30,"CLICK")            
            drawbacksButton = Button ((255,255,255),450,600,70,30,"CLICK")
            
            #Settings page buttons
            fifthteenButton = Button((255,255,255),300,100,100,30,"")
            thirtyButton = Button ((255,255,255),500,100,100,30,"")
            sixtyButton = Button ((255,255,255),700,100,100,30,"")
            settingsBackButton = Button((255,255,255),100,400,100,30,"BACK")
            customiseTextButton = Button ((255,255,255),100,300,200,30,"CUSTOMISE TEXT")

            #Customise text page buttons
            customiseTextBackButton = Button((255,255,255),100,450,100,30,"BACK")
            customiseTextEraseButton = Button ((255,255,255),700,450,100,30,"ERASE")

            #Select text/difficulty page buttons
            selectTextButton = Button((255,255,255),100,200,100,30,"SELECT TEXT")
            easyButton = Button ((255,255,255),130,350,100,30,"EASY")
            mediumButton = Button ((255,255,255),360,350,100,30,"MEDIUM")
            hardButton = Button ((255,255,255),590,350,100,30,"HARD")

            #Select category page buttons
            musicButton = Button ((255,255,255),30,350,100,30,"MUSIC")
            sportsButton = Button ((255,255,255),230,350,100,30,"SPORTS")
            scienceButton = Button ((255,255,255),430,350,100,30,"SCIENCE")
            animalsButton = Button ((255,255,255),630,350,100,30,"ANIMALS")
            foodButton = Button ((255,255,255),30,450,100,30,"FOOD")
            geographyButton = Button ((255,255,255),230,450,100,30,"GEOGRAPHY")        
            entertainmentButton = Button ((255,255,255),430,450,100,30,"ENTERTAINMENT")
            randomWordsButton = Button ((255,255,255),630,450,100,30,"RANDOM WORDS")

            #Menu buttons
            tipsAndTricksButton = Button ((255,255,255),325,550,100,30,"Tips & Tricks")
            leaderBoardButton = Button ((255,255,255),350,450,100,30,"Leaderboard")
            customerFeedbackButton = Button ((255,255,255),300,350,100,30,"Customer-feedback")
            minigameButton = Button ((255,255,255),350,250,100,30,"Minigame")
            lessonsButton = Button ((255,255,255),350,150,100,30,"Lessons")
            typingtestButton = Button ((255,255,255),325,50,100,30,"Typing Test")
            
            #Lesson options buttons
            analysisButton = Button ((255,255,255),200,350,100,30,"Analysis")
            trainingButton = Button ((255,255,255),500,350,100,30,"Training")
            lessonOptionBackButton = Button ((255,255,255),100,550,100,30,"BACK")
            

            #Training options Buttons
            topLeftButton = Button ((255,255,255),100,200,100,30,"Top Left")
            bottomLeftButton = Button ((255,255,255),100,500,100,30,"Bottom Left")
            topRightButton = Button ((255,255,255),600,200,100,30,"Top Right")
            bottomRightButton = Button ((255,255,255),600,500,100,30,"Bottom Right")
            middleButton = Button ((255,255,255),375,350,100,30,"Middle")
            trainingOptionBackButton = Button ((255,255,255),100,625,100,30,"BACK")

            #Training buttons
            trainingResetButton = Button ((255,255,255),700,550,100,30,"RESET")
            trainingBackButton = Button ((255,255,255),100,550,100,30,"RESET")

            #Analysis Results buttons
            analysisResultsBackButton = Button ((255,255,255),700,50,100,30,"BACK")

            #Login page buttons
            usernameButton = Button ((255,255,255),250,100,220,30,usernameText)
            passwordButton = Button ((255,255,255),250,200,220,30,passwordText)
            newUsernameButton = Button ((255,255,255),250,400,220,30,newUsernameText)
            newPasswordButton = Button ((255,255,255),250,500,220,30,newPasswordText)
            confirmButton = Button ((255,255,255),600,150,100,30,"CONFIRM")
            addButton = Button ((255,255,255),600,450,100,30,"ADD")

            #Customer feedback buttons
            oneButton = Button((255,255,255),50,100,50,30,"1")
            twoButton = Button ((255,255,255),125,100,50,30,"2")
            threeButton = Button ((255,255,255),200,100,50,30,"3")
            fourButton = Button((255,255,255),275,100,50,30,"4")
            fiveButton = Button ((255,255,255),350,100,50,30,"5")
            sixButton = Button ((255,255,255),425,100,50,30,"6")
            sevenButton = Button((255,255,255),500,100,50,30,"7")
            eightButton = Button ((255,255,255),575,100,50,30,"8")
            nineButton = Button ((255,255,255),650,100,50,30,"9")
            tenButton = Button ((255,255,255),725,100,50,30,"10")
            customerFeedbackSubmitButton = Button ((255,255,255),350,600,100,30,"SUBMIT")
            customerFeedbackBackButton = Button ((255,255,255),100,600,100,30,"BACK")

            #Leaderboard buttons
            typingTestLeaderboardButton = Button ((255,255,255),100,350,200,30,"Typing test rankings")
            minigameLeaderboardButton = Button ((255,255,255),500,350,200,30,"Minigame rankings")
            typingTestLeaderboardBackButton = Button ((255,255,255),50,650,100,30,"BACK")
            minigameLeaderboardBackButton = Button ((255,255,255),50,650,100,30,"BACK")  

            #Minigame Difficulty buttons
            minigameEasyButton = Button((255,255,255),180,300,100,30,"Easy")
            minigameMediumButton = Button ((255,255,255),380,300,100,30,"Medium")
            minigameHardButton = Button ((255,255,255),580,300,100,30,"Hard")
            minigameSurvivalButton = Button ((255,255,255),380,500,100,30,"Survival")

            #Minigame Buttons
            minigameBackButton = Button ((255,255,255),50,650,100,30,"BACK")
            minigameContinueButton = Button((255,255,255),600,650,100,30,"CONTINUE")

            buySlowBlocksButton = Button((255,255,255),300,250,50,30,"BUY")
            descSlowBlocksButton = Button ((255,255,255),400,250,50,30,"DESC")
            
            buyTimeStopButton = Button((255,255,255),300,350,50,30,"BUY")
            descTimeStopButton = Button ((255,255,255),400,350,50,30,"DESC")

            buyBombButton = Button((255,255,255),300,450,50,30,"BUY")
            descBombButton = Button ((255,255,255),400,450,50,30,"DESC")             

            #Main typing test button operations
            if backButton.hovering(mousePosition) == True and enter == False: 
                showMenu = True
                enter = True
                start = False
                start_ticks = pygame.time.get_ticks()/1000
                
                
            #Customise text button
            if customiseTextButton.hovering(mousePosition) == True and showSettings == True:
                showSettings = False
                showCustomiseTextPage = True

            #Erase button in customise text page
            if customiseTextEraseButton.hovering(mousePosition) == True and showCustomiseTextPage == True:
                custom_text = ("")
                
            #Back button in customise text page    
            if customiseTextBackButton.hovering(mousePosition) == True and len(custom_text)>70 and len(custom_text)<150:
                
                showCustomiseTextPage = False
                screen.fill((255,255,255))
                showSettings = True
                
            #Select text button in the settings
            if selectTextButton.hovering(mousePosition) == True and showSettings == True:
                showSettings = False
                showSelectTextPage = True

            #What clicking the difficulty buttons does
            if easyButton.hovering(mousePosition) == True and showSelectTextPage == True:
                difficulty = ("Easy")
                showSelectTextPage = False
                showSelectCategoryPage = True
            if mediumButton.hovering(mousePosition) == True and showSelectTextPage == True:
                difficulty = ("Medium")
                showSelectTextPage = False
                showSelectCategoryPage = True
            if hardButton.hovering(mousePosition) == True and showSelectTextPage == True:
                difficulty = ("Hard")
                showSelectTextPage = False
                showSelectCategoryPage = True

            #What clicking the category buttons does
            if musicButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("Music")
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
            if sportsButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("Sports")                
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
            if scienceButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("Science")                
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
            if animalsButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("Animals")                
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
            if foodButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("Food")                
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
            if geographyButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("Geography")                
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
            if entertainmentButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("Entertainment")                
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
            if randomWordsButton.hovering(mousePosition) == True and showSelectCategoryPage == True:
                category = ("RandomWords")                
                showSelectCategoryPage = False
                retrieveSampleText()
                restartTest()
                
                
            #Back button in the settings            
            if settingsBackButton.hovering(mousePosition) == True and showSettings == True:
                showSettings = False
                enter = False
                start_ticks = pygame.time.get_ticks()/1000
                input_text = ""
                start = False

            if tipsAndTricksBackButton.hovering(mousePosition) == True and showTipsAndTricks == True:
                showMenu = True
                showTipsAndTricks = False

            #What clicking the timer buttons does
            if fifthteenButton.hovering(mousePosition) == True and showSettings == True:
                clock = 15
                
            elif thirtyButton.hovering(mousePosition) == True and showSettings == True:
                clock = 30
                
            elif sixtyButton.hovering(mousePosition) == True and showSettings == True:
                clock = 60
                
            #What clicking the menu buttons do
            if typingtestButton.hovering(mousePosition) == True and showMenu == True:
                enter = False
                showMenu = False
                
            if lessonsButton.hovering(mousePosition) == True and showMenu == True:
                showLessonOptions = True
                showMenu = False

            if customerFeedbackButton.hovering(mousePosition) == True and showMenu == True:
                showCustomerFeedback = True
                showMenu = False
                
            if tipsAndTricksButton.hovering(mousePosition) == True and showMenu == True:
                showTipsAndTricks = True
                showMenu = False
                
            #What clicking the lesson option buttons do
            if trainingButton.hovering(mousePosition) == True and showLessonOptions == True:
                showTrainingOptions = True
                showLessonOptions = False
                
            if analysisButton.hovering(mousePosition) == True and showLessonOptions == True:
                showAnalysis = True
                showLessonOptions = False

            if lessonOptionBackButton.hovering(mousePosition) == True and showLessonOptions == True:
                showMenu = True
                showLessonOptions = False

            #What clicking the training options buttons do
            if topLeftButton.hovering(mousePosition) == True and showTrainingOptions == True:
                keyboardPosition = top_left #Selects the area of the keyboard
                showTraining = True
                showTrainingOptions = False
                
            if bottomLeftButton.hovering(mousePosition) == True and showTrainingOptions == True:
                keyboardPosition = bottom_left
                showTraining = True
                showTrainingOptions = False
                
            if topRightButton.hovering(mousePosition) == True and showTrainingOptions == True:
                keyboardPosition = top_right
                showTraining = True
                showTrainingOptions = False
                
            if bottomRightButton.hovering(mousePosition) == True and showTrainingOptions == True:
                keyboardPosition = bottom_right
                showTraining = True
                showTrainingOptions = False
                
            if middleButton.hovering(mousePosition) == True and showTrainingOptions == True:
                keyboardPosition = middle
                showTraining = True
                showTrainingOptions = False

            if trainingOptionBackButton.hovering(mousePosition) == True and showTrainingOptions == True:
                showTrainingOptions = False
                showLessonOptions = True
                
            #What clicking the training buttons do
            if trainingResetButton.hovering(mousePosition) == True and showTraining == True:
                randomText = random.randint(0,2) #Re-generates the random number
                trainingText = top_left[randomText] #Reassigns the random text
                input_text = ""                     #Clears the text box
                
            if trainingBackButton.hovering(mousePosition) == True and showTraining == True:
                showTrainingOptions = True   #Goes back to the training option screen
                showTraining = False

            #What clicking the analyis results buttons do
            if analysisResultsBackButton.hovering(mousePosition) == True and showAnalysisResults == True:
                showMenu = True
                showAnalysisResults = False

            #What the login page buttons do
            if usernameButton.hovering(mousePosition) == True and showLogin == True:
                currentBox = "username" #Used to identify which box the user is typing in
                
            if passwordButton.hovering(mousePosition) == True and showLogin == True:
                currentBox = "password"
                
            if newUsernameButton.hovering(mousePosition) == True and showLogin == True:
                currentBox = "new username"
                
            if newPasswordButton.hovering(mousePosition) == True and showLogin == True:
                currentBox = "new password"
                
            if confirmButton.hovering(mousePosition) == True and showLogin == True:

                #Encrypts the password so it matches the one in the database
                checkEncryptedPassword = encode(passwordText,5)
                
                c.execute("SELECT MAX(username) FROM User WHERE password = (?)",(checkEncryptedPassword,))

                if c.fetchone()[0] is None:     #If there is no username with that password
                    incorrectDetails = True     #Displays the incorrect details message

                c.execute("SELECT MAX(username) FROM User WHERE password = (?)",(checkEncryptedPassword,))
                if usernameText == c.fetchone()[0]:

                    #Grants access
                    c.execute("SELECT MAX(user_ID) FROM User WHERE password = (?)",(checkEncryptedPassword,))
                    user_id = str(c.fetchone()[0])
                    
                    showMenu = True
                    showLogin = False
                    
                else:
                    incorrectDetails = True     #Displays the incorrect details message
                    usernameText = ""           #Resets the boxes
                    passwordText = ""
                    
            if addButton.hovering(mousePosition) == True and showLogin == True:

                if len(newUsernameText)>2 and len(newPasswordText)>2:
                        

                    if add == True: #Ensures the user cannot add more than one account

                        detailsTooShort = False
                        
                        c.execute("SELECT MAX(username) FROM User WHERE username = (?)",(newUsernameText,))
                        
                        if c.fetchone()[0] is None:
                            encryptedPassword = encode(newPasswordText,5) #Encrypts the password

                            user_id = createPrimaryKey()
                            
                            c.execute("INSERT INTO User(user_ID,username,password,money) VALUES (?,?,?,?)",(user_id ,newUsernameText,encryptedPassword,0))
                            c.execute("INSERT INTO HighScore VALUES (?,?,?,?,?,?,?)",(user_id,0,0, category,difficulty, datetime.datetime.now(),"N/A"))
                            c.execute("INSERT INTO CustomerFeedback VALUES (?,?,?)",(user_id, "", ""))
                            c.execute("INSERT INTO PowerUps VALUES (?,?,?)",(user_id, "Slow Blocks", 0))
                            c.execute("INSERT INTO PowerUps VALUES (?,?,?)",(user_id, "Time-stop", 0))
                            c.execute("INSERT INTO PowerUps VALUES (?,?,?)",(user_id, "Bomb", 0))
                            new_db.commit()
                            newUsernameText = ""
                            newPasswordText = ""
                            add = False             #Ensures the user cannot add more than one account
                            addedMessage = True     #Displays the message saying that the account was added
                            
                        else:
                            usernameTaken = True    #Displays the message
                            newUsernameText = ""
                            newPasswordText = ""                        
                    else:
                        newUsernameText = ""
                        newPasswordText = ""
                        oneAccountMessage = True    #Displays the message
                else:
                    detailsTooShort = True
                    
            #What the customer feedback buttons do
            if oneButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 1        #Sets the rating
                showRating = True #Displays the rating message
            if twoButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 2
                showRating = True
            if threeButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 3
                showRating = True
            if fourButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 4
                showRating = True
            if fiveButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 5
                showRating = True
            if sixButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 6
                showRating = True
            if sevenButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 7
                showRating = True
            if eightButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 8
                showRating = True
            if nineButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 9
                showRating = True
            if tenButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                rating = 10
                showRating = True

            if customerFeedbackSubmitButton.hovering(mousePosition) == True and showCustomerFeedback == True:

                if rating > 0:
                    
                                        
                    c.execute("UPDATE CustomerFeedback SET rating = (?) WHERE user_ID = (?)",[rating,user_id])    #Adds the rating given
                    c.execute("UPDATE CustomerFeedback SET review = (?) WHERE user_ID = (?)",[input_text,user_id])#Adds the review
                    f = open("Customer-feedback", "a") #Opens and allows me to append to the file
                    f.write("\n---------------------------------------") #Separates each review
                    c.execute("SELECT username FROM User WHERE user_ID = (?)",(user_id,))
                    f.write("\nUsername:")
                    f.write(removeBracketsAndCommas(str(c.fetchall()))) #Displays the username
                    f.write("\nRating:")
                    f.write(str(rating)) #Displays the rating
                    f.write("\n")
                    f.write(input_text) #Dispays the review
                    f.close()
                    customerFeedbackAdded = True #Allows the message to be displayed 
                
                else:
                    showBadReviewMessage = True
                
                
                
            
                new_db.commit()
                
            if customerFeedbackBackButton.hovering(mousePosition) == True and showCustomerFeedback == True:
                showMenu = True
                showCustomerFeedback = False

            if leaderBoardButton.hovering(mousePosition) == True and showMenu == True:
                showLeaderboard = True
                showMenu = False

            if typingTestLeaderboardButton.hovering(mousePosition) == True and showLeaderboard == True:
                showTypingTestLeaderboard = True
                showLeaderboard = False

            if typingTestLeaderboardBackButton.hovering(mousePosition) == True and showTypingTestLeaderboard == True:
                showTypingTestLeaderboard = False
                showMenu = True
                
            if minigameBackButton.hovering(mousePosition) == True and showMinigameLeaderboard == True:
                showMinigameLeaderboard = False
                showMenu = True
                
            if minigameLeaderboardButton.hovering(mousePosition) == True and showLeaderboard == True:
                showMinigameLeaderboard = True
                showLeaderboard = False
                

            if minigameButton.hovering(mousePosition) == True and showMenu == True:
                showMinigameShop = True
                showMenu = False

            if minigameEasyButton.hovering(mousePosition) == True and showMinigameDifficulties == True:
                minigameDifficulty = "easy"         #Sets the difficulty
                showMinigameDifficulties = False    #Hides the difficulty selection
                showMinigame = True                 #Displays the minigame
                
            if minigameMediumButton.hovering(mousePosition) == True and showMinigameDifficulties == True:
                minigameDifficulty = "medium"
                showMinigameDifficulties = False
                showMinigame = True
                
            if minigameHardButton.hovering(mousePosition) == True and showMinigameDifficulties == True:
                minigameDifficulty = "hard"
                showMinigameDifficulties = False
                showMinigame = True
                
            if minigameSurvivalButton.hovering(mousePosition) == True and showMinigameDifficulties == True:
                minigameDifficulty = "survival"
                showMinigameDifficulties = False
                showMinigame = True

            if minigameBackButton.hovering(mousePosition) == True and showMinigame == True:
                showMinigame = False
                showMenu = True
                showMinigameResults = False

            #Minigame Shop buttons functionality

            if descSlowBlocksButton.hovering(mousePosition) == True and showMinigameShop == True:
                showSlowBlocksDesc = True
                showTimeStopDesc = False
                showBombDesc = False
                
            if descTimeStopButton.hovering(mousePosition) == True and showMinigameShop == True:
                showTimeStopDesc = True
                showBombDesc = False
                showSlowBlocksDesc = False

            if descBombButton.hovering(mousePosition) == True and showMinigameShop == True:
                showBombDesc = True
                showTimeStopDesc = False
                showSlowBlocksDesc = False
                
            if buySlowBlocksButton.hovering(mousePosition) == True and showMinigameShop == True:
                displayCannotAffordMessage = False #Hides the message if it was visible before
                minigameShopPurchase("Slow Blocks", 250) #Calls the procedure

            if buyTimeStopButton.hovering(mousePosition) == True and showMinigameShop == True:
                displayCannotAffordMessage = False
                minigameShopPurchase("Time-stop", 500)
                
            if buyBombButton.hovering(mousePosition) == True and showMinigameShop == True:
                displayCannotAffordMessage = False
                minigameShopPurchase("Bomb", 1000)

            if minigameContinueButton.hovering(mousePosition) == True and showMinigameShop == True:
                showMinigameShop = False
                showMinigameDifficulties = True
                
            if generalTips1Button.hovering(mousePosition) == True and showTipsAndTricks == True:
                webbrowser.open("https://www.ratatype.com/learn/#:~:text=Limit%20your%20hand%20and%20finger,since%20they%20are%20considerably%20underdeveloped.")

            if generalTips2Button.hovering(mousePosition) == True and showTipsAndTricks == True:
                webbrowser.open("https://www.wikihow.com/Type-Faster")
                
            if generalTips3Button.hovering(mousePosition) == True and showTipsAndTricks == True:
                webbrowser.open("https://www.hongkiat.com/blog/faster-keyboard-typing/")
                   
            if benefits1Button.hovering(mousePosition) == True and showTipsAndTricks == True:
                webbrowser.open("https://funtech.co.uk/latest/how-touch-typing-is-an-essential-skill-all-children-should-learn")

            if benefits2Button.hovering(mousePosition) == True and showTipsAndTricks == True:
                webbrowser.open("https://adamfortgo.wordpress.com/2014/06/25/benefits-of-touch-typing-skills/")

            if drawbacksButton.hovering(mousePosition) == True and showTipsAndTricks == True:
                webbrowser.open("http://www.jointventurephysiotherapy.com/blog/repetitive-strain-injury-rsi-from-computer-use")
            

    #Main typing test
    if enter == False:
        #background colour        
        screen.fill((255, 255, 255))
        
     


        #Generate input box
        pygame.draw.rect(screen,(0,0,0),input_box,2)#(surface to draw on, colour, shape, border width)
        
        #generate text
        text_on_screen(sample_text, 100, 100)
        text_on_screen(input_text,22,400)
        
        

        #timer
        displayedTimer = textfont.render(str(round(currentTime)),True,(0,0,0))
        screen.blit(displayedTimer,(50,50))

        #back button
        backButton = Button ((255,255,255),100,600,100,30,"BACK")
        backButton.display(screen, textfont, True,(255,255,255))
        

    
    
    #success event
    if enter == True:
        results()
        pygame.display.update()

    
    #Settings
    if showSettings == True:
        
        #Shows the timers
        text_on_screen("Timer:",100,100)
        text_on_screen("15",300,100)
        text_on_screen("30",500,100)
        text_on_screen("60",700,100)
        
        #Creates all the buttons
        
        #Timer buttons
        fifthteenButton = Button((255,255,255),300,100,100,30,"15")
        thirtyButton = Button ((255,255,255),500,100,100,30,"30")
        sixtyButton = Button ((255,255,255),700,100,100,30,"60")
        
        #Back button
        settingsBackButton = Button((255,255,255),100,400,100,30,"BACK")
        settingsBackButton.display(screen, textfont, False, (0,0,0))
        
        #Customise text button
        customiseTextButton = Button ((255,255,255),100,300,200,30,"CUSTOMISE TEXT")
        customiseTextButton.display(screen, textfont, False, (0,0,0))

        #Select text button
        selectTextButton = Button((255,255,255),100,200,100,30,"SELECT TEXT")
        selectTextButton.display(screen, textfont, False, (0,0,0))
        
        #Adds box outline to selected time and removes it from others
        if clock == 15:
            fifthteenButton.display(screen, textfont, True, (0,0,0))
            thirtyButton.display(screen, textfont, True,(255,255,255))
            sixtyButton.display(screen, textfont, True,(255,255,255))
        elif clock ==30:
            thirtyButton.display(screen, textfont, True,(0,0,0))
            fifthteenButton.display(screen, textfont, True,(255,255,255))
            sixtyButton.display(screen, textfont, True,(255,255,255))
        elif clock == 60:
            sixtyButton.display(screen, textfont, True,(0,0,0))
            fifthteenButton.display(screen, textfont, True,(255,255,255))
            thirtyButton.display(screen, textfont, True,(255,255,255))                        

    #Customise text page
    if showCustomiseTextPage == True:
        screen.fill((255,255,255))
        text_on_screen("TYPE TO ADD CUSTOM TEXT",275,50)

        text_on_screen(custom_text, 100, 100)
        sample_text = custom_text
        
        if len(custom_text)>70 and len(custom_text)<150:
            customiseTextBackButton.display(screen, textfont, False, (0,0,0))
            customiseTextBackButton = Button((255,255,255),100,450,100,30,"BACK")
        customiseTextEraseButton = Button ((255,255,255),700,450,100,30,"ERASE")
        customiseTextEraseButton.display(screen,textfont, False, (0,0,0))
    pygame.display.update()

    #Select text/difficulty page
    if showSelectTextPage == True:
        screen.fill((255,255,255))
        text_on_screen("SELECT DIFFICULTY",300,50)
        easyButton = Button ((255,255,255),130,350,100,30,"EASY")
        mediumButton = Button ((255,255,255),360,350,100,30,"MEDIUM")
        hardButton = Button ((255,255,255),590,350,100,30,"HARD")
        easyButton.display(screen, textfont, False, (0,0,0))
        mediumButton.display(screen, textfont, False, (0,0,0))
        hardButton.display(screen, textfont, False, (0,0,0))

    #Select category page
    if showSelectCategoryPage == True:
        screen.fill((255,255,255))
        text_on_screen("SELECT Category",300,50)
        musicButton = Button ((255,255,255),30,350,100,30,"MUSIC")
        sportsButton = Button ((255,255,255),230,350,100,30,"SPORTS")
        scienceButton = Button ((255,255,255),430,350,100,30,"SCIENCE")
        animalsButton = Button ((255,255,255),630,350,100,30,"ANIMALS")
        foodButton = Button ((255,255,255),30,450,100,30,"FOOD")
        geographyButton = Button ((255,255,255),230,450,100,30,"GEOGRAPHY")        
        entertainmentButton = Button ((255,255,255),430,450,100,30,"ENTERTAINMENT")
        randomWordsButton = Button ((255,255,255),630,450,100,30,"RANDOM WORDS")
        musicButton.display(screen, textfont, False, (0,0,0))
        sportsButton.display(screen, textfont, False, (0,0,0))
        scienceButton.display(screen, textfont, False, (0,0,0))         
        animalsButton.display(screen, textfont, False, (0,0,0))
        foodButton.display(screen, textfont, False, (0,0,0))
        geographyButton.display(screen, textfont, False, (0,0,0))        
        entertainmentButton.display(screen, textfont, False, (0,0,0))
        randomWordsButton.display(screen, textfont, False, (0,0,0))

    #Menu
    if showMenu == True:
        screen.fill((255,255,255))
        tipsAndTricksButton = Button ((255,255,255),325,550,100,30,"Tips & Tricks")
        leaderBoardButton = Button ((255,255,255),350,450,100,30,"Leaderboard")
        customerFeedbackButton = Button ((255,255,255),300,350,200,30,"Customer-feedback")
        minigameButton = Button ((255,255,255),350,250,100,30,"Minigame")
        lessonsButton = Button ((255,255,255),350,150,100,30,"Lessons")
        typingtestButton = Button ((255,255,255),325,50,100,30,"Typing Test")
        tipsAndTricksButton.display(screen, textfont, False, (0,0,0))
        leaderBoardButton.display(screen, textfont, False, (0,0,0))
        customerFeedbackButton.display(screen, textfont, False, (0,0,0))
        minigameButton.display(screen, textfont, False, (0,0,0))         
        lessonsButton.display(screen, textfont, False, (0,0,0))
        typingtestButton.display(screen, textfont, False, (0,0,0))
        input_text = ""
        section = 0
        sample_text = ("Hello and welcome to the typing test that improves and tests your typing speed")
        points = 0
        
        easyBlock1 = Block (100,100,"hello",0.05,"easy")
        easyBlock2 = Block (200,100,"bow",0.1,"medium")
        easyBlock3 = Block (300,100,"gun",0.125,"easy")
        easyBlock4 = Block (400,100,"tower",0.075,"easy")
        
        mediumBlock1 = Block (100,100,"brow",0.1,"easy")
        mediumBlock2 = Block (200,100,"welcome",0.2,"medium")
        mediumBlock3 = Block (300,100,"abide",0.25,"medium")
        mediumBlock4 = Block (400,100,"yes",0.15,"easy")
        
        hardBlock1 = Block (100,100,"exquisite",0.15,"hard")
        hardBlock2 = Block (200,100,"maybe",0.3,"medium")
        hardBlock3 = Block (300,100,"interfere",0.375,"hard")
        hardBlock4 = Block (400,100,"tower",0.225,"medium")
        
    #Lesson Option screen
    if showLessonOptions == True:
        screen.fill((255,255,255))
        analysisButton = Button ((255,255,255),200,350,100,30,"Analysis")
        trainingButton = Button ((255,255,255),500,350,100,30,"Training")
        lessonOptionBackButton = Button ((255,255,255),100,550,100,30,"BACK")
        analysisButton.display(screen, textfont, False, (0,0,0))
        trainingButton.display(screen, textfont, False, (0,0,0))
        lessonOptionBackButton.display(screen, textfont, False, (0,0,0))
        input_text = ""

    #Lesson training options screen
    if showTrainingOptions == True:
        randomText = random.randint(0,2) #Will be used later to generate a random text
        screen.fill((255,255,255)) #Clears the screen
        topLeftButton = Button ((255,255,255),100,200,100,30,"Top Left")
        bottomLeftButton = Button ((255,255,255),100,500,100,30,"Bottom Left")
        topRightButton = Button ((255,255,255),600,200,100,30,"Top Right")
        bottomRightButton = Button ((255,255,255),600,500,100,30,"Bottom Right")
        middleButton = Button ((255,255,255),375,350,100,30,"Middle")
        trainingOptionBackButton = Button ((255,255,255),100,625,100,30,"BACK")
        topLeftButton.display(screen, textfont, False, (0,0,0))
        bottomLeftButton.display(screen, textfont, False, (0,0,0))
        topRightButton.display(screen, textfont, False, (0,0,0))         
        bottomRightButton.display(screen, textfont, False, (0,0,0))
        middleButton.display(screen, textfont, False, (0,0,0))
        trainingOptionBackButton.display(screen, textfont, False, (0,0,0))

    #Lesson training screen
    if showTraining == True:
        screen.fill((255,255,255)) #Clears the screen
        trainingText = keyboardPosition[randomText] #Randomises the text
        text_on_screen(trainingText,100,100)
        pygame.draw.rect(screen,(0,0,0),input_box,2) #Draws the input box
        text_on_screen(input_text,22,400)
        trainingResetButton = Button ((255,255,255),700,550,100,30,"RESET")
        trainingResetButton.display(screen, textfont, False, (0,0,0))
        trainingBackButton = Button ((255,255,255),100,550,100,30,"BACK")
        trainingBackButton.display(screen, textfont, False, (0,0,0))
        
    #Lesson analysis
    if showAnalysis == True:

        if section == 0: #This is the first text the user sees
            sample_text = "YOU WILL BE TESTED 5 TIMES FOR EACH AREA OF THE KEYBOARD\nPress enter to proceed"
            
        enter = False #Activates the timer
        
    if showAnalysisResults == True:
        
        enter = True    #Stops the timer
        showAnalysis = False #Stops the test from displaying
        
        screen.fill((255,255,255))

        #Header
        text_on_screen("WPM              ACCURACY",250,100)
        
        text_on_screen("Top-left",50,150)
        text_on_screen(str(analysisResultsList[0][1]),250,150)
        text_on_screen(str(analysisResultsList[0][2]),450,150)
        
        text_on_screen("Bottom-left",50,225)
        text_on_screen(str(analysisResultsList[1][1]),250,225)
        text_on_screen(str(analysisResultsList[1][2]),450,225)
        
        text_on_screen("Top-right",50,300)
        text_on_screen(str(analysisResultsList[2][1]),250,300)
        text_on_screen(str(analysisResultsList[2][2]),450,300)
        
        text_on_screen("Bottom-right",50,375)
        text_on_screen(str(analysisResultsList[3][1]),250,375)
        text_on_screen(str(analysisResultsList[3][2]),450,375)
        
        text_on_screen("Middle",50,450)
        text_on_screen(str(analysisResultsList[4][1]),250,450)
        text_on_screen(str(analysisResultsList[4][2]),450,450)

        lowScore = analysisResultsList[0][1] #Initialises so it can be compared
        lowArea = "Top left"
        totalAccuracy = 0
        for i in range (0, 5): #Loops through each element of the list
            
            totalAccuracy = totalAccuracy + analysisResultsList[i][2]
            
            if analysisResultsList[i][1]<lowScore:
                lowScore = analysisResultsList[i][1] #Updates when new low is met
                
                if lowScore != analysisResultsList[0][1]: #If the lowscore is not
                                                          #the top left's it updates
                    lowArea = analysisResultsList[i][0]
        
        weakestAreaMessage = "- Your weakest area is the " + str(lowArea) + " with a score of " + str(lowScore)
        text_on_screen(weakestAreaMessage,50,550)
        averageAccuracy = totalAccuracy/5
        if averageAccuracy >90:
            text_on_screen("- Your accuracy is very high, maybe you can sacrifice some of it for a higher speed.",50,600)
        else:
            text_on_screen("- Your accuracy is not very high, try slowing down your typing.",50,600)
            
        analysisResultsBackButton = Button ((255,255,255),700,50,100,30,"BACK")
        analysisResultsBackButton.display(screen, textfont, False, (0,0,0))
        
    if showLogin == True:
        screen.fill((255,255,255))

        #Used for display
        text_on_screen("Username:",100,100) 
        text_on_screen("Password:",100,200)
        text_on_screen("New username:",80,400)
        text_on_screen("New password:",80,500)

        #Creates the buttons
        usernameButton = Button ((255,255,255),250,100,220,30,usernameText)
        passwordButton = Button ((255,255,255),250,200,220,30,passwordText)
        newUsernameButton = Button ((255,255,255),250,400,220,30,newUsernameText)
        newPasswordButton = Button ((255,255,255),250,500,220,30,newPasswordText)
        confirmButton = Button ((255,255,255),600,150,100,30,"CONFIRM")
        addButton = Button ((255,255,255),600,450,100,30,"ADD")

        #Displays the buttons
        usernameButton.display(screen, textfont, True, (0,0,0))
        passwordButton.display(screen, textfont, True, (0,0,0))
        confirmButton.display(screen, textfont, True, (0,0,0))
        newUsernameButton.display(screen, textfont, True, (0,0,0))
        newPasswordButton.display(screen, textfont, True, (0,0,0))
        addButton.display(screen, textfont, True, (0,0,0))

        #Displays messages based on user input
        if incorrectDetails == True:
            text_on_screen("Incorrect details.",600,250)
            
        if oneAccountMessage == True:
            text_on_screen("You can only add one account.",600,550)
            
        if usernameTaken == True:
            text_on_screen("Username is taken.",250,350)
            
        if addedMessage == True:
            text_on_screen("Added.",600,400)

        if detailsTooShort == True:
            text_on_screen("Username or Password is too short.", 400,600)

    if showCustomerFeedback == True:

        screen.fill((255,255,255))
        text_on_screen("Rate the program out of 10:",250,50)
        text_on_screen("Your review:",50,200)
        text_on_screen(input_text,25,260) #Displays what the user types
        pygame.draw.rect(screen,(0,0,0),customerFeedback_box,2) #Draws the large box

        #Buttons
        oneButton = Button((255,255,255),50,100,50,30,"1")
        twoButton = Button ((255,255,255),125,100,50,30,"2")
        threeButton = Button ((255,255,255),200,100,50,30,"3")
        fourButton = Button((255,255,255),275,100,50,30,"4")
        fiveButton = Button ((255,255,255),350,100,50,30,"5")
        sixButton = Button ((255,255,255),425,100,50,30,"6")
        sevenButton = Button((255,255,255),500,100,50,30,"7")
        eightButton = Button ((255,255,255),575,100,50,30,"8")
        nineButton = Button ((255,255,255),650,100,50,30,"9")
        tenButton = Button ((255,255,255),725,100,50,30,"10")
        customerFeedbackSubmitButton = Button ((255,255,255),350,600,100,30,"SUBMIT")
        customerFeedbackBackButton = Button ((255,255,255),100,600,100,30,"BACK")
        
        oneButton.display(screen, textfont, True, (0,0,0))
        twoButton.display(screen, textfont, True, (0,0,0))
        threeButton.display(screen, textfont, True, (0,0,0))
        fourButton.display(screen, textfont, True, (0,0,0))
        fiveButton.display(screen, textfont, True, (0,0,0))
        sixButton.display(screen, textfont, True, (0,0,0))
        sevenButton.display(screen, textfont, True, (0,0,0))
        eightButton.display(screen, textfont, True, (0,0,0))
        nineButton.display(screen, textfont, True, (0,0,0))
        tenButton.display(screen, textfont, True, (0,0,0))
        customerFeedbackSubmitButton.display(screen, textfont, True, (0,0,0))
        customerFeedbackBackButton.display(screen, textfont, True, (255,255,255))
             
        if showRating == True:
            text_on_screen(("Your rating:"+str(rating)),300,150)
            
        if customerFeedbackAdded == True:
            text_on_screen("Added.",350,650)

        if showBadReviewMessage == True:
            text_on_screen("Invalid Review.",500,650)

    if showLeaderboard == True:
        screen.fill((255,255,255))
        
        typingTestLeaderboardButton = Button ((255,255,255),100,350,200,30,"Typing test rankings")
        minigameLeaderboardButton = Button ((255,255,255),500,350,200,30,"Minigame rankings")
        
        typingTestLeaderboardButton.display(screen, textfont, True, (255,255,255))
        minigameLeaderboardButton.display(screen, textfont, True, (255,255,255))

    if showTypingTestLeaderboard == True:
        
        screen.fill((255,255,255))

        #Displays the row names
        text_on_screen("1",50,150)
        text_on_screen("2",50,250)
        text_on_screen("3",50,350)
        text_on_screen("4",50,450)
        text_on_screen("5",50,550)

        #Selects the data for the highscores in descending order
        
        c.execute("SELECT highScore_ID, wpm, accuracy, category, difficulty FROM HighScore ORDER BY wpm DESC")


        #Stores each row as an element of the ranking list created above
        for x in range(0, len(c.fetchall())):

            if x <5:
            
                c.execute("SELECT highScore_ID, wpm, accuracy, category, difficulty FROM HighScore ORDER BY wpm DESC")
                rankings[x] = c.fetchall()[x]   

        #Retrieves the username for each record and stores it in the rankingUsernames list
        for i in range (0, len(rankings)):
            
            
            c.execute("SELECT username FROM User WHERE user_ID = (?)", (str(rankings[i][0]),))
            
            if str(rankings[i][0]) == 'N/A':
                rankingUsernames[i] = "N/A"
                
            else:
                c.execute("SELECT username FROM User WHERE user_ID = (?)", (str(rankings[i][0]),))
                
                #Would return the value with commas and brackets so I used string handling to remove them
                #e.g. the username g would return as [('g',)]
                removeBracket = str(c.fetchall())[1:]
                removeCommaBracket = removeBracket[0:-2]
                removeBracket2 = removeCommaBracket[1:]
                removeCommaBracket2 = removeBracket2[0:-2]
                removeApostrophe = removeCommaBracket2[1:]
                
                rankingUsernames[i] = removeApostrophe


        #Displays each element of the usernameRankings list
        text_on_screen("USERNAMES",100,100)
        text_on_screen(rankingUsernames[0],100,150)
        text_on_screen(rankingUsernames[1],100,250)
        text_on_screen(rankingUsernames[2],100,350)
        text_on_screen(rankingUsernames[3],100,450)
        text_on_screen(rankingUsernames[4],100,550)

        #Uses double indexing to search through the rankings list
        text_on_screen("WPM",250,100)
        text_on_screen(rankings[0][1], 250,150)
        text_on_screen(rankings[1][1], 250,250)
        text_on_screen(rankings[2][1], 250,350)
        text_on_screen(rankings[3][1], 250,450)
        text_on_screen(rankings[4][1], 250,550)

        text_on_screen("ACCURACY",400,100)
        text_on_screen(rankings[0][2], 400,150)
        text_on_screen(rankings[1][2], 400,250)
        text_on_screen(rankings[2][2], 400,350)
        text_on_screen(rankings[3][2], 400,450)
        text_on_screen(rankings[4][2], 400,550)

        text_on_screen("CATEGORY",550,100)
        text_on_screen(rankings[0][3], 550,150)
        text_on_screen(rankings[1][3], 550,250)
        text_on_screen(rankings[2][3], 550,350)
        text_on_screen(rankings[3][3], 550,450)
        text_on_screen(rankings[4][3], 550,550)        

        text_on_screen("DIFFICULTY",675,100)
        text_on_screen(rankings[0][4], 675,150)
        text_on_screen(rankings[1][4], 675,250)
        text_on_screen(rankings[2][4], 675,350)
        text_on_screen(rankings[3][4], 675,450)
        text_on_screen(rankings[4][4], 675,550)

        #Back button
        typingTestLeaderboardBackButton = Button ((255,255,255),50,650,100,30,"BACK")        
        typingTestLeaderboardBackButton.display(screen, textfont, True, (255,255,255))
        
    if showMinigameDifficulties == True:
        
        screen.fill((255,255,255))
        
        minigameEasyButton = Button((255,255,255),180,300,100,30,"Easy")
        minigameMediumButton = Button ((255,255,255),380,300,100,30,"Medium")
        minigameHardButton = Button ((255,255,255),580,300,100,30,"Hard")
        minigameSurvivalButton = Button ((255,255,255),380,500,100,30,"Survival")
        
        minigameEasyButton.display(screen, textfont, True, (255,255,255))
        minigameMediumButton.display(screen, textfont, True, (255,255,255))
        minigameHardButton.display(screen, textfont, True, (255,255,255))
        minigameSurvivalButton.display(screen, textfont, True, (255,255,255))

        
    if showMinigame == True:
        
        screen.fill((255,255,255)) 

        if bombExploding == True:
            
            displayImage(bombImg,50,50)
            
            if pygame.time.get_ticks()/1000 - bomb_ticks >0.25:
                
                bombExploding = False

                bomb_ticks = 1000000
        
        if minigameStop == True:
            input_text = "Press enter to start"
            text_on_screen(input_text,300,550)
            
            minigameBackButton = Button ((255,255,255),50,650,100,30,"BACK")        
            minigameBackButton.display(screen, textfont, True, (255,255,255))
            
        if minigameStop == False:

            #Ensures the results are hidden
            showMinigameResults = False

            if minigameDifficulty == "easy":
                
                minigameExecution(easyBlock1,easyBlock2,easyBlock3,easyBlock4)
                
            elif minigameDifficulty == "medium":

                minigameExecution(mediumBlock1, mediumBlock2, mediumBlock3, mediumBlock4)

            elif minigameDifficulty == "hard":

                minigameExecution(hardBlock1, hardBlock2, hardBlock3, hardBlock4)

            elif minigameDifficulty == "survival":
                
                minigameExecution(mediumBlock1, mediumBlock2, mediumBlock3, mediumBlock4)

                mediumBlock1.increase_speed(0.00001)
                mediumBlock2.increase_speed(0.00001)
                mediumBlock3.increase_speed(0.00001)
                mediumBlock4.increase_speed(0.00001)
                
            text_on_screen(str(points),400,500)

            #Power ups
            text_on_screen("POWERUPS",675,200)
            
            text_on_screen("Slow:",650,300)
            c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Slow Blocks"])        
            text_on_screen(removeBracketsAndCommas(str(c.fetchall())),725,300)

            text_on_screen("Time-Stop:",650,400)
            c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Time-stop"])        
            text_on_screen(removeBracketsAndCommas(str(c.fetchall())),780,400)
        
            text_on_screen("Bomb:",650,500)
            c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Bomb"])        
            text_on_screen(removeBracketsAndCommas(str(c.fetchall())),725,500)


            

    if showMinigameResults == True:
        
        #Checks if the score is a high score or not
        c.execute("SELECT MAX(minigameHighScore) FROM HighScore WHERE highScore_ID = (?)",(user_id,))
        
        if c.fetchone()[0] == "N/A": #Ensures highScore has a value as if the table is empty the value would be nothing
            minigameHighScore = 0
            
        else:
            c.execute("SELECT MAX(minigameHighScore) FROM HighScore WHERE highScore_ID =(?)",(user_id,))
            minigameHighScore = c.fetchone()[0] #Stores the highscore in the variable
            
        if points > int(minigameHighScore):
            #Replaces the highscore with the current one
            c.execute("UPDATE HighScore SET minigameHighScore = (?) WHERE highScore_ID = (?)",[points,user_id])

            new_db.commit()

        #Displays the highscore and amount of points
        text_on_screen(("High Score: " + str(minigameHighScore)),100,100)
        text_on_screen(("Points: "+str(points)),400,300)

        if rewardMoney == True:
            moneyToDisplay = str(updateMoney(minigameDifficulty, points))
            text_on_screen(moneyToDisplay,100,200)


            
    if showMinigameLeaderboard == True:
        screen.fill((255,255,255))

        text_on_screen("1",50,150)
        text_on_screen("2",50,250)
        text_on_screen("3",50,350)
        text_on_screen("4",50,450)
        text_on_screen("5",50,550)

        #Selects the data for the highscores in descending order
        
        c.execute("SELECT highScore_ID, minigameHighScore FROM HighScore ORDER BY wpm DESC")

        #Stores each row as an element of the ranking list created above
        for x in range(0, len(c.fetchall())):
            
             if x < 5:
            
                c.execute("SELECT highScore_ID, minigameHighScore FROM HighScore ORDER BY minigameHighScore DESC")
                minigameRankings[x] = c.fetchall()[x]

        #Retrieves the username for each record and stores it in the rankingUsernames list
        for i in range (0, len(minigameRankings)):

           
            
            c.execute("SELECT username FROM User WHERE user_ID = (?)", (str(minigameRankings[i][0]),))
            
            if str(minigameRankings[i][0]) == 'N/A':
                minigameUsernames[i] = "N/A"
                
            else:
                c.execute("SELECT username FROM User WHERE user_ID = (?)", (str(minigameRankings[i][0]),))
                
                #Would return the value with commas and brackets so I used string handling to remove them
                #e.g. the username g would return as [('g',)]
                
                removeBracket = str(c.fetchall())[1:]
                removeCommaBracket = removeBracket[0:-2]
                removeBracket2 = removeCommaBracket[1:]
                removeCommaBracket2 = removeBracket2[0:-2]
                removeApostrophe = removeCommaBracket2[1:]
                
                minigameUsernames[i] = removeApostrophe


        text_on_screen("USERNAMES",100,100)
        text_on_screen(minigameUsernames[0],100,150)
        text_on_screen(minigameUsernames[1],100,250)
        text_on_screen(minigameUsernames[2],100,350)
        text_on_screen(minigameUsernames[3],100,450)
        text_on_screen(minigameUsernames[4],100,550)

        text_on_screen("SCORE",400,100)
        text_on_screen(str(minigameRankings[0][1]), 400,150)
        text_on_screen(str(minigameRankings[1][1]), 400,250)
        text_on_screen(str(minigameRankings[2][1]), 400,350)
        text_on_screen(str(minigameRankings[3][1]), 400,450)
        text_on_screen(str(minigameRankings[4][1]), 400,550)

        minigameLeaderboardBackButton = Button ((255,255,255),50,650,100,30,"BACK")        
        minigameLeaderboardBackButton.display(screen, textfont, True, (255,255,255))
        

    if showMinigameShop == True:
        screen.fill((255,255,255))
        
        #Header
        text_on_screen("SHOP",370,50)
        text_on_screen("Here you can buy power-ups to be used during the minigame.",80,100)
        
        #Displays money
        text_on_screen("Money:",80,150)
        c.execute("SELECT money FROM User WHERE User.user_id = (?)",(user_id,))
        text_on_screen(removeBracketsAndCommas(str(c.fetchall())),200,150)
        
        #Slow blocks display
        text_on_screen("Slow blocks:", 100,250)
        c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Slow Blocks"])        
        text_on_screen(removeBracketsAndCommas(str(c.fetchall())),310,225)
        text_on_screen("Cost: 250",500,250)

        #Time-stop display
        text_on_screen("Time-stop:", 100,350)
        c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Time-stop"])        
        text_on_screen(removeBracketsAndCommas(str(c.fetchall())),310,325)
        text_on_screen("Cost: 500",500,350)

        #Bomb display
        text_on_screen("Bomb:", 100,450)
        c.execute("SELECT quantity FROM PowerUps WHERE PowerUps.user_ID = (?) AND PowerUps.name = (?)",[user_id ,"Bomb"])        
        text_on_screen(removeBracketsAndCommas(str(c.fetchall())),310,425)
        text_on_screen("Cost: 1000",500,450)
        
        text_on_screen("Description:",80,550)

        

        #Shop Buttons
        minigameContinueButton = Button((255,255,255),600,650,100,30,"CONTINUE")
        
        buySlowBlocksButton = Button((255,255,255),300,250,50,30,"BUY")
        descSlowBlocksButton = Button ((255,255,255),400,250,50,30,"DESC")

        buyTimeStopButton = Button((255,255,255),300,350,50,30,"BUY")
        descTimeStopButton = Button ((255,255,255),400,350,50,30,"DESC")

        buyBombButton = Button((255,255,255),300,450,50,30,"BUY")
        descBombButton = Button ((255,255,255),400,450,50,30,"DESC")        
               

        minigameContinueButton.display(screen, textfont, True, (0,0,0))
        
        buySlowBlocksButton.display(screen, textfont, True, (0,0,0))
        descSlowBlocksButton.display(screen, textfont, True, (0,0,0))
        buyTimeStopButton.display(screen, textfont, True, (0,0,0))
        descTimeStopButton.display(screen, textfont, True, (0,0,0))
        buyBombButton.display(screen, textfont, True, (0,0,0))
        descBombButton.display(screen, textfont, True, (0,0,0))



        if displayCannotAffordMessage == True:
            text_on_screen("You cannot afford this power up.", 400,175)
        
        if showSlowBlocksDesc == True:
            text_on_screen("When you press 1, the speed of the blocks will be halved for 2 seconds.",80,600)

        if showTimeStopDesc == True:
            text_on_screen("When you press 2, the blocks will stop moving for 2 seconds.",80,600)
            
        if showBombDesc == True:
            text_on_screen("When you press 3, all the blocks will reset to the top of the screen.",80,600)            

    if showTipsAndTricks == True:
        
        screen.fill((255,255,255))
        
        #Header
        text_on_screen("Tips & tricks from me:",250,50)

        #My tips
        text_on_screen("1. Press each key lightly.",50,100)
        text_on_screen("2. Use many fingers, not just your thumb and index fingers.",50,150)
        text_on_screen("3. Don't lift your fingers far from the keyboard much after pressing each key.", 50, 200)
        text_on_screen("4. Practice!", 50, 290)

        #Header 2
        text_on_screen("Links for information:",250,350)
        
        text_on_screen("General tips:",50,400)
        generalTips1Button = Button ((255,255,255),250,400,70,30,"CLICK")
        generalTips2Button = Button ((255,255,255),350,400,70,30,"CLICK")
        generalTips3Button = Button ((255,255,255),450,400,70,30,"CLICK")

        generalTips1Button.display(screen, textfont, True, (0,0,0))
        generalTips2Button.display(screen, textfont, True, (0,0,0))
        generalTips3Button.display(screen, textfont, True, (0,0,0))
        
        text_on_screen("Benefits of learning to type well:",50,500)
        benefits1Button = Button ((255,255,255),500,500,70,30,"CLICK")
        benefits2Button = Button ((255,255,255),600,500,70,30,"CLICK")

        benefits1Button.display(screen, textfont, True, (0,0,0))
        benefits2Button.display(screen, textfont, True, (0,0,0))
        
        text_on_screen("Drawbacks of not typing well:",50,600)
        drawbacksButton = Button ((255,255,255),450,600,70,30,"CLICK")
        drawbacksButton.display(screen, textfont, True, (0,0,0))
        
        tipsAndTricksBackButton = Button ((255,255,255),600,650,50,30,"BACK")
        tipsAndTricksBackButton.display(screen, textfont, True, (0,0,0))



        
new_db.close()
pygame.quit()
