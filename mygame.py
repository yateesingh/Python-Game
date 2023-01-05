import pygame
import sys
import random
pygame.init()
pygame.display.set_caption("MARIO - BUT BAD")
hello="world"
width=720
height=480
brown=(243,85,35)
white=(255,255,255)
ground=[width,70]
ground_pos=[0,height-ground[1]]
ground_img=pygame.image.load("ground.png")
background=(35,215,243)
cloud_img=pygame.image.load("cloud.png")
cloud_list=[1,2,3,4]
bush_img=pygame.image.load("bush.png")
mount_img=pygame.image.load("mountain.png")
intro_img=pygame.image.load("INTRO.png")
speed=3
speed2=1
score=0
bush_pos=[20,height-140]
mount_pos=[450,height-200]

player_size=[75,123]
player_image=pygame.image.load("mario.png")
player_pos=[250,height-193]


enemy_image=pygame.image.load("goomba1.png")

enemy_dead=pygame.image.load("goomba 2.png")
enemy_pos=[0,height-115]
enemy_size=[51,45]
enemy_list=[1,2]
dead=False
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height))

def move_bgL():
    if (bush_pos[0]+151)>=0:
        bush_pos[0]-=2
    else:
        bush_pos[0]=width
    if (mount_pos[0] + 300 )>=0:
        mount_pos[0]-=2
    else:
        mount_pos[0]=width


    

def level(score):
    if score<15:
        speed=4
    elif score<25:
        speed=5
    elif score<45:
        speed=6
    else:
        speed=7
    return speed

def enemy_maker(enemy_list):
    
    while True:
        
        enemy_list[0]=[random.randint(400,width),height-115]
        enemy_list[1]=[random.randint(400,width),height-115]
        if abs(enemy_list[0][0] - enemy_list[1][0]) >= 300:
            break         

def draw_enemies(enemy_list,enemy_image):
    for enemy in enemy_list:
        if enemy[0] >= 500:
            screen.blit(enemy_image,(enemy[0],enemy[1]))
        elif enemy[0] >=55 and enemy[0]<= 122:
            screen.blit(enemy_image,(enemy[0],enemy[1]))
        else:
             screen.blit(enemy_image,(enemy[0],enemy[1]))
       
def move_enemies(enemy_list,score):
        for enemy in enemy_list:
           if enemy[0]+ enemy_size[0] >=0 :
               enemy[0] -= speed +random.randint(-2,2)
           else:
               
               score+=1
               enemy_list.remove(enemy)
               
        return score
             
def enemy_collision(enemy_list,player_pos):
    for enemy_no in range(len(enemy_list)):
            if collision(player_pos,enemy_list[enemy_no])== True   :
                return True       
    return False

def enemy_escape(enemy):   
    enemy_list.remove(enemy)    

def collision(player_pos,enemy_pos):
    p_x=player_pos[0]
    p_y=player_pos[1]
    e_x=enemy_pos[0]
    e_y=enemy_pos[1]
    if ((e_x >= p_x) and( e_x <= (p_x + player_size[0]))) or ((p_x >= e_x )and (p_x < (e_x+enemy_size[0]))):
        if ((e_y >= p_y)  and (e_y < (p_y + player_size[1]))) or ( (p_y >= e_y) and (p_y < (e_y+ enemy_size[1]))) :
            return True
    return False

myFont=pygame.font.SysFont("comicsans",40,bold=True)


def check_pos(player_pos):
    if player_pos[0]<0 :
        player_pos[0]=width-player_size[0]
    if player_pos[0]+player_size[0] > width:
        player_pos[0]=0

def kill(enemy_list,player_pos):
    for enemy in enemy_list:
        
        p_x=player_pos[0]
        p_y=player_pos[1]
        e_x=enemy[0]
        e_y=enemy[1]
        
        if  ((p_x + player_size[0] <=e_x+enemy_size[0]+20 and p_x + player_size[0] >=e_x+enemy_size[0]-20) or
             (p_x>=e_x-20 and p_x<=e_x+20 and p_y+player_size[1]<=e_y+20) )and p_y+player_size[1]>=e_y-20:
            enemy_escape(enemy)
            return(True)
            
            

def cloud_maker(cloud_list):
    cloud_list[0]=[0,0]
    cloud_list[1]=[200,80]
    cloud_list[2]=[400,30]
    cloud_list[3]=[600,0]

def cloud_put(cloud_list,cloud_img):
    for cloud in cloud_list:
        screen.blit(cloud_img,(cloud[0],cloud[1]))
        
def cloud_move(cloud_list,speed2):
    score=0
    for cloud in cloud_list:
        if cloud[0]+150 >= 0 :
            cloud[0]-=speed2
        else:
            cloud[0]=width-10

cloud_maker(cloud_list)

enemy_maker(enemy_list)
jump_val=10       
jump=False
gameover= False

intro_done=False

while not intro_done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYUP:
            intro_done=True
        
    screen.fill(background)
    cloud_put(cloud_list,cloud_img)
    cloud_move(cloud_list,speed2)
    screen.blit(bush_img,bush_pos)
    screen.blit(mount_img,mount_pos)
    draw_enemies(enemy_list,enemy_image)
    screen.blit(ground_img,ground_pos)
    screen.blit(player_image,player_pos)
    
    screen.blit(intro_img,(150,50))
    
    pygame.display.update()
    
  


while not gameover:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
      
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
         player_pos[0]-=5
        
    if keys[pygame.K_RIGHT]:
         player_pos[0]+=5
       
         
    if not(jump):
        
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            jump=True
           
            
    else:
        if jump_val>=-10:
            neg=1
            if jump_val<0:
                neg=-1
            player_pos[1]-=(jump_val**2 )*0.5*neg
            
            jump_val-=1
        else:
            jump=False
            jump_val=10
   
    screen.fill(background)
    
    clock.tick(39)
    text="SCORE :" +str(score)
    label=myFont.render(text,1,(255,218,4))
    level(score)    
    
    score=move_enemies(enemy_list,score)
    
    cloud_put(cloud_list,cloud_img)
    cloud_move(cloud_list,speed)
    screen.blit(bush_img,bush_pos)
    screen.blit(mount_img,mount_pos)
    draw_enemies(enemy_list,enemy_image)
    speed=level(score)
    
    if enemy_collision(enemy_list,player_pos) ==True:
           gameover=True
    screen.blit(player_image,player_pos)
    screen.blit(label,(10,10))
    check_pos(player_pos)
    p=kill(enemy_list,player_pos)
    if p==True:
        score+=5
 
    if len(enemy_list) <=1:
        x=enemy_list[0][0]
        y=random.randint(200,500)
        enemy_list.append([x+y,height-115])
    move_bgL()   
    screen.blit(ground_img,ground_pos)
    pygame.display.update()
    
else:
    myFont1=pygame.font.SysFont("monospace",40,bold=True)
    text1="GAME OVER"
    labe2=myFont1.render(text1,5,(255,0,0))
    screen.blit(labe2,(260,210))
    pygame.display.update()
    

