from pygame import *
import sys

init()

bat_image = image.load("batman.png")
bat_image = transform.scale(bat_image, (200,200))



mixer.music.load()

Vader_image = image.load("dvpng.webp")
Vader_image = transform.scale(Vader_image, (200,200))



window = display.set_mode((1280,720))

window.fill((151,209,250))



while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    # Deve desenhar a partir daqui
    draw.rect(window,(72,155,37),(0,600,1280,120) )
    draw.rect(window,(121,77,27),(1000,300,50,300))
    draw.rect(window,(100,100,100),(300,300,300,300))
    draw.circle(window,(72,155,37),(1020,300),100)
    draw.polygon(window,(242,136,59),((300,300,),(450,150),(600,300)))
    


    # Desenhar Imagem (Tiradas da internet)
    window.blit(bat_image,(100,400))
    window.blit(Vader_image,(600,410))

    # Desenhar Textos
    batman_text = batman_font.render('I am Batman',True,(0,0,0))
    window.blit(batman_text,(100,400))


    
    
    
    
    
    
    display.update()
