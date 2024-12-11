import pygame as pg
import random as rand

w = 1000
h = 750

gun_width = 100
gun_height = 100

laser_left_width = 75
laser_left_height = 16

laser_up_width = 16
laser_up_height = 75

laser_right_width = 75
laser_right_height = 16

laser_down_width = 16
laser_down_height = 75

bullet_left_width = 32
bullet_left_height = 16

bullet_up_width = 16
bullet_up_height = 32

bullet_right_width = 32
bullet_right_height = 16

bullet_down_width = 16
bullet_down_height = 32

laser_speed = 1

bullet_speed = 5

window = pg.display.set_mode((w, h))
pg.display.set_caption('Laser Atack')
bg = pg.transform.scale(pg.image.load('bg.png'), (w, h))
gun = pg.transform.scale(pg.image.load('gun.png'), (gun_width, gun_height))

def draw(laser_left_1, laser_left_2, laser_left_3, laser_up_1, laser_up_2, laser_up_3, laser_right_1, laser_right_2, laser_right_3, laser_down_1, laser_down_2, laser_down_3, bullet_left_1, bullet_left_2, bullet_left_3, bullet_up_1, bullet_up_2, bullet_up_3, bullet_right_1, bullet_right_2, bullet_right_3, bullet_down_1, bullet_down_2, bullet_down_3):

    window.blit(bg, (0, 0))

    pg.draw.rect(window, 'red', laser_left_1)
    pg.draw.rect(window, 'red', laser_left_2)
    pg.draw.rect(window, 'red', laser_left_3)

    pg.draw.rect(window, 'red', laser_up_1)
    pg.draw.rect(window, 'red', laser_up_2)
    pg.draw.rect(window, 'red', laser_up_3)

    pg.draw.rect(window, 'red', laser_right_1)
    pg.draw.rect(window, 'red', laser_right_2)
    pg.draw.rect(window, 'red', laser_right_3)

    pg.draw.rect(window, 'red', laser_down_1)
    pg.draw.rect(window, 'red', laser_down_2)
    pg.draw.rect(window, 'red', laser_down_3)

    pg.draw.rect(window, 'blue', bullet_left_1)
    pg.draw.rect(window, 'blue', bullet_left_2)
    pg.draw.rect(window, 'blue', bullet_left_3)

    pg.draw.rect(window, 'blue', bullet_up_1)
    pg.draw.rect(window, 'blue', bullet_up_2)
    pg.draw.rect(window, 'blue', bullet_up_3)

    pg.draw.rect(window, 'blue', bullet_right_1)
    pg.draw.rect(window, 'blue', bullet_right_2)
    pg.draw.rect(window, 'blue', bullet_right_3)

    pg.draw.rect(window, 'blue', bullet_down_1)
    pg.draw.rect(window, 'blue', bullet_down_2)
    pg.draw.rect(window, 'blue', bullet_down_3)
    
    window.blit(gun, (450, 325))

    pg.display.update()

