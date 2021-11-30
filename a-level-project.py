import pygame
import pyautogui
import time
import random
import sqlite3

'''
I am using a class for interacting with the databse 
as there will be a lot of repeated code all over my program 
so it makes it easier to code and neater
'''

class Database():

    def __init__(self): # creates a connection with the database
        self.db = 'accounts.db'
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()

    def fetch_data(self):
        '''
This procedure gathers and returns 
all of the data from the database
in a 2D array with an array for each
attribute
        '''
        ids = []
        unames = []
        pwords = []
        crlist = []
        rplist = []
        rwlist = []
        rllist = []
        bg_active = []
        bg_owned = []

        sql = '''SELECT * FROM Accounts'''
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for r in rows: 
            ids.append(r[0])
            unames.append(r[1])
            pwords.append(r[2])
            crlist.append(r[3])
            rplist.append(r[4])
            rwlist.append(r[5])
            rllist.append(r[6])
            bg_active.append(r[7])
            bg_owned.append(r[8])

        return [ids,unames,pwords,crlist,rplist,rwlist,rllist, bg_active, bg_owned] # allows for all of the database to be stored in one variable

        '''
            These functions below allow me to interact with the database
            with out having to write-out the sql everytime
        '''

    def add_account(self, data):
        sql = '''INSERT INTO Accounts (Username, Password, Credits, Played, Won, Lost, Background_ACTIVE, Background_OWNED)
                VALUES (?,?,?,?,?,?,?,?);'''
        self.cur.execute(sql, data)
        self.conn.commit()

    def update_values(self, data):
        sql = '''UPDATE Accounts
                SET Credits = ?,
                    Played = ?,
                    Won = ?,
                    Lost = ?
                WHERE accountID = ?;'''
        self.cur.execute(sql, data)
        self.conn.commit() 

    def update_active_bg(self, data):
        sql = '''UPDATE Accounts
                SET Background_ACTIVE = ?
                WHERE accountID = ?;
                '''       
        self.cur.execute(sql, data)
        self.conn.commit()
    
    def update_owned_bg(self,data):
        sql = '''UPDATE Accounts 
                SET Background_OWNED = ?
                WHERE accountID = ?;
                '''
        self.cur.execute(sql, data)
        self.conn.commit()

db = Database() # initializes the database connection

class Account(): # allows an instance of the account to hold all of the attributes in one location
    def __init__(self, id,username, password, credits, rp, rw,rl, active_bg, owned_bg):  
        self.id = id
        self.username = username
        self.password = password
        self.credits = credits
        self.rp = rp
        self.rw = rw
        self.rl = rl
        self.bet = 0
        # These 2 variables allow the shop and game to select the correct images
        self.active_bg = active_bg
        self.owned_bg = owned_bg

def startScreen():
    pygame.init()
    pygame.font.init()

    dX, dY = pyautogui.size()#gets the size for the users display

    win = pygame.display.set_mode((dX,dY),pygame.FULLSCREEN) #creates the window in fullscreen mode

    font = pygame.font.Font('Fonts/OpenSans-Regular.ttf',32)

    bg = pygame.image.load('Images/playersBG.jpeg')
    bg = pygame.transform.scale(bg, (dX, dY))
    
    win.blit(bg, (0,0))
    pygame.display.set_caption('Players')

    pygame.display.update()
    run = True
    while run:
        
        for event in pygame.event.get(): #is triggered when something happens in the game - ie mouse movement
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed() #gets all of the inputs from the keyboard
        if keys[pygame.K_ESCAPE]:
            run = False 

        mx, my = pygame.mouse.get_pos() # returns an array of x and y
        pressed = pygame.mouse.get_pressed() # returns a boolean value for each mouse click


        #button code
        if pressed[0]:
            if 945 < mx < 1870: # checks the x position of the mouse is within the button boundaries
                if 700 < my < 950: # checks the y position of the mouse
                    run = False
                    accountStartUp('create')
                if 1000 < my < 1250:
                    run = False
                    accountStartUp('login')
                if 1310 < my < 1550:
                    run = False
            time.sleep(0.1)
    

 #-----------------------------------------------------------------------------------------------------------------------------------------------------
   

