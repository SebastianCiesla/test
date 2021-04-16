import pygame

#Inicialize pygame
pygame.init()

#Window
screen=pygame.display.set_mode((1800,800))

#Font
font=pygame.font.Font('Dustfine.otf',32)
xfont=10
yfont=10
text = '''
SPACE --- acceleration      X  --- delay        B  --- break
'''
def show_font(x,y):
    font_disp=font.render(text,True,(255,0,0))
    screen.blit(font_disp,(x,y))

#---------------
# Start conditions for bug
ambu=pygame.image.load('butterfly.png')
rot=180
xam=500
yam=500
speed=1
radius_start=0

#------------------------
#Wave compute
def wave_calc(wave):
    wave[2]+=wave_speed
    pygame.draw.circle(screen, (255, 0, 0), (wave[0], wave[1]), wave[2], 1)

# ---------------------
# Adding waves to waves list
def wave_creator(x,y):
    return waves_list.append([x,y,radius_start])


#----------------------
#Start conditions for waves
wave_speed=2
waves_list=[]
time=0

running=True
while running:
    # Draw background
    screen.fill((0, 0, 0))

    bug=pygame.transform.rotate(ambu, rot)

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                rot = 360
            if event.key == pygame.K_UP:
                rot = 180
            if event.key == pygame.K_LEFT:
                rot = 270
            if event.key == pygame.K_RIGHT:
                rot = 90
            if event.key == pygame.K_SPACE:
                speed+=1
            if event.key == pygame.K_x:
                speed-=1
            if event.key == pygame.K_b:
                speed=0



    #Adding new circle after 100 loop runs
    time+=1
    if time==100:
        wave_creator(xam,yam)
        time=0

    #Creations
    for waves in waves_list:
        if waves[2]>1500:
            waves_list.remove(waves)
        else:
            wave_calc(waves)




    #Speed of bug
    if speed<=0:
        speed=0

    #Buttertfly dynamics
    if rot == 90:
        xam += speed
    if rot == 180:
        yam -= speed
    if rot == 270:
        xam -= speed
    if rot == 360:
        yam += speed


    #Bug bounds
    if xam>1750:
        xam=1750
    if xam<0:
        xam=0
    if yam<0:
        yam=0
    if yam>750:
        yam=750

    show_font(xfont,yfont)
    screen.blit(bug, (xam, yam))

    pygame.display.update()