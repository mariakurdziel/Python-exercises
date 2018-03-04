# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pygame, sys, os,time,random
from pygame.locals import*

pygame.init()
pygame.mixer.init()
length=600
width=800
clock=pygame.time.Clock()
smallfont=pygame.font.SysFont(None,25)
mediumfont=pygame.font.SysFont(None,40)
largefont=pygame.font.SysFont(None,100)
extralargefont=pygame.font.SysFont(None,140)

screen=pygame.display.set_mode((width,length))
pygame.display.set_caption('Snake')
green=(0,153,0)
black=(0,0,0)
darkblue=(0,0,128)
red=(255,0,0)
white=(255,250,250)
palegreen=(152,251,152)
paleyel=(241,232,150)
blue=(30,144,255)
lista=[]
nameList=[]



pygame.display.update()
graphic=pygame.image.load('lebekwunsza.png')
apple=pygame.image.load('perfectapple.png')
pineapple=pygame.image.load('ananasik.png')
bomb=pygame.image.load('Bomb.png')
choco=pygame.image.load('choco.png')
strawberry=pygame.image.load('straw.png')
cupcake=pygame.image.load('cup.png')
snakeintro=pygame.image.load('snakeok.png')
arrows=pygame.image.load('strzalki.png')
wallintro=pygame.image.load('wall.png')
snake2=pygame.image.load('wunsz2.png')
loli=pygame.image.load('lolipop.png')
coke=pygame.image.load('coke.png')
donut=pygame.image.load('donut.png')
pizza=pygame.image.load('pizz.png')
boom=pygame.image.load('bumok.png')
file='Cinema Sins Background Song (Clowning Around) - Background Music (HD).mp3'
hamb=pygame.image.load('hamb.png')
bomb=pygame.image.load('Bomb.png')
winner1=pygame.image.load('medal.png')
pygame.mixer.music.load(file)
#pygame.mixer.music.load('Fail.mp3')

def quick_texts(message, colour,x,y):
    text=smallfont.render(message,True,colour)
    screen.blit(text,[x,y])
    
def quick_textm(message, colour,x,y):
    text=mediumfont.render(message,True,colour)
    screen.blit(text,[x,y])
    
def text(message, colour,size):
    if size=="small":
        textSurf=smallfont.render(message,True,colour)
    elif size=="medium":
        textSurf=mediumfont.render(message,True,colour)
    elif size=="large":
        textSurf=largefont.render(message,True,colour)
    else:
        textSurf=extralargefont.render(message,True,colour)
    return textSurf, textSurf.get_rect()
    
def message(message, colour,y,size):
    textSurf,textRect=text(message,colour,size)
    textRect.center=(width/2),(length/2 + y)
    screen.blit(textSurf,textRect)
    

def draw_snake(snakelist,size,colour):
    for x in snakelist:
        pygame.draw.rect(screen,colour,[x[0],x[1],10,10])
        
def object(objectx,objecty,objectsize,scoreplus,score):
    colour=palegreen
    if scoreplus=="BOMB":
        quick_texts("-"+str(int(score/2)),black,width/2,length/2)
    else:
        quick_texts("+"+str(scoreplus),black,width/2,length/2)
    pygame.draw.rect(screen,colour,[objectx,objecty,objectsize,objectsize])
    pygame.display.update()
    
    
#def bombs(bombx,bomby,bombsize,score):
def gameinfo():
    info=True
    while info==True:
        screen.fill(palegreen)
        pygame.init()
        for event in  pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_intro()
                        info=False
        message("How to play?",darkblue,-200,"large") 
        screen.blit(arrows,(width/2-300,length/2-150))
        quick_texts("Use UP,DOWN,LEFT and RIGHT arrow to navigate",black,width/2-80,length/2-110)
        quick_texts("your snake. If you play multiplayer, use W (up),",black,width/2-70,length/2-90)
        quick_texts("S (down), A (left) and  D (right) to move blue snake",black,width/2-80,length/2-70)
        screen.blit(choco,(width/2-340,length/2-20))
        screen.blit(apple,(width/2-260,length/2-20))
        screen.blit(cupcake,(width/2-210,length/2-30))
        quick_texts("Eat apples and other stuff to get points and",black,width/2-80,length/2-20)
        quick_texts("get to the next levels. The more you eat,",black,width/2-60,length/2)
        quick_texts("the longer you are",black,width/2,length/2+20)
        screen.blit(bomb,(width/2-270,length/2+50))
        quick_texts("If you eat bomb, you lose half of your points",black,width/2-80,length/2+80)
        screen.blit(wallintro,(width/2-280,length/2+130))
        quick_texts("If you run into wall or yourself, you lose",black,width/2-80,length/2+150)
        quick_textm("Press Q to quit",darkblue,width/2-110,length/2+230)
        pygame.display.update()
        clock.tick(3)
        
