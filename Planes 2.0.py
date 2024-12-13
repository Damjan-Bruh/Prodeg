import pygame as pg
import random as rand

pg.font.init()
font = pg.font.Font('freesansbold.ttf', 32)

w = 1000
h = 750

window = pg.display.set_mode((w, h))
pg.display.set_caption('Planes')
bg = pg.transform.scale(pg.image.load('bg.png'), (w, h))

plane_body_width = 200
plane_body_height = 20

plane_wings_width = 15
plane_wings_height = 150

plane_glass_width = 20
plane_glass_height = 10

laser_width = 5
laser_height = 100

player_speed = 5

font_x = 15
font_y = 55

score = 0

def draw(plane_body, plane_wings, plane_glass, laser, laser1, score, font_x, font_y):

    window.blit(bg, (0, 0))

    pg.draw.rect(window, 'black', plane_body)
    pg.draw.rect(window, 'black', plane_wings)
    pg.draw.rect(window, 'blue', plane_glass)
    pg.draw.rect(window, 'red', laser)
    pg.draw.rect(window, 'red', laser1)
    score_image = font.render(f"Score: {str(score)}", True, [255, 255, 255])
    window.blit(score_image, (font_x, font_y))

    pg.display.update()

def main(score, font_x, font_y):

    run = True

    plane_body = pg.Rect(200, 490, plane_body_width, plane_body_height)
    plane_wings = pg.Rect(335, 425, plane_wings_width, plane_wings_height)
    plane_glass = pg.Rect(350, 490, plane_glass_width, plane_glass_height)
    laser = pg.Rect(995, rand.randint(0, 650), laser_width, laser_height)
    laser1 = pg.Rect(995, rand.randint(0, 650), laser_width, laser_height)

    while run:

        for event in pg.event.get():

            if event.type == pg.QUIT:

                run = False
                break
        
        laser.x -= 7
        laser1.x -= 7

        if laser.x <= -5:

            laser.x += 1005
            laser.y = rand.randint(0, 650)
            score += 1

        if laser1.x <= -5:

            laser1.x += 1005
            laser1.y = rand.randint(0, 650)
            score += 1

        keys = pg.key.get_pressed()

        if keys[pg.K_w] or keys[pg.K_UP]:

            plane_body.y -= player_speed
            plane_wings.y -= player_speed
            plane_glass.y -= player_speed

        if keys[pg.K_s] or keys[pg.K_DOWN]:

            plane_body.y += player_speed
            plane_wings.y += player_speed
            plane_glass.y += player_speed

        if laser.y >= plane_wings.y and laser.y <= plane_wings.y + plane_wings_height:

            if laser.x >= plane_wings.x and laser.x <= plane_wings.x + plane_wings_width:

                run = False

        if laser1.y >= plane_wings.y and laser1.y <= plane_wings.y + plane_wings_height:
                
            if laser1.x >= plane_wings.x and laser1.x <= plane_wings.x + plane_wings_width:
            
                run = False

        draw(plane_body, plane_wings, plane_glass, laser, laser1, score, font_x, font_y)

    pg.quit()

if __name__ == '__main__':

    main(score, font_x, font_y)