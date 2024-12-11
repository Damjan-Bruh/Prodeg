import pygame as pg
from pygame import mixer
import time as tm
import random as rand
mixer.init()
def game():
    pg.font.init()
    w = 1000
    h = 750
    px = rand.randint(1, 1000)
    py = 940
    WIN = pg.display.set_mode((w, h))
    pg.display.set_caption("Enemy Shooter classic 10062024")
    BG = pg.transform.scale(pg.image.load("bges.png"), (w, h))
    PW = 150
    PH = 350
    PH1 = 200
    PW2 = 30
    PH2 = 30
    GH = 300
    GW = 1000
    EW = 76
    EH = 150
    HR = 50
    TW = 50
    TV = 10
    PV = 5
    PVB = 10
    def draw(grass, enemy, head, player, player1, player2, elapsed_time, time):
        WIN.blit(BG, (0, 0))
        pg.draw.rect(WIN, "lime", grass)
        pg.draw.rect(WIN, "red", enemy)
        pg.draw.rect(WIN, "yellow", head)
        pg.draw.rect(WIN, (100, 100, 100), player)
        pg.draw.rect(WIN, (200, 200, 200), player1)
        pg.draw.rect(WIN, (100, 100, 100), player2)
        pg.draw.rect(WIN, "lime", time)
        pg.display.update()
    def main():
        run = True
        grass = pg.Rect(0, 450, GW, GH)
        enemy = pg.Rect(rand.randint(74, 924), 300, EW, EH)
        head = pg.Rect(enemy.x + 13, 250, HR, HR)
        player = pg.Rect(rand.randint(1, 1000), 400, PW, PH)
        player1 = pg.Rect(player.x, 200, PW, PH1)
        player2 = pg.Rect(player.x + 60, 170, PW2, PH2)
        time = pg.Rect(950, 0, TW, TW)
        tm.sleep(3)
        clock = pg.time.Clock()
        start_time = tm.time()
        elapsed_time = 0
        while run:
            clock.tick(60)
            elapsed_time = tm.time() - start_time
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    break
            if elapsed_time == 0:
                run = False
                break
            TXW = w - time.x
            time.x -= TV
            keys = pg.key.get_pressed()
            if keys[pg.K_a] and player.x - PV >= 0:
                player.x -= PV
                player1.x -= PV
                player2.x -= PV
            if keys[pg.K_LEFT] and player.x - PVB >= 0:
                player.x -= PVB
                player1.x -= PVB
                player2.x -= PVB
            if keys[pg.K_d] and player.x + PV <= w:
                player.x += PV
                player1.x += PV
                player2.x += PV
            if keys[pg.K_RIGHT] and player.x + PVB <= w:
                player.x += PVB
                player1.x += PVB
                player2.x += PVB
            if keys[pg.K_s]:
                if player.x + 75 >= enemy.x:
                    if player.x + 75 <= enemy.x + 76:
                        enemy.x = rand.randint(1, 924)
                        head.x = enemy.x + 13
                        time.x += TXW
                        mixer.music.load('gunshot.mp3')
                        mixer.music.play()
            if keys[pg.K_DOWN]:
                if player.x + 75 >= enemy.x:
                    if player.x + 75 <= enemy.x + 76:
                        enemy.x = rand.randint(1, 924)
                        head.x = enemy.x + 13
                        time.x += TXW
                        mixer.music.load('gunshot.mp3')
                        mixer.music.play()
            if time.x <= 0:
                tm.sleep(3)
                quit()
            draw(grass, enemy, head, player, player1, player2, elapsed_time, time)
        pg.quit()
    if __name__ == "__main__":
        main()
game()