def accountStartUp(screen):
    '''
This procedure runs the create account
and login screen. I have used the 'screen'
variable as this will limit the amount of 
code i need to write.
    '''

    dX, dY = pyautogui.size()#gets the size for the users display

    win = pygame.display.set_mode((dX,dY),pygame.FULLSCREEN) #creates the window in fullscreen mode
    clock = pygame.time.Clock() # initializes the clock, esures the loop runs at a constant/stable rate (60FPS)

    font1 = pygame.font.Font('Fonts/OpenSans-Regular.ttf',32) #loads the font from the folder
    font2 = pygame.font.Font('Fonts/OpenSans-Regular.ttf',32) 
    font3 = pygame.font.Font('Fonts/OpenSans-Regular.ttf',48) 
    
    loggedIn = False
    username = 'Click here to enter your Username' # placeholder text
    password = ''
    passwordDisplay = 'Click here to enter your password' # having 2 variables allows me to display '*' for every letter to keep it secure
    emText = 'Please enter a username and password'

    if screen == 'login':
        bg = pygame.image.load('Images/loginbg.jpg')
    else:
        bg = pygame.image.load('Images/cabg.png')
    bg = pygame.transform.scale(bg, (dX, dY))
    
    win.blit(bg, (0,0))
    pygame.display.set_caption('Players')