def main():

    run = True

    laser_left_1 = pg.Rect(0, 367, laser_left_width, laser_left_height)
    laser_left_2 = pg.Rect(-80, 367, laser_left_width, laser_left_height)
    laser_left_3 = pg.Rect(-160, 367, laser_left_width, laser_left_height)

    laser_up_1 = pg.Rect(492, 0, laser_up_width, laser_up_height)
    laser_up_2 = pg.Rect(492, -80, laser_up_width, laser_up_height)
    laser_up_3 = pg.Rect(492, -160, laser_up_width, laser_up_height)

    laser_right_1 = pg.Rect(925, 367, laser_left_width, laser_right_height)
    laser_right_2 = pg.Rect(1005, 367, laser_left_width, laser_right_height)
    laser_right_3 = pg.Rect(1085, 367, laser_left_width, laser_right_height)

    laser_down_1 = pg.Rect(492, 675, laser_down_width, laser_down_height)
    laser_down_2 = pg.Rect(492, 755, laser_down_width, laser_down_height)
    laser_down_3 = pg.Rect(492, 835, laser_down_width, laser_down_height)

    bullet_left_1 = pg.Rect(484, 367, bullet_left_width, bullet_left_height)
    bullet_left_2 = pg.Rect(484, 367, bullet_left_width, bullet_left_height)
    bullet_left_3 = pg.Rect(484, 367, bullet_left_width, bullet_left_height)

    bullet_up_1 = pg.Rect(492, 359, bullet_up_width, bullet_up_height)
    bullet_up_2 = pg.Rect(492, 359, bullet_up_width, bullet_up_height)
    bullet_up_3 = pg.Rect(492, 359, bullet_up_width, bullet_up_height)

    bullet_right_1 = pg.Rect(484, 367, bullet_right_width, bullet_right_height)
    bullet_right_2 = pg.Rect(484, 367, bullet_right_width, bullet_right_height)
    bullet_right_3 = pg.Rect(484, 367, bullet_right_width, bullet_right_height)

    bullet_down_1 = pg.Rect(492, 359, bullet_down_width, bullet_down_height)
    bullet_down_2 = pg.Rect(492, 359, bullet_down_width, bullet_down_height)
    bullet_down_3 = pg.Rect(492, 359, bullet_down_width, bullet_down_height)

    while run:

        laser_left_1.x += laser_speed

        if laser_left_1.x >= 500:

            laser_left_1.x -= 575

        laser_left_2.x += laser_speed

        if laser_left_2.x >= 500:

            laser_left_2.x -= 575

        laser_left_3.x += laser_speed

        if laser_left_3.x >= 500:

            laser_left_3.x -= 575

        laser_up_1.y += laser_speed

        if laser_up_1.y >= 350:

            laser_up_1.y -= 425

        laser_up_2.y += laser_speed

        if laser_up_2.y >= 350:

            laser_up_2.y -= 425

        laser_up_3.y += laser_speed

        if laser_up_3.y >= 350:

            laser_up_3.y -= 425

        laser_right_1.x -= laser_speed

        if laser_right_1.x <= 500:

            laser_right_1.x += 500

        laser_right_2.x -= laser_speed

        if laser_right_2.x <= 500:

            laser_right_2.x += 500

        laser_right_3.x -= laser_speed

        if laser_right_3.x <= 500:

            laser_right_3.x += 500

        laser_down_1.y -= laser_speed

        if laser_down_1.y <= 350:

            laser_down_1.y += 425

        laser_down_2.y -= laser_speed

        if laser_down_2.y <= 350:

            laser_down_2.y += 425

        laser_down_3.y -= laser_speed

        if laser_down_3.y <= 350:

            laser_down_3.y += 425

        keys = pg.key.get_pressed()

        def left_bullet():

            #bullet_left_1

            if keys[pg.K_a]:

                bullet_left_1.x -= bullet_speed

            if bullet_left_1.x <= laser_left_1.x + laser_left_width:

                bullet_left_1.x += w/2 - (laser_left_1.x + laser_left_width)

                laser_left_1.x -= rand.randint(500, 1000)

            if bullet_left_1.x <= laser_left_2.x + laser_left_width:

                bullet_left_1.x += w/2 - (laser_left_2.x + laser_left_width)

                laser_left_2.x -= rand.randint(500, 1000)

            if bullet_left_1.x <= laser_left_3.x + laser_left_width:

                bullet_left_1.x += w/2 - (laser_left_3.x + laser_left_width)

                laser_left_3.x -= rand.randint(500, 1000)

            #bullet_left_2

            if keys[pg.K_f]:

                bullet_left_2.x -= bullet_speed

            if bullet_left_2.x <= laser_left_1.x + laser_left_width:

                bullet_left_2.x += w/2 - (laser_left_1.x + laser_left_width)

                laser_left_1.x -= rand.randint(500, 1000)

            if bullet_left_2.x <= laser_left_2.x + laser_left_width:

                bullet_left_2.x += w/2 - (laser_left_2.x + laser_left_width)

                laser_left_2.x -= rand.randint(500, 1000)

            if bullet_left_2.x <= laser_left_3.x + laser_left_width:

                bullet_left_2.x += w/2 - (laser_left_3.x + laser_left_width)

                laser_left_3.x -= rand.randint(500, 1000)

            #bullet_left_3

            if keys[pg.K_j]:

                bullet_left_3.x -= bullet_speed

            if bullet_left_3.x <= laser_left_1.x + laser_left_width:

                bullet_left_3.x += w/2 - (laser_left_1.x + laser_left_width)

                laser_left_1.x -= rand.randint(500, 1000)

            if bullet_left_3.x <= laser_left_2.x + laser_left_width:

                bullet_left_3.x += w/2 - (laser_left_2.x + laser_left_width)

                laser_left_2.x -= rand.randint(500, 1000)

            if bullet_left_3.x <= laser_left_3.x + laser_left_width:

                bullet_left_3.x += w/2 - (laser_left_3.x + laser_left_width)

                laser_left_3.x -= rand.randint(500, 1000)
            
        left_bullet()

        def up_bullet():

            #bullet_up_1

            if keys[pg.K_w]:

                bullet_up_1.y -= bullet_speed

            if bullet_up_1.y <= laser_up_1.y + laser_up_height:

                bullet_up_1.y += h/2 - (laser_up_1.y + laser_up_height)

                laser_up_1.y -= rand.randint(500, 1000)

            if bullet_up_1.y <= laser_up_2.y + laser_up_height:

                bullet_up_1.y += h/2 - (laser_up_2.y + laser_up_height)

                laser_up_2.y -= rand.randint(500, 1000)

            if bullet_up_1.y <= laser_up_3.y + laser_up_height:

                bullet_up_1.y += h/2 - (laser_up_3.y + laser_up_height)

                laser_up_3.y -= rand.randint(500, 1000)

            #bullet_up_2

            if keys[pg.K_t]:

                bullet_up_2.y -= bullet_speed

            if bullet_up_2.y <= laser_up_1.y + laser_up_height:

                bullet_up_2.y += h/2 - (laser_up_1.y + laser_up_height)

                laser_up_1.y -= rand.randint(500, 1000)

            if bullet_up_2.y <= laser_up_2.y + laser_up_height:

                bullet_up_2.y += h/2 - (laser_up_2.y + laser_up_height)

                laser_up_2.y -= rand.randint(500, 1000)

            if bullet_up_2.y <= laser_up_3.y + laser_up_height:

                bullet_up_2.y += h/2 - (laser_up_3.y + laser_up_height)

                laser_up_3.y -= rand.randint(500, 1000)

            #bullet_up_3

            if keys[pg.K_i]:

                bullet_up_3.y -= bullet_speed

            if bullet_up_3.y <= laser_up_1.y + laser_up_height:

                bullet_up_3.y += h/2 - (laser_up_1.y + laser_up_height)

                laser_up_1.y -= rand.randint(500, 1000)

            if bullet_up_3.y <= laser_up_2.y + laser_up_height:

                bullet_up_3.y += h/2 - (laser_up_2.y + laser_up_height)

                laser_up_2.y -= rand.randint(500, 1000)

            if bullet_up_3.y <= laser_up_3.y + laser_up_height:

                bullet_up_3.y += h/2 - (laser_up_3.y + laser_up_height)

                laser_up_3.y -= rand.randint(500, 1000)
        
        up_bullet()

        def right_bullet():

            #bullet_right_1

            if keys[pg.K_d]:

                bullet_right_1.x += bullet_speed

            if bullet_right_1.x + bullet_right_width >= laser_right_1.x:

                bullet_right_1.x -= (laser_right_1.x - w/2)

                laser_right_1.x += rand.randint(500, 1000)

            if bullet_right_1.x + bullet_right_width >= laser_right_2.x:

                bullet_right_1.x -= (laser_right_2.x - w/2)

                laser_right_2.x += rand.randint(500, 1000)

            if bullet_right_1.x + bullet_right_width >= laser_right_3.x:

                bullet_right_1.x -= (laser_right_3.x - w/2)

                laser_right_3.x += rand.randint(500, 1000)


            #bullet_right_2

            if keys[pg.K_h]:

                bullet_right_2.x += bullet_speed

            if bullet_right_2.x + bullet_right_width >= laser_right_1.x:

                bullet_right_2.x -= (laser_right_1.x - w/2)

                laser_right_1.x += rand.randint(500, 1000)

            if bullet_right_2.x + bullet_right_width >= laser_right_2.x:

                bullet_right_2.x -= (laser_right_2.x - w/2)

                laser_right_2.x += rand.randint(500, 1000)

            if bullet_right_2.x + bullet_right_width >= laser_right_3.x:

                bullet_right_2.x -= (laser_right_3.x - w/2)

                laser_right_3.x += rand.randint(500, 1000)

            #bullet_right_3

            if keys[pg.K_l]:

                bullet_right_3.x += bullet_speed

            if bullet_right_3.x + bullet_right_width >= laser_right_1.x:

                bullet_right_3.x -= (laser_right_1.x - w/2)

                laser_right_1.x += rand.randint(500, 1000)

            if bullet_right_3.x + bullet_right_width >= laser_right_2.x:

                bullet_right_3.x -= (laser_right_2.x - w/2)

                laser_right_2.x += rand.randint(500, 1000)

            if bullet_right_3.x + bullet_right_width >= laser_right_3.x:

                bullet_right_3.x -= (laser_right_3.x - w/2)

                laser_right_3.x += rand.randint(500, 1000)

        right_bullet()

        def down_bullet():

            #bullet_down_1

            if keys[pg.K_s]:

                bullet_down_1.y += bullet_speed

            if bullet_down_1.y + bullet_down_height >= laser_down_1.y:

                bullet_down_1.y -= (laser_down_1.y - h/2)

                laser_down_1.y += rand.randint(500, 1000)

            if bullet_down_1.y + bullet_down_height >= laser_down_2.y:

                bullet_down_1.y -= (laser_down_2.y - h/2)

                laser_down_2.y += rand.randint(500, 1000)

            if bullet_down_1.y + bullet_down_height >= laser_down_3.y:

                bullet_down_1.y -= (laser_down_3.y - h/2)

                laser_down_3.y += rand.randint(500, 1000)

            #bullet_down_2

            if keys[pg.K_g]:

                bullet_down_2.y += bullet_speed

            if bullet_down_2.y + bullet_down_height >= laser_down_1.y:

                bullet_down_2.y -= (laser_down_1.y - h/2)

                laser_down_1.y += rand.randint(500, 1000)

            if bullet_down_2.y + bullet_down_height >= laser_down_2.y:

                bullet_down_2.y -= (laser_down_2.y - h/2)

                laser_down_2.y += rand.randint(500, 1000)

            if bullet_down_2.y + bullet_down_height >= laser_down_3.y:

                bullet_down_2.y -= (laser_down_3.y - h/2)

                laser_down_3.y += rand.randint(500, 1000)

            #bullet_down_3

            if keys[pg.K_k]:

                bullet_down_3.y += bullet_speed

            if bullet_down_3.y + bullet_down_height >= laser_down_1.y:

                bullet_down_3.y -= (laser_down_1.y - h/2)

                laser_down_1.y += rand.randint(500, 1000)

            if bullet_down_3.y + bullet_down_height >= laser_down_2.y:

                bullet_down_3.y -= (laser_down_2.y - h/2)

                laser_down_2.y += rand.randint(500, 1000)

            if bullet_down_3.y + bullet_down_height >= laser_down_3.y:

                bullet_down_3.y -= (laser_down_3.y - h/2)

                laser_down_3.y += rand.randint(500, 1000)

        down_bullet()

        def game():

            #right_lasers

            if laser_right_1.x + laser_right_width == 450:

                quit()

            if laser_right_2.x + laser_right_width == 450:

                quit()

            if laser_right_3.x + laser_right_width == 450:

                quit()

            #up_lasers

            if laser_up_1.y + laser_up_height == 300:

                quit()

            if laser_up_2.y + laser_up_height == 300:

                quit()

            if laser_up_3.y + laser_up_height == 300:

                quit()

            #right_lasers

            if laser_right_1.x == 450:

                quit()

            if laser_right_2.x == 450:

                quit()

            if laser_right_3.x == 450:

                quit()

            #down_lasers

            if laser_down_1.y == 300:

                quit()

            if laser_down_2.y == 300:

                quit()

            if laser_down_3.y == 300:

                quit()

        game()

        #quit

        for event in pg.event.get():

            if event.type == pg.QUIT:

                run = False
                break

        draw(laser_left_1, laser_left_2, laser_left_3, laser_up_1, laser_up_2, laser_up_3, laser_right_1, laser_right_2, laser_right_3, laser_down_1, laser_down_2, laser_down_3, bullet_left_1, bullet_left_2, bullet_left_3, bullet_up_1, bullet_up_2, bullet_up_3, bullet_right_1, bullet_right_2, bullet_right_3, bullet_down_1, bullet_down_2, bullet_down_3)

    pg.quit()
    
if __name__ == '__main__':

    main()