print('WELCOME TO HOOK UP GAME')
print('STORY')
print('IN THIS GAME YOU HAVE TO REACH TO A GIVEN LOCATION BUT REMEMBER THAT IS')
print('NOT SO EASY THERE WILL BE OPSTICAL SPAWNING EVERY SECOND YOU HAVE TO')
print('AVOID THEM AND REACH TO THE RED SPOT IF YOU WANT TO WIN THIS GAME.')
print('IF YOU WIN YOU GET TO HERE HOOK UP SONG AND IF YOU LOOSE YOU GET TO HERE ')
print('dhinchak poojas song')
print('!ALL THE BEST FOR GAME PLAY!')
print('NOTE')
print('GAME WILL NOT WORK WITHOUT ENTERING NAME')
name=input('ENTER YOUR NAME:')

import pygame
import random as R
import time as t
import os
pygame.mixer.init(
        )
pygame.init(
        )
#
#colour code
w=(255,255,255)
r=(255,0,0)
g=(0,255,0)
b=(0,0,255)
y=(255,255,0)
B=(0,0,0)
#
 #screen
screen=pygame.display.set_mode((600,300),pygame.RESIZABLE) #size of screen
pygame.display.set_caption(
        'DODGER GAME '
                           ) #name of game
#bi=pygame.transform.scale(bi,(600,600)).convert_alpha()
#
#
pygame.display.update(
        )
########################################################################################################################################################################
clock=pygame.time.Clock(
        )
font=pygame.font.SysFont(
        None
        ,
        55
                         )
def text(t,color,x,y):
        tex=font.render(t,True,color)
        screen.blit(tex,[x,y])
def welcome():
    WEI=pygame.image.load('WI.jpg')
    WEI=pygame.transform.scale(WEI,(300,200)).convert_alpha()
    # WELCOME BGM
    #bi=pygame.image.load('mj.jpg') # you can add image on wlcome screen 
    
    pygame.mixer.music.load('wbg.mp3')
    pygame.mixer.music.play()
    _exit_=False

    # WRITING TXT ON WLCOME PAGE
    
    while not _exit_:
        screen.fill(
                (233,210,229))
        text('DODGER ',r,300,50)
        text('GAME',r,400,100)
        text('PRESS SPACE TO START',B,100,225)
        screen.blit(WEI,(0,0))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    _exit_=True
        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                       gameloop(
                               )

            if _exit_:
                quit()                
        pygame.display.update()
        
        clock.tick(120)  #fps of game

########################################################################################################################################################################3###
#YOUR GAME CODE / GAME LOOP
def gameloop():
    start_time=t.time()        
    #specific variable
    _exit_=False

    game_over=False

    win=False
#
 #   
#
    px=100
    py=100

    wx=150
    wy=150

    w1x=160
    w1y=160

    if(not os.path.exists('name.txt')):
            with open('name.txt','w')as f:
                    f.write(str(name))
    with open('highscore.txt','r')as f:
         hiscore=f.read()


########################################################################################################################################################################
    # GAME BGM
    pygame.mixer.music.load('gbg.mp3')
    pygame.mixer.music.play( )
    _exit_=False


        #game code
    while not _exit_:
        # IF YOU LOOSE
        if game_over:
            lo=pygame.image.load( "los.jpg")
            lo=pygame.transform.scale(lo,(391,234)).convert_alpha()

            screen.fill(w)
            screen.blit( lo,(100,0))

            text('PRESS SPACE',b,320,230)
            text('FOR MENU',b,400,260)#('TEXT',COLOUR,LOCATION ON X,LOCATION ON Y)
           
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            _exit_=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                               welcome(
                                       )
        # IF YOU WIN
        elif win:
             Wi=pygame.image.load("win.jpg")

             Wi=pygame.transform.scale(Wi,(300,300)).convert_alpha()

             screen.fill(w)
             screen.blit(Wi,(100,0))
             text('PRESS SPACE', b,320,230)
             text('FOR MENU',b,400,260)
         
             for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            _exit_=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                               welcome()
      
        elif _exit_:
                quit()
        else:
        #player control
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    _exit_=True
                

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        px=px+10

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        px=px-10

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        py=py-10

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        py=py+10
        

    ############################################################################################################

            W=pygame.image.load("BG.PNG")
            W=pygame.transform.scale(W,(600,300)).convert_alpha()
            
            screen.fill(g)     #colour of screen
            screen.blit(W,(0,0))
                       
            #screen.blit(bi,(0,0))            #projecting image
                                      #postion , size
            pygame.draw.rect(screen,b,[px, py,10, 10])
                                        
            
            #wall
            
              
            W=pygame.draw.rect(screen,r,[500,200,10,10])
            
            if px==500 and py==200:
                win=True
                pygame.mixer.music.load('hookup.mp3')
                pygame.mixer.music.play()

            for i in range(0,20):#you can increase or decrase opstical by changeing (0,xyz)
#                                                                                      ^
                pygame.draw.rect(screen,B,[R.randint(0,600),R.randint(0,300),20,10])
                if abs(px-R.randint(0,600))<6 and abs(py-R.randint(0,600))<6:
                    px=px-10
                    game_over=True
                    pygame.mixer.music.load('lobg.mp3')
                    pygame.mixer.music.play()
                    
                if abs(px-R.randint(0,600)-10)<6 and abs(
                        py-R.randint(0,300))<6:
                    px=px+10
                    screen.fill(w)
                    game_over=True
                    pygame.mixer.music.load('lobg.mp3')
                    pygame.mixer.music.play() 
        pygame.display.update()
        clock.tick(60)  #fps of game

        end_time=t.time()
        
    pygame.quit
    quit()
if name!='':
        welcome()
'''import mysql.connector as m
mydb=m.connect(
host='localhost',
user='root',
passwd='root',
database='game'
)

l=mydb.cursor(
)

l.execute(

'insert into game_name values(str(name))'

)

print(

'name entered in sql'

)
'''