# used so the program knows what input box is active

    unClicked = False 
    pwClicked = False
    error = False

    def displayUpdate():
    
        win.blit(bg, (0,0))
        unTextSurface = font1.render(username,True,(0,0,0))
        pwTextSurface = font2.render(passwordDisplay,True,(0,0,0))
        if screen == 'login':
            win.blit(unTextSurface, (400, 750))
            win.blit(pwTextSurface, (400, 1170))
        else: 
            win.blit(unTextSurface, (480,835))
            win.blit(pwTextSurface, (480, 1300))
        if error:
            errorMessage = font3.render(emText,True, (255,0,0))
            win.blit(errorMessage, (600,400))
            pygame.display.update()
        pygame.display.update()

    data = db.fetch_data()
    run = True

    while run:
        clock.tick() # locking the game updates 60 times a second
        mx, my = pygame.mouse.get_pos() # returns an array of x and y

        for event in pygame.event.get(): # loop is activated when an event occurs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    run = False
                else:
                    run = True
                if event.key == pygame.K_RETURN:
                    if screen == 'login':
                        if (username != 'Click here to enter your Username' and len(username) > 0) and (password != 'Click here to enter your password' and len(password) > 0):
                            if username in data[1]:
                                index = data[1].index(username)
                                aID = data[0][1]
                                if password == data[2][index]:
                                    run = False
                                    mainMenu(Account(index, username, password, data[3][index], data[4][index], data[5][index], data[6][index], data[7][index], data[8][index]))
                                    
                            else:
                                username = ''
                                password = ''
                        else:
                            error = True
                    else:
                        if (username != 'Click here to enter your Username' and len(username) > 0) and (password != 'Click here to enter your password' and len(password) > 0):
                            if username in data[1]:
                                error = True # The user cannot create an account with a username that is already in use 
                            else:
                                error = False 
                        else:
                            error = True

                        if not error:
                            run = False
                            db.add_account((username, password, 1000, 0, 0,0 ,'default.jpg', 'default.jpg'))
                            data = db.fetch_data()
                            index = data[1].index(username)
                            mainMenu(Account(index, username, password, data[3][index], data[4][index], data[5][index], data[6][index], data[7][index], data[8][index]))
                            
                      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen == 'login':
                    if 350 < mx < 1430: # checks the x position of the mouse
                        if 660 < my < 890:
                            unClicked = True
                            pwClicked = False
                        elif 1080 < my < 1320:
                            unClicked = False
                            pwClicked = True
                        else: 
                            unClicked = False
                            pwClicked = False
                    else:
                        unClicked = False
                        pwClicked = False
                    
                    if (720 < mx < 1550) and (1550 < my < 1790):
                        if ((username != 'Click here to enter your Username' and len(username) > 0) and 
                        (password != 'Click here to enter your password' and len(password) > 0)):
                            # data is fetched from the database using a 2D
                            if username in data[1]:
                                index = data[1].index(username)
                                aID = data[0][index]
                                if password == data[2][index]:
                                    run = False
                                    mainMenu(Account(index, username, password, data[3][index], data[4][index], data[5][index], data[6][index], data[7][index], data[8][index]))
                                else:
                                    error = True
                            else:
                                error = True
                        else:
                            error = True  
                    
                else:
                    if 400 < mx <1640:
                        if 775 < my < 1020:
                            unClicked = True
                            pwClicked = False
                        elif 1230 < my < 1500:
                            unClicked = False
                            pwClicked = True
                        else: 
                            unClicked = False
                            pwClicked = False
                    else:
                        unClicked = False
                        pwClicked = False
                    
                    if (1000 < mx < 1900) and (1670 < my < 1900):
                        if ((username != 'Click here to enter your Username' and username != '') and 
                        (password != 'Click here to enter your password' and len(password) > 0)):
                            if username in data[1]:
                                error = True
                            else:
                                error = False
                        else:
                            error = True
                        
                        if not error:
                            run = False
                            db.add_account((username, password, 1000, 0, 0,0 ,'default.jpg', 'default.jpg'))
                            data = db.fetch_data()
                            index = data[1].index(username)
                            mainMenu(Account(index, username, password, data[3][index], data[4][index], data[5][index], data[6][index], data[7][index], data[8][index]))

            if unClicked:
                if username == 'Click here to enter your Username':
                    username = '' #removes the placeholder text
                else:
                    font1 = pygame.font.Font('Fonts/OpenSans-Regular.ttf',64) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1] # working backspace
                    else:
                        username += event.unicode # adds the input to the variable
            
            if pwClicked:
                if password == 'Click here to enter your password' or passwordDisplay == 'Click here to enter your password':
                    passwordDisplay = '' # resets the password variable 
                else:
                    font2 = pygame.font.Font('Fonts/OpenSans-Regular.ttf',64) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                        passwordDisplay = passwordDisplay[:-1]
                    else:
                        password += event.unicode
                        passwordDisplay += '*'

        

        displayUpdate() 
    pygame.quit()       
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def mainMenu(account):
    def displayUpdate():
        win.blit(bg, (0,0))
        ttd = f'{account.username} : {account.credits} CR || W/L/Played {account.rw}/{account.rl}/{account.rp}'
        ttd = font.render(ttd, True, (0,0,0))
        win.blit(ttd,(1700,50))
        pygame.display.update()
    
    dX, dY = pyautogui.size()#gets the size for the users display

    win = pygame.display.set_mode((dX,dY),pygame.FULLSCREEN) #creates the window in fullscreen mode
    clock = pygame.time.Clock() # initializes the clock, esures the loop runs at a constant/stable rate (60FPS)

    bg = pygame.image.load('Images/mainmenu.png')
    bg = pygame.transform.scale(bg,(dX,dY))

    font = pygame.font.Font('Fonts/OpenSans-Regular.ttf',50) #loads the font from the folder

    run = True
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 155 < mx < 750:
                    if 700 < my < 905:
                        run = False
                        betting(account)
                    if 1075 < my < 1240:
                        run = False
                        shop(account)
                    if 1460 < my < 1630:
                        run = False
        
        displayUpdate()

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def shop(acc):

    def displayUpdate(defText, fText, sText, gText): # passing in the text variables allow them to be up to date with the database
        defText = font.render(defText, True, (255,255,255))
        fText = font.render(fText, True, (255,255,255))
        sText = font.render(sText,True,(255,255,255))
        gText = font.render(gText,True,(255,255,255))
        mmText = font.render('Main Menu',True,(255,255,255))
        acText = font.render(f'{acc.username} : {acc.credits} CR', True, (255,255,255))

        win.blit(bg, (0,0))
        win.blit(mmText, (2100,100))
        win.blit(acText, (750, 100))

        win.blit(default, (500,450))
        win.blit(defText, (750, 700))

        win.blit(flamingo, (500,1000))
        win.blit(fText, (750, 1250))

        win.blit(silver, (1500,450))
        win.blit(sText, (1750, 700))

        win.blit(gold, (1500, 1000))
        win.blit(gText, (1750, 1250))

        pygame.display.update()
        
    
    dX, dY = pyautogui.size()#gets the size for the users display

    win = pygame.display.set_mode((dX,dY),pygame.FULLSCREEN) #creates the window in fullscreen mode
    clock = pygame.time.Clock() # initializes the clock, esures the loop runs at a constant/stable rate (60FPS)

    bg = pygame.image.load('Images/shopbg.png')
    bg = pygame.transform.scale(bg,(dX,dY))

    default = pygame.image.load('Images/GameBG/Normal/default.jpg')
    default = pygame.transform.scale(default, (750,500))

    font = pygame.font.Font('Fonts/OpenSans-Regular.ttf',70) #loads the font from the folder

    run = True
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        if acc.active_bg == 'default.jpg':
            defText = 'ACTIVE'
        else:
            defText = 'EQUIP'
        
        
            
        '''
            These selection tress decide what image to display in the shop
            They also decide the function of clicking on the image (Buy or equip)
        '''

        if 'flamingo.png' in acc.owned_bg:
            flamingo = pygame.image.load('Images/GameBG/Normal/flamingo.png')
            f_owned = True
            fText = 'EQUIP'
        else:
            flamingo = pygame.image.load('Images/GameBG/Blur/flamingoblur.png')
            f_owned = False
            fText = '2500 CR'
        flamingo = pygame.transform.scale(flamingo,(750,500))
        if 'silver.png' in acc.owned_bg:
            silver = pygame.image.load('Images/GameBG/Normal/silver.png')
            s_owned = True
            sText = 'EQUIP'
        else:
            silver = pygame.image.load('Images/GameBG/Blur/silverblur.png')
            s_owned = False
            sText = '6000 CR'
        silver = pygame.transform.scale(silver, (750,500))
        if 'gold.png' in acc.owned_bg:
            gold = pygame.image.load('Images/GameBG/Normal/gold.png')
            g_owned = True
            gText = 'EQUIP'
        else:
            gold = pygame.image.load('Images/GameBG/Blur/goldblur.png')
            g_owned = False
            gText = '10,000 CR'
        gold = pygame.transform.scale(gold, (750,500))

        if acc.active_bg == 'flamingo.png':
            fText = 'ACTIVE'
        if acc.active_bg == 'silver.png':
            sText = 'ACTIVE'
        if acc.active_bg == 'gold.png':
            gText = 'ACTIVE'

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN: # This series of selection trees creates the buttons
                if 500 < mx < 1250:
                    if 450 < my < 950:
                        acc.active_bg = 'default.jpg'
                        defText = 'ACTIVE'
                        db.update_active_bg(('default.jpg', acc.id))
                    if 1000 < my < 1500:
                        if f_owned:
                            acc.active_bg = 'flamingo.png'
                            fText = 'ACTIVE'
                            db.update_active_bg(('flamingo.png', acc.id))
                        else:
                            if acc.credits > 2500:
                                acc.credits -= 2500
                                db.update_values((acc.credits, acc.rp, acc.rw, acc.rl, acc.id))
                                acc.owned_bg += ',flamingo.png'
                                db.update_owned_bg((acc.owned_bg, acc.id))
                                f_owned = True
                if 1500 < mx < 2250:
                    if 450 < my < 950:
                        if s_owned:
                            acc.active_bg = 'silver.png'
                            sText = 'ACTIVE'
                            db.update_active_bg(('silver.png', acc.id))
                        else:
                            if acc.credits > 6000:
                                acc.credits -= 6000
                                db.update_values((acc.credits, acc.rp, acc.rw, acc.rl, acc.id))
                                acc.owned_bg += ',silver.png'
                                db.update_owned_bg((acc.owned_bg, acc.id))
                                s_owned = True
                    if 1000 < my < 1500:
                        if g_owned:
                            acc.active_bg = 'gold.png'
                            gText = 'ACTIVE'
                            db.update_active_bg((acc.active_bg, acc.id))
                        else:
                            if acc.credits > 10000:
                                acc.credits -= 10000
                                db.update_values((acc.credits, acc.rp, acc.rw, acc.rl, acc.id))
                                acc.owned_bg += ',gold.png'
                                db.update_owned_bg((acc.owned_bg, acc.id))
                                g_owned = True    

                    if ( 2000 < mx < 2500 ) and ( 100 < my < 200): # button to go back to the main menu
                        run = False
                        mainMenu(acc)                             

        displayUpdate(defText, fText, sText, gText)