def game_intro():
    intro=True
    while intro==True:
        screen.fill(palegreen)
        for event in  pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        intro=False
                        return False
                    if event.key==pygame.K_i:
                        gameinfo()
                    if event.key==pygame.K_m:
                        return True
                        GameOn()
                        
        message("SNAKE",darkblue,-200,"extralarge")
        quick_textm("I",darkblue,width/2-110,length/2-100)
        quick_textm("- How to play",black,width/2-80,length/2-100)
        quick_textm("R",darkblue,width/2-110,length/2-40)
        quick_textm("- One Player",black,width/2-80,length/2-40)
        quick_textm("M",darkblue,width/2-110,length/2+20)
        quick_textm("- Multiplayer",black,width/2-80,length/2+20)
        screen.blit(snakeintro,(width/2-90,length/2+100))
        
        pygame.display.update()
        clock.tick(3)
        
def gameover2 (gameEnd, GameOver, score,score2,winner):

    if winner=="BLUE SNAKE":
        col=blue
    else:
        col=green
    while GameOver==True:
        screen.fill(palegreen)
        message("GAME OVER",darkblue,-150,"large")
        quick_textm("WINNER:",black,width/2-170,length/2-60)
        quick_textm(str(winner),col,width/2-30,length/2-60)
        quick_textm("SCORE 1:",green,width/2-130,length/2-10)
        quick_textm(str(score),black,width/2+90,length/2-10)
        quick_textm("SCORE 2:",blue,width/2-130,length/2+40)
        quick_textm(str(score2),black,width/2+90,length/2+40)
        quick_textm("END GAME",black,width/2-130,length/2+90)
        quick_textm("Q",red,width/2+95,length/2+90)
        quick_textm("NEW GAME",black,width/2-130,length/2+140)
        quick_textm("R",red,width/2+95,length/2+140)
        
        pygame.display.update()
        for event in  pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    gameEnd=True
                    gameOver=False
                    return gameEnd
                elif event.key==pygame.K_r:
                    GameOn()
                    return gameEnd
        pygame.display.update()
        time.sleep(0.2)

def gameover1(gameEnd,GameOver,score):
    

    while GameOver==True:
        screen.fill(palegreen)
        message("GAME OVER",darkblue,-150,"large")
        quick_textm("YOUR SCORE:",black,width/2-130,length/2-60)
        quick_textm(str(score),red,width/2+90,length/2-60)
        quick_textm("END GAME",black,width/2-130,length/2-10)
        quick_textm("Q",red,width/2+95,length/2-10)
        quick_textm("NEW GAME",black,width/2-130,length/2+40)
        quick_textm("R",red,width/2+95,length/2+40)

        pygame.display.update()
        for event in  pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    gameEnd=True
                    gameOver=False
                    return gameEnd
                elif event.key==pygame.K_r:
                    GameOn()
                    return gameEnd

        pygame.display.update()
        time.sleep(0.2)
    
