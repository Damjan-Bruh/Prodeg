import pygame as pg
import random as rand

w = 1000
h = 750

window = pg.display.set_mode((w, h))
pg.display.set_caption('Dodger')
bg = pg.transform.scale(pg.image.load('bgdg.png'), (w, h))

player_width = 50
player_height = 100

head_width = 26
head_height = 25

bomb_width = 25
bomb_height = 50

player_speed = 5

fast_speed = 10

bomb_speed = 4

def draw(player, head, bomb_1, bomb_2, bomb_3):

    window.blit(bg, (0, 0))

    pg.draw.rect(window, 'red', player)
    pg.draw.rect(window, 'yellow', head)
    pg.draw.rect(window, 'darkgreen', bomb_1)
    pg.draw.rect(window, 'darkgreen', bomb_2)
    pg.draw.rect(window, 'darkgreen', bomb_3)

    pg.display.update()

def main():

    run = True

    player = pg.Rect(rand.randint(0, 950), 325, player_width, player_height)
    head = pg.Rect(player.x + 12, 300, head_width, head_height)
    bomb_1 = pg.Rect(rand.randint(0, 975), 0, bomb_width, bomb_height)
    bomb_2 = pg.Rect(rand.randint(0, 975), 0, bomb_width, bomb_height)
    bomb_3 = pg.Rect(rand.randint(0, 975), 0, bomb_width, bomb_height)

    while run:

        bomb_1.y += bomb_speed
        bomb_2.y += bomb_speed
        bomb_3.y += bomb_speed

        if bomb_1.y >= 750:

            bomb_1.y -= 800
            bomb_1.x = rand.randint(0, 975)

        if bomb_2.y >= 750:

            bomb_2.y -= 800
            bomb_2.x = rand.randint(0, 975)

        if bomb_3.y >= 750:

            bomb_3.y -= 800
            bomb_3.x = rand.randint(0, 975)
        
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:

            player.x -= player_speed
            head.x -= player_speed

        if keys[pg.K_LEFT]:

            player.x -= fast_speed
            head.x -= fast_speed

        if keys[pg.K_d]:

            player.x += player_speed
            head.x += player_speed

        if keys[pg.K_RIGHT]:

            player.x += fast_speed
            head.x += fast_speed

        if bomb_1.x >= player.x and bomb_1.x <= player.x + player_width:

            if bomb_1.y >= player.y:

                run = False

        if bomb_2.x >= player.x and bomb_2.x <= player.x + player_width:

            if bomb_2.y >= player.y:

                run = False

        if bomb_3.x >= player.x and bomb_3.x <= player.x + player_width:

            if bomb_3.y >= player.y:

                run = False
            
        for event in pg.event.get():

            if event.type == pg.QUIT:

                run = False
                break

        draw(player, head, bomb_1, bomb_2, bomb_3)

    pg.quit()

if __name__ == '__main__':

    main()
