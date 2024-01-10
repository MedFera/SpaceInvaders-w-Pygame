import sys
import pygame
import random
import math

#Initialize pygame
pygame.init()

#Create the screen (width, height)
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invaders")

#Need to call image module from pygame
icon = pygame.image.load("icon.png")
#Adds icon to the game window
pygame.display.set_icon(icon)

#Add background image
background = pygame.image.load("background.png")


#Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(random.randint(-2, -1) / 10)
    enemyY_change.append(20)


#Bullet 
bulletImg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = 480
bulletY_change = 2
bullet_state = "ready" #Ready - bullet not on screen/ Fire - bullet moving on screen

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 20
textY = 20

def player(x,y):
    #blit means to draw image on screen
    screen.blit(playerImg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i] , (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16 ,y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2)) #distance formula
    if distance < 27:
        return True
    else:
        return False
    
def show_score(x,y):
    score = font.render("Score: " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    
def add_more_enemy():
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(random.randint(-2, -1) / 10)
    enemyY_change.append(20)

game_over_state = False

def game_over(x,y):
    screen.fill((5,5,15))
    game_over_text = font.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over_text,(x,y))
    
    
#An Event is anything happening inside game window
#This is the game loop that handles events
running = True
while running == True:
    #This gets all the events happening in pygame
    for event in pygame.event.get():
        #If the QUIT event happens then the loop finishes
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0 
                   
        #Checks to see if key is pressed down
        if event.type == pygame.KEYDOWN:
            #Now we will assign actions to which button is pressed
            if event.key == pygame.K_a:
                playerX_change -= 3

            if event.key == pygame.K_d:
                playerX_change += 3
                
            #This is Bullet being fired
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, playerY)
         
        
           
                    
            
        
            
            
                
    #color in the screen background        
    screen.fill((5,5,15))        
    
    #Background image
    screen.blit(background,(0,0))
    
    #Player Movement (Boundaries Check)
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    #Enemy Movement (Boundaries Check)
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = random.randint(0,4) / 10 + .1
            enemyY[i] += enemyY_change[i]
            
        elif enemyX[i] >= 736:
            enemyX[i] = 736
            enemyX_change[i] = random.randint(-4,0) / 10 -.1
            enemyY[i] += enemyY_change[i]
            
        #Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)        
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1            
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)  
        
        collision_player = isCollision(enemyX[i],enemyY[i],playerX,playerY)        
        if collision_player:
            game_over_state = True
              
        enemy(enemyX[i] , enemyY[i], i)
         
    #Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY == 0:
            bullet_state = "ready"
            bulletY = playerY
            
            
    #Difficulty adjustment
    if score_value < 20:
        num_of_enemies = 7
        add_more_enemy()
        for i in range(num_of_enemies):
            enemyY_change[i] = 25
    elif score_value < 60:
        num_of_enemies = 8
        add_more_enemy()      
    elif score_value < 80:
        num_of_enemies = 9
        add_more_enemy()
        for i in range(num_of_enemies):
            enemyY_change[i] = 30
    elif score_value < 100:
        num_of_enemies = 10
        add_more_enemy()
    elif score_value < 120:
        num_of_enemies = 11
        add_more_enemy()
        for i in range(num_of_enemies):
            enemyY_change[i] = 35
    elif score_value < 140:
        num_of_enemies = 12
        add_more_enemy()
    elif score_value < 160:
        num_of_enemies = 13
        add_more_enemy()
        for i in range(num_of_enemies):
            enemyY_change[i] = 40
    elif score_value < 180:
        num_of_enemies = 14
        add_more_enemy()
        for i in range(num_of_enemies):
            enemyY_change[i] = 45
    elif score_value < 200:
        num_of_enemies = 15
        add_more_enemy()
        for i in range(num_of_enemies):
            enemyY_change[i] = 50
    
          
    player(playerX,playerY)
    show_score(textX,textY)
    
    
    if game_over_state == True:
        game_over(305,280) 
    #updates the display of the window (screen variable)      
    pygame.display.update()

#Ensure game closes just in case            
pygame.quit()
sys.exit()