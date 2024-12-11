import pygame as pg
import time as tm
from pygame import mixer

mixer.init()

def game():
    
    w = 1000
    h = 750

    window = pg.display.set_mode((w, h))
    pg.display.set_caption('Guy and Arrow')
    bg = pg.transform.scale(pg.image.load('bgga.png'), (w, h))

    gw = 1000
    gh = 375

    pw = 50
    ph = 100

    hw = 50
    hh = 50

    aw = 75
    ah = 10

    av = 7

    def draw(grass, player, head, arrow):

        window.blit(bg, (0, 0))

        pg.draw.rect(window, 'green', grass)
        pg.draw.rect(window, 'red', player)
        pg.draw.rect(window, 'orange', head)
        pg.draw.rect(window, 'brown', arrow)

        pg.display.update()

    def main():

        run = True

        grass = pg.Rect(0, 375, gw, gh)
        player = pg.Rect(200, 275, pw, ph)
        head = pg.Rect(200, 225, hw, hh)
        arrow = pg.Rect(925, 275, aw, ah)

        while run:

            for event in pg.event.get():

                if event.type == pg.QUIT:

                    run = False
                    break
            
            arrow.x -= av

            if arrow.x == -75:
                
                arrow.x += 1000
            
            if arrow.x >= player.x and arrow.x <= player.x + pw:

                if arrow.y >= player.y and arrow.y <= player.y + ph:

                    quit()

            keys = pg.key.get_pressed()

            if keys[pg.K_SPACE]:

                player.y -= 5
                head.y -= 5

                if player.y == 95:

                    player.y += 180
                    head.y += 180

            draw(grass, player, head, arrow)
    
        pg.quit()
    
    if __name__ == '__main__':
        
        main()

game()