def GameOn(): 
    gameEnd=False
    gameOver=False
    multiplayer=False
    length=600
    width=800
    black=(0,0,0)
    green=(0,153,0)
    red=(255,0,0)
    white=(255,250,250)
    point_x=100
    point_y=100
    point_2x=700
    point_2y=100
    headx=0
    heady=0
    lengths=1
    lengths2=1
    applesize=30
    colour=red
    x_change=0
    y_change=0
    x2_change=0
    y2_change=0
    size=10
    score=0
    score2=0
    level=1
    pnpsize=90
    strawsize=40
    cupsize=40
    lolisize=60
    chocosize=60
    hambsize=50
    cokesize=70
    donsize=50
    pizzasize=50
    bombsize=65
    wallsize=90
    licz=0
    speed=20
    applex=round(random.randrange(0+applesize,width-applesize)/10.0)*10.0
    appley=round(random.randrange(0+applesize,length-applesize)/10.0)*10.0
    pnpx=round(random.randrange(0+pnpsize,width-pnpsize)/10.0)*10.0
    pnpy=round(random.randrange(0+pnpsize,length-pnpsize)/10.0)*10.0
    strawx=round(random.randrange(0+strawsize,width-strawsize)/10.0)*10.0
    strawy=round(random.randrange(0+strawsize,length-strawsize)/10.0)*10.0
    cupx=round(random.randrange(0+cupsize,width-cupsize)/10.0)*10.0
    cupy=round(random.randrange(0+cupsize,length-cupsize)/10.0)*10.0
    lolix=round(random.randrange(0+lolisize,width-lolisize)/10.0)*10.0
    loliy=round(random.randrange(0+lolisize,length-lolisize)/10.0)*10.0
    chocx=round(random.randrange(0+chocosize,width-chocosize)/10.0)*10.0
    chocy=round(random.randrange(0+chocosize,length-chocosize)/10.0)*10.0
    hambx=round(random.randrange(0+hambsize,width-hambsize)/10.0)*10.0
    hamby=round(random.randrange(0+hambsize,length-hambsize)/10.0)*10.0
    cokex=round(random.randrange(0+cokesize,width-cokesize)/10.0)*10.0
    cokey=round(random.randrange(0+cokesize,length-cokesize)/10.0)*10.0
    pizzx=round(random.randrange(0+pizzasize,width-pizzasize)/10.0)*10.0
    pizzy=round(random.randrange(0+pizzasize,length-pizzasize)/10.0)*10.0
    donx=round(random.randrange(0+donsize,width-pizzasize)/10.0)*10.0
    dony=round(random.randrange(0+donsize,length-donsize)/10.0)*10.0
    bombx=round(random.randrange(0+bombsize,width-bombsize)/10.0)*10.0
    bomby=round(random.randrange(0+bombsize,length-bombsize)/10.0)*10.0 
    bomb2x=round(random.randrange(0+bombsize,width-bombsize)/10.0)*10.0
    bomb2y=round(random.randrange(0+bombsize,width-bombsize)/10.0)*10.0 

    pnpsize=40
    scoreobj=10
    scoreobjplus=50
    snakeList=[]
    snake2List=[]
    winner=""
    multiplayer=game_intro()
    pygame.mixer.music.play()
    
    while not gameEnd:
        
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                gameEnd=True
                        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-10
                    y_change=0
                if event.key==pygame.K_RIGHT:
                    x_change=10
                    y_change=0
                if event.key==pygame.K_UP:
                    x_change=0
                    y_change=-10
                if event.key==pygame.K_DOWN:
                    x_change=0
                    y_change=10
                if event.key==pygame.K_a:
                    x2_change=-10
                    y2_change=0
                if event.key==pygame.K_d:
                    x2_change=10
                    y2_change=0
                if event.key==pygame.K_w:
                    x2_change=0
                    y2_change=-10
                if event.key==pygame.K_s:
                    x2_change=0
                    y2_change=10
                    
            
        if point_x==width:
            point_x=0
        elif point_x==0:
            point_x=width
        elif point_y==length:
            point_y=0
        elif point_y==0:
            point_y=length

                
        if level==1:        
            if point_x>=applex-applesize and point_x<=applex+applesize and point_y>=appley-applesize and point_y<=appley+applesize:
                score=score+10
                applex=round(random.randrange(applesize+10,width-applesize-10)/10.0)*10.0
                appley=round(random.randrange(applesize+10,length-applesize-10)/10.0)*10.0
                lengths=lengths+1
                pygame.display.update()
                
                
            if multiplayer==False and score%3==0 and score>0:
                screen.blit(pineapple,(pnpx,pnpy))
                pygame.display.update()
                if point_x>=pnpx-pnpsize and point_x<=pnpx+pnpsize and point_y>=pnpy-pnpsize and point_y<=pnpy+pnpsize:
                    score=score+scoreobjplus
                    object(pnpx,pnpy,pnpsize,scoreobjplus,score)                
                    pnpx=round(random.randrange(pnpsize+10,width-pnpsize-10)/10.0)*10.0
                    pnpy=round(random.randrange(pnpsize+10,length-pnpsize-10)/10.0)*10.0
                    lengths=lengths+1
                    pygame.display.update()
        
                
        elif level==2:
            if point_x>=strawx-strawsize and point_x<=strawx+strawsize and point_y>=strawy-strawsize and point_y<=strawy+strawsize:
                score=score+10
                licz=licz+1
                strawx=round(random.randrange(strawsize+10,width-strawsize-10)/10.0)*10.0
                strawy=round(random.randrange(strawsize+10,length-strawsize-10)/10.0)*10.0
                lengths=lengths+1
                pygame.display.update()
                
                
            if multiplayer==False and score%3==0 and score>0:
                screen.blit(cupcake,(cupx,cupy))
                pygame.display.update()
                if point_x>=cupx-cupsize and point_x<=cupx+cupsize and point_y>=cupy-cupsize and point_y<=cupy+cupsize:
                    scoreobjplus=50
                    score=score+50
                    object(cupx,cupy,cupsize,scoreobjplus,score)                
                    cupx=round(random.randrange(cupsize+10,width-cupsize-10)/10.0)*10.0
                    cupy=round(random.randrange(cupsize+10,length-cupsize-10)/10.0)*10.0
                    lengths=lengths+1
                    pygame.display.update()
            speed=30
                    
        elif level==3:
            if point_x>=lolix-lolisize and point_x<=lolix+lolisize and point_y>=loliy-lolisize and point_y<=loliy+lolisize:
                score=score+10
                licz=licz+1
                lolix=round(random.randrange(lolisize+10,width-lolisize-10)/10.0)*10.0
                loliy=round(random.randrange(lolisize+10,length-lolisize-10)/10.0)*10.0
                lengths=lengths+1
                pygame.display.update()
                
            if multiplayer==False and score%3==0:
                screen.blit(choco,(chocx,chocy))
                pygame.display.update()
                if point_x>=chocx-chocosize and point_x<=chocx+chocosize and point_y>=chocy-chocosize and point_y<=chocy+chocosize:
                    score=score+50
                    scoreobjplus=50
                    object(chocx,chocy,chocosize,scoreobjplus,score)                
                    chocx=round(random.randrange(chocosize+10,width-chocosize-10)/10.0)*10.0
                    chocy=round(random.randrange(chocosize+10,length-chocosize-10)/10.0)*10.0
                    lengths=lengths+1
                    pygame.display.update()
            speed=40
            
        elif level==4:   
             if point_x>=hambx-hambsize and point_x<=hambx+hambsize and point_y>=hamby-hambsize and point_y<=hamby+hambsize:
                score=score+10
                hambx=round(random.randrange(hambsize+10,width-hambsize-10)/10.0)*10.0
                hamby=round(random.randrange(hambsize+10,length-hambsize-10)/10.0)*10.0
                lengths=lengths+1
                pygame.display.update()
                
                
             if multiplayer==False and score%3==0:
                screen.blit(coke,(cokex,cokey))
                pygame.display.update()
                if point_x>=cokex-cokesize and point_x<=cokex+cokesize and point_y>=cokey-cokesize and point_y<=cokey+cokesize:
                    score=score+50
                    scoreobjplus=50
                    object(cokex,cokey,cokesize,scoreobjplus,score)                
                    cokex=round(random.randrange(cokesize+10,width-cokesize-10)/10.0)*10.0
                    cokey=round(random.randrange(cokesize+10,length-cokesize-10)/10.0)*10.0
                    lengths=lengths+1
                    pygame.display.update()
             speed=50
             
        elif level==5:
            
            if point_x>=pizzx-pizzasize and point_x<=pizzx+pizzasize and point_y>=pizzy-pizzasize and point_y<=pizzy+pizzasize:
                score=score+10
                pizzx=round(random.randrange(pizzasize+10,width-pizzasize-10)/10.0)*10.0
                pizzy=round(random.randrange(pizzasize+10,length-pizzasize-10)/10.0)*10.0
                lengths=lengths+1
                pygame.display.update()
                
                
            if multiplayer==False and score%3==0:
                screen.blit(donut,(donx,dony))
                pygame.display.update()
                if point_x>=donx-donsize and point_x<=donx+donsize and point_y>=dony-donsize and point_y<=dony+donsize:
                    score=score+50
                    scoreobjplus=50
                    object(donx,dony,donsize,scoreobjplus,score)                
                    donx=round(random.randrange(donsize+10,width-donsize-10)/10.0)*10.0
                    dony=round(random.randrange(donsize+10,length-donsize-10)/10.0)*10.0
                    lengths=lengths+1
                    pygame.display.update()
            speed=60
        if score>100 and score<300:
            level=2
        if score>=300 and score<500:
            level=3
        elif score>=500 and score<=700:
            level=4
        elif score>700:
            level=5
        if score>1000:
            screen.blit(winner1,(width/2,length/2))
            pygame.display.update()
            
            
            
        point_x=point_x+x_change   
        point_y=point_y+y_change
        
        point_2x=point_2x+x2_change   
        point_2y=point_2y+y2_change
        
        screen.fill(palegreen)    
        snakeHead=[]
        snakeHead.append(point_x)
        snakeHead.append(point_y)
        snakeList.append(snakeHead)
        
        if len(snakeList)>lengths:
            del snakeList[0]        

        for x in snakeList[:-1]:
            if x==snakeHead:
                gameOver = True
                if multiplayer==True:
                    winner="BLUE SNAKE"
                    gameover2(gameEnd,gameOver,score,score2,winner)
                else:
                    gameover1(gameEnd,gameOver,score)
                    
        if multiplayer==True:
        
            screen.fill(palegreen) 
            
            snakeHead2=[]
            snakeHead2.append(point_2x)
            snakeHead2.append(point_2y)
            snake2List.append(snakeHead2)
            
            if len(snake2List)>lengths2:
                del snake2List[0]        
    
            for x in snake2List[:-1]:
                if x==snakeHead2:
                   gameOver = True
                   winner="GREEN SNAKE"
                   gameover2(gameEnd,gameOver,score,score2,winner)
                   
            for y in snakeList[:-1]:
                if y==snakeHead2:
                    gameOver = True
                    winner="BLUE SNAKE"
                    gameover2(gameEnd,gameOver,score,score2,winner)

                    
            if point_2x==width:
                point_2x=0
            elif point_2x==0:
                point_2x=width
            elif point_2y==length:
                point_2y=0
            elif point_2y==0:
                point_2y=length
            
            if level==1:        
                if point_2x>=applex-applesize and point_2x<=applex+applesize and point_2y>=appley-applesize and point_2y<=appley+applesize:
                    score2=score2+10
                    applex=round(random.randrange(applesize+10,width-applesize-10)/10.0)*10.0
                    y=round(random.randrange(applesize+10,length-applesize-10)/10.0)*10.0
                    lengths2=lengths2+1
                    pygame.display.update()
                
                    
            elif level==2:
                if point_2x>=strawx-strawsize and point_2x<=strawx+strawsize and point_2y>=strawy-strawsize and point_2y<=strawy+strawsize:
                    score2=score2+10
                    licz=licz+1
                    strawx=round(random.randrange(strawsize+10,width-strawsize-10)/10.0)*10.0
                    strawy=round(random.randrange(strawsize+10,length-strawsize-10)/10.0)*10.0
                    lengths2=lengths2+1
                    pygame.display.update()
                    

                speed=30
                
            elif level==3:
                if point_2x>=lolix-lolisize and point_2x<=lolix+lolisize and point_2y>=loliy-lolisize and point_2y<=loliy+lolisize:
                    score2=score2+10
                    lolix=round(random.randrange(lolisize+10,width-lolisize-10)/10.0)*10.0
                    loliy=round(random.randrange(lolisize+10,length-lolisize-10)/10.0)*10.0
                    lengths2=lengths2+1
                    pygame.display.update()
                    
                
            elif level==4:   
                 if point_2x>=hambx-hambsize and point_2x<=hambx+hambsize and point_2y>=hamby-hambsize and point_2y<=hamby+hambsize:
                    score2=score2+10
                    hambx=round(random.randrange(hambsize+10,width-hambsize-10)/10.0)*10.0
                    hamby=round(random.randrange(hambsize+10,length-hambsize-10)/10.0)*10.0
                    lengths2=lengths2+1
                    pygame.display.update()
                 speed=50    
                 
            elif level==5:
                
                if point_2x>=pizzx-pizzasize and point_2x<=pizzx+pizzasize and point_2y>=pizzy-pizzasize and point_2y<=pizzy+pizzasize:
                    score2=score2+10
                    hambx=round(random.randrange(pizzasize+10,width-pizzasize-10)/10.0)*10.0
                    hamby=round(random.randrange(pizzasize+10,length-pizzasize)/10.0)*10.0
                    lengths2=lengths2+1
                    pygame.display.update()
                    
            if point_2x>=bombx-bombsize/2 and point_2x<=bombx+bombsize/2 and point_2y>=bomby-bombsize/2 and point_2y<=bomby+bombsize/2:
                score=int(score/2)
                object(bombx,bomby,bombsize,"BOMB",score)                
                bombx=round(random.randrange(100,width-100)/10.0)*10.0
                bomby=round(random.randrange(100,length-100)/10.0)*10.0
                pygame.display.update()
                
            if point_2x>=bomb2x-bombsize/2 and point_2x<=bomb2x+bombsize/2 and point_2y>=bomb2y-bombsize/2 and point_2y<=bomb2y+bombsize/2:
                score=int(score/2)
                object(bomb2x,bomb2y,bombsize,"BOMB",score)                
                bomb2x=round(random.randrange(100,width-100)/10.0)*10.0
                bomb2y=round(random.randrange(100,length-100)/10.0)*10.0
                pygame.display.update()
                    
        if point_x>=bombx-bombsize/2 and point_x<=bombx+bombsize/2 and point_y>=bomby-bombsize/2 and point_y<=bomby+bombsize/2:
            score=int(score/2)
            object(bombx,bomby,bombsize,"BOMB",score)                
            bombx=round(random.randrange(100,width-100)/10.0)*10.0
            bomby=round(random.randrange(100,length-100)/10.0)*10.0
            pygame.display.update()
            
        if point_x>=bomb2x-bombsize/2 and point_x<=bomb2x+bombsize/2 and point_y>=bomb2y-bombsize/2 and point_y<=bomb2y+bombsize/2:
            score=int(score/2)
            object(bombx,bomby,bombsize,"BOMB",score)                
            bomb2x=round(random.randrange(100,width-100)/10.0)*10.0
            bomb2y=round(random.randrange(100,length-100)/10.0)*10.0
               
        draw_snake(snakeList,size,green)
        screen.blit(graphic,(point_x-35,point_y-30))
        screen.blit(bomb,(bombx,bomby))
        screen.blit(bomb,(bomb2x,bomb2y))

        if multiplayer==True:
            draw_snake(snake2List,size,blue)
            screen.blit(snake2,(point_2x-75,point_2y-50))
        if level==1:
            screen.blit(apple,(applex,appley))
        elif level==2:
            screen.blit(strawberry,(strawx,strawy))
        elif level==3:
            screen.blit(loli,(lolix,loliy)) 
        elif level==4:
            screen.blit(hamb,(hambx,hamby))
        else:
            screen.blit(pizza,(pizzx,pizzy))

        if multiplayer==False:
            quick_texts("LEVEL:"+" "+str(level),black,550,30)
            quick_texts("SCORE:"+" "+str(score),black,650,30)
            
        else:
            quick_texts("LEVEL:"+" "+str(level),black,430,30)
            quick_texts("SCORE 1:"+" "+str(score),green,530,30)
            quick_texts("SCORE 2:"+" "+str(score2),blue,650,30)
            
        if multiplayer==False:
            gameEnd=gameover1(gameEnd,gameOver,score)
        else:
            gameEnd=gameover2(gameEnd,gameOver,score,score2,winner)

        clock.tick(speed)
        pygame.display.update()
GameOn()    
pygame.quit()
quit()