#-----------------------------------------------------------------------------------------------------------------------------------------------

def betting(acc):
    
    def displayUpdate(): #this fucntion is mainly to display to the user how mucht they are betting and their balance
        usernametxt = 'Player: '+str(acc.username)
        crtxt = 'Credits: '+str(acc.credits)+'cr'
        bettxt = 'Bet: '+str(acc.bet)+'cr'
        usernametxt = font.render(usernametxt,True,(0,0,0))
        crtxt = font.render(crtxt,True,(0,0,0))
        bettxt = font.render(bettxt,True,(0,0,0))
        win.blit(betbg, (0,0))
        win.blit(usernametxt, (250,250))
        win.blit(crtxt, (250,320))
        win.blit(bettxt, (250,390))
        pygame.display.update()

    dX, dY = pyautogui.size()#gets the size for the users display

    win = pygame.display.set_mode((dX,dY),pygame.FULLSCREEN) #creates the window in fullscreen mode
    clock = pygame.time.Clock() # initializes the clock, esures the loop runs at a constant/stable rate (60FPS)

    betbg = pygame.image.load('Images/betting.jpg')
    betbg = pygame.transform.scale(betbg,(dX,dY))

    font = pygame.font.Font('Fonts/OpenSans-Regular.ttf',70) #loads the font from the folder

    acc.bet = 0
    cr = acc.credits
    run = True
    while run:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.K_ESCAPE:
                    run = False
                else:
                    run = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1150 < my < 1460: # this loops checks the x and y postion of the mouse when clicked
                    if 670 < mx < 930:
                        if cr > (acc.bet + 5): # checks if the user has enough credits to bet
                            acc.bet += 5
                            acc.credits -= 5
                    if 1030 < mx < 1300:
                        if cr > (acc.bet + 10):
                            acc.bet += 10
                            acc.credits -= 10
                    if 1370 < mx < 1660:
                        if cr > (acc.bet + 25):
                            acc.bet += 25
                            acc.credits -= 25
                    if 1700 < mx < 1990:
                        if cr > (acc.bet + 50):
                            acc.bet += 50
                            acc.credits -= 50
                    if 2030 < mx < 2200:
                        if cr > (acc.bet + 100):
                            acc.bet += 100
                            acc.credits -= 100

                if 1550 < my < 1870:
                    if 1160 < mx < 1490:
                        if cr > (acc.bet + 250):
                            acc.bet += 250
                            acc.credits -= 250
                    if 1550 < mx < 1860:
                        if cr > (acc.bet + 500):
                            acc.bet += 500
                            acc.credits -= 500
                
                if (520 < my < 915):
                    if (1960 < mx < 2370):
                        game(acc)
                        run = False

        displayUpdate()
            

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def game(player):
    def displayUpdate(stand):
        win.blit(gamebg, (0,0))
        ttd = font.render(str(player.username), True, (255,255,255))
        win.blit(ttd, (1400,1870))
        px = 1050
        x = 1050
        for p in Ppaths:  # goes through the list of paths and loads those files
            pc = pygame.image.load(p)
            pc = pygame.transform.scale(pc, (400,580))
            win.blit(pc, (px,1200))
            px += 75 # ensures the user can see all their cards and they arent overlapped

        if stand: # this makes it so the user cannot see the dealers cards if they are still making their hand
            for p in dPaths:
                c = pygame.image.load(p)
                c = pygame.transform.scale(c, (400,580))
                win.blit(c, (x,375))
                x += 100
        else:
            for p in dPaths:
                if dPaths.index(p) == 0:
                    img = pygame.image.load(p)
                else:
                    img = pygame.image.load('Cards/blue_back.jpg')
                img = pygame.transform.scale(img, (400,580))
                win.blit(img, (x,375))
                x += 100

        pygame.display.update()

    def bustCheck():
        if sum(pHand) > 21:
            pBust = True
        else:
            pBust = False
        if sum(dHand) > 21:
            dBust = True
        else:
            dBust = False
        
        return dBust, pBust

    
    def hit():
        value = deck.pop() 
        symbol = suit.pop()

        if value > 10: # the picture cards are 11,12 and 13 which arent values you can get in blackjack
            pHand.append(10)

        elif value == 1:
            if sum(pHand) < 11:
                pHand.append(11)
            else:
                pHand.append(1)
        else:
            pHand.append(value)
        
        if value == 11:
            value = 'J'
        if value == 12:
            value = 'Q'
        if value == 13:
            value = 'K'
        if value == 1:
            value = 'A'

        card =  str(value) + symbol
        pCards.append(card)
        path = f'Cards/{card}.png'
        Ppaths.append(path)

        dBust, pBust = bustCheck()

    def blackjackChecker():
        pbj = False
        dbj = False

        if len(pCards) > 2: # blackjack is not possible with more than 2 cards
            return 'none'
        else:
            if  (('A' in pCards[0]) or ('J' in pCards[0]) or ('Q' in pCards[0]) or ('K' in pCards[0]) 
            or ('10' in pCards[0])) and (('A' in pCards[1]) or ('J' in pCards[1]) or ('Q' in pCards[1]) 
            or ('K' in pCards[1]) or ('10' in pCards[1])):
                pbj = True
            if  (('A' in dCards[0]) or ('J' in dCards[0]) or ('Q' in dCards[0]) or ('K' in dCards[0])
            or ('10' in dCards[0])) and (('A' in dCards[1]) or ('J' in dCards[1]) or ('Q' in dCards[1]) 
            or ('K' in dCards[1]) or ('10' in dCards[1])):
                dbj = True
        
            if pbj and dbj: # a draw with no bust means the dealer wins
                return 'dealer'

            elif pbj and dbj == False:
                return 'player'

            elif pbj == False and dbj:
                return 'dealer'

            else:
                return None


    dX, dY = pyautogui.size()#gets the size for the users display

    win = pygame.display.set_mode((dX,dY),pygame.FULLSCREEN) #creates the window in fullscreen mode
    clock = pygame.time.Clock() # initializes the clock, esures the loop runs at a constant/stable rate (60FPS)
    gamebg = pygame.image.load(f'Images/GameBG/Normal/{player.active_bg}')
    gamebg = pygame.transform.scale(gamebg,(dX,dY))

    font = pygame.font.Font('Fonts/OpenSans-Regular.ttf',90) #loads the font from the folder  

    mx, my = pygame.mouse.get_pos()

    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4 
    suit = ['S','C','H','D']*52

    pHand = [] # use of lists for the hand as it easy to sum for totals
    dHand = []

    Ppaths = [] # a list for the paths to the images of the cards
    dPaths = []

    pCards = [] # a general list for the value and suit to check for blackjack
    dCards = []

    # --- start of the game ---    
    for i in range(2): # deals the first two cards to the dealer and player
        random.shuffle(deck)
        random.shuffle(suit)

        value = deck.pop()
        symbol = suit.pop()

        if value > 10:
            pHand.append(10)
        elif value == 1:
            pHand.append(11)
        else:
            pHand.append(value)

        if value == 11: 
            value = 'J'
        elif value == 12:
            value = 'Q'
        elif value == 13:
            value = 'K' 
        elif value == 1:
            value = 'A'

        card = str(value) + symbol
        pCards.append(card)
        path = 'Cards/'+card+'.png'
        Ppaths.append(path)

    for i in range(2):
        value = deck.pop()
        symbol = suit.pop()

        if value > 10:
            dHand.append(10)
        else:
            dHand.append(value)

        if value == 11: 
            value = 'J'
        elif value == 12:
            value = 'Q'
        elif value == 13:
            value = 'K' 
        elif value == 1:
            value = 'A'

        card = str(value) + symbol
        dCards.append(card)

        path = 'Cards/'+card+'.png'
        dPaths.append(path)


    blackjack = blackjackChecker()

    if blackjack == None or blackjack == 'dealer':
        stand = False
    elif blackjack == 'player':
        stand = True

    pBust = False
    dBust = False

    displayUpdate(stand)

    

    run = True
    while run: # main game loop
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE: 
                    run = False
                if event.key == pygame.K_h:
                    hit()
                    displayUpdate(stand)
                if event.key == pygame.K_s:
                    stand = True

        if pBust:
            stand = True

        if stand:
            displayUpdate(stand) # displays the dealers cards
            blackjack = blackjackChecker() # checks for blackjacks
            if blackjack == 'none':
            #-------------------------------- Dealers algorithm
                while sum(dHand) < 17: # loop which acts as the dealer's algorithm
                    value = deck.pop()
                    symbol = suit.pop()

                    if value > 10:
                        dHand.append(10)
                    else:
                        dHand.append(value)

                    if value == 11: 
                        value = 'J'
                    elif value == 12:
                        value = 'Q'
                    elif value == 13:
                        value = 'K' 
                    elif value == 1:
                        value = 'A'
                    
                    card = str(value) + symbol
                    dCards.append(card)

                    path = 'Cards/'+card+'.png'
                    dPaths.append(path)

                    displayUpdate(stand)

            #---------------------------- end of the dealer's algorithm
            # This following code checks for the winner of the round
            dBust, pBust = bustCheck()
            player.rp += 1
            if blackjack == 'none':
                if pBust and dBust:
                    run = False
                    player.rl += 1
                    time.sleep(5) # this is used to allow the player to review the round and see what has happened
                    winningScreen('Dealer',player)    

                elif pBust and  dBust == False:
                    run = False
                    player.rl += 1
                    time.sleep(5)
                    winningScreen('Dealer',player)

                elif pBust == False and dBust:
                    run = False
                    player.rw += 1
                    time.sleep(5)
                    player.credits += player.bet * 2
                    winningScreen(player.username,player)

                elif pBust == False and dBust == False:
                    dScore = sum(dHand)
                    pScore = sum(pHand)
                    if dScore >= pScore:
                        run = False
                        player.rl += 1
                        time.sleep(5)
                        winningScreen('Dealer',player)
                    else:
                        run = False
                        player.rw += 1
                        time.sleep(5)
                        player.credits += player.bet * 2 # rewards the player with their bet
                        winningScreen(player.username,player)
            else:
                run = False
                if blackjack == 'player':
                    player.rw += 1
                    time.sleep(5)
                    player.credits += player.bet * 5 # when the player gets lucky they get a x5 bonus
                    winningScreen(player.username,player)
                else:
                    player.rl += 1
                    time.sleep(5)
                    winningScreen('Dealer',player)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def winningScreen(winner, acc):
    db.update_values((acc.credits, acc.rp, acc.rw, acc.rl, acc.id))
    dX, dY = pyautogui.size()#gets the size for the users display

    win = pygame.display.set_mode((dX,dY),pygame.FULLSCREEN) #creates the window in fullscreen mode
    clock = pygame.time.Clock() # initializes the clock, esures the loop runs at a constant/stable rate (60FPS)

    bg = pygame.image.load('Images/after_round.png')
    bg = pygame.transform.scale(bg,(dX,dY))

    font = pygame.font.Font('Fonts/PTMono-Regular.ttf',80) #loads the font from the folder so pygame has a font to write form

    mx, my = pygame.mouse.get_pos()

    def displayUpdate():
        if winner == 'd':
            ttd = 'ITS A DRAW!'
        else:
            ttd = str(f'{winner} WINS!') # uses the winner variable passed in by the game function
        wintxt = font.render(ttd, True, (255,255,255))
        pcrtxt = font.render((f'You have {acc.credits} after this round'), True, (255,255,255))
        win.blit(bg, (0,0))
        win.blit(wintxt, (110,720))
        win.blit(pcrtxt, (110,1200))
        pygame.display.update()

    run = True
    while run:
        clock.tick(60)
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    run = False
            if events.type == pygame.MOUSEBUTTONUP:
                if (1530 < mx < 2770) and (450 < my < 620):
                    run = False
                    betting(acc)
                elif (1360 < mx < 2930) and (900 < my < 1130):
                    run = False
                    mainMenu(acc)
                elif (1775 < mx < 2510) and (1365 < my < 1660):
                    quit()

        mx, my = pygame.mouse.get_pos()
        displayUpdate()

            

startScreen() # starts the program
'''
All of the code for the game will be called concurrenlty 
starting with the function above
'''
pygame.quit()