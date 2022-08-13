import pygame, sys, time, random, math
from pygame.locals import * # constants
from tools import *
from player import Player
from button import Button
from coin import Coin

def main():
    pygame.init()

    # display
    size = (640, 480)
    DISPLAY = pygame.display.set_mode(size)
    pygame.display.set_caption('Hellarich')
    pygame.display.set_icon(Coin().sprite)
    # colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    YELLOW = (235,235,0)
    PURPLE = (139,0,61)
    # fonts
    font_13 = pygame.font.Font('data/fonts/font.otf', 13)
    font_25 = pygame.font.Font('data/fonts/font.otf', 25)
    font_32 = pygame.font.Font('data/fonts/font.otf', 32)
    # images
    shop = pygame.image.load('data/images/shop.png')
    logo = pygame.image.load('data/images/logo_purple.png')
    start_button = pygame.image.load('data/images/start_button.png')
    final = pygame.image.load('data/images/final.png')
    bg_title = pygame.image.load('data/images/bg_title.png')
    bg_info = pygame.image.load('data/images/bg_info.png')
    bg_game = pygame.image.load('data/images/bg_game.png')
    # sounds
    s_coin = pygame.mixer.Sound("data/sounds/coin.wav")
    s_forte = pygame.mixer.Sound("data/sounds/forte.mp3")
    s_upgrade = pygame.mixer.Sound("data/sounds/upgrade.wav")
    s_final = pygame.mixer.Sound("data/sounds/lessgo.mp3")
    # objects
    player = Player()
    coins = []
    buttons = []
    for i in range(3): 
        buttons.append(Button())
    buttons[0].sprite = pygame.image.load('data/images/button_speed.png')
    buttons[1].sprite = pygame.image.load('data/images/button_money.png')
    buttons[2].sprite = pygame.image.load('data/images/button_rich.png')
    button_info = Button()
    button_info.sprite = pygame.image.load('data/images/button.png')

    # MADE BY
    for i in range(8000):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(WHITE)
        startMsg = font_32.render("Made by Infibiss", True, (BLACK))
        DISPLAY.blit(startMsg, (DISPLAY.get_width() / 2 - startMsg.get_width() / 2, DISPLAY.get_height() / 2 - startMsg.get_height() / 2))
            
        pygame.display.update()

    ### TITLE SCREEN
    titleScreen = True
    while titleScreen:
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        mouseX, mouseY = pygame.mouse.get_pos()  
        if clicked and Check(mouseX, mouseY, 1, 1, DISPLAY.get_width() / 2 - start_button.get_width() / 2, 288, start_button.get_width(), start_button.get_height()):
            titleScreen = False
        
        DISPLAY.fill(WHITE)
        DISPLAY.blit(bg_title, (0,0)) 
        DISPLAY.blit(logo, (DISPLAY.get_width() / 2 - logo.get_width() / 2, DISPLAY.get_height() / 2 - logo.get_height() / 2 + math.sin(time.time() * 5) * 5 - 75)) # 1 - speed 2 - distance
        DISPLAY.blit(start_button, (DISPLAY.get_width() / 2 - start_button.get_width() / 2, 288))

        pygame.display.update()

    ### GAME
    numofcoins = [5] * 1 + [4] * 2 + [3] * 3 + [2] * 4 + [1] * 5 + [0] * 1985
    cntcoins = [1999, 1699, 1399, 1099, 699, 399, 30]
    valuecoins = [1] * 85 + [3] * 12 + [5] * 3
    price_speed = [15, 50, 100, 300, 500, 800, 1100, 1300, 1700, 99999]
    price_money = [50, 150, 300, 600, 900, 1300, 99999]
    price_rich = [70, 200, 600, 1000, 1300, 1700, 99999]
    buttons[0].price = price_speed[0]
    buttons[1].price = price_money[0]
    buttons[2].price = price_rich[0]
    maxlvl = [9, 6, 6]
    buttonW, buttonH = 80, 60
    button_infoX, button_infoY = 260, 420
    end, secret = 0, 0

    while True:
        # player position
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseY < 400:
            player.position.x = GetPos(player, mouseX - player.sprite.get_width() / 2 + 2) # center of player
            player.position.x = min(640 - player.sprite.get_width(), player.position.x) # right border
            player.position.x = max(0, player.position.x) # left border

        # if buttons clicked
        clicked = [False] * 3
        clicked_info = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in range(3):
                    if Check(mouseX, mouseY, 1, 1, 355 + i * 90, 415, buttonW, buttonH):
                        clicked[i] = True
                if Check(mouseX, mouseY, 1, 1, button_infoX, button_infoY, 80, 40):
                    clicked_info = True
                if Check(mouseX, mouseY, 1, 1, 15, 425, 50, 50): # secret
                    secret += 1
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # if secret
        if secret == 10:
            pygame.mixer.Sound.play(s_forte)
            bg_game = pygame.image.load('data/images/forte_evalar.png')
            player.sprite = pygame.image.load('data/images/forte_sanitar.png')
            secret = 0

        # info window
        if clicked_info:
            while True:
                mouseX, mouseY = pygame.mouse.get_pos()
                exit = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if Check(mouseX, mouseY, 1, 1, 405, 220, 80, 40):
                            exit = True
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if exit:
                    break

                DISPLAY.fill(WHITE)
                DISPLAY.blit(bg_info, (0, 0))
                DISPLAY.blit(button_info.sprite, (405, 220)) 
                back = font_25.render("BACK", True, (BLACK))
                DISPLAY.blit(back, (423, 225))
                pygame.display.update()

        # upgrade
        for i in range(3):
            if clicked[i]:
                if buttons[i].lvl <= maxlvl[i] and player.money >= buttons[i].price:
                    player.money -= buttons[i].price
                    pygame.mixer.music.stop()
                    if i == 0:
                        pygame.mixer.Sound.play(s_upgrade)
                        player.speed += 1
                        buttons[0].price = price_speed[buttons[0].lvl]
                    if i == 1:
                        pygame.mixer.Sound.play(s_upgrade)
                        buttons[1].price = price_money[buttons[1].lvl]
                    if i == 2:
                        pygame.mixer.Sound.play(s_final)
                        bg_game = pygame.image.load('data/images/bg_game.png') # make default from secret
                        path = 'data/images/player' + str(buttons[2].lvl + 1) + '.png'
                        player.sprite = pygame.image.load(path)
                        buttons[2].price = price_rich[buttons[2].lvl]
                    buttons[i].lvl += 1
        
        # if final
        flag = True
        for i in range(3):
            if buttons[i].lvl <= maxlvl[i]:
                flag = False
        end += flag
        if end > 100:
            time.sleep(2)
            break

        ### PRINT
        DISPLAY.fill(WHITE)
        DISPLAY.blit(bg_game, (0, 0)) 
        DISPLAY.blit(shop, (0, 0))
        # buttons
        DISPLAY.blit(button_info.sprite, (button_infoX, button_infoY)) 
        info = font_25.render("INFO", True, (BLACK))
        DISPLAY.blit(info, (283, 425))
        for button in buttons:
            DISPLAY.blit(button.sprite, (350 + buttons.index(button) * 90, 400)) 
            price = font_13.render("Cost: " + GetPrice(button, maxlvl[buttons.index(button)]), True, (BLACK))
            lvl = font_13.render("lvl: " + GetLvl(button, maxlvl[buttons.index(button)]), True, (BLACK))
            DISPLAY.blit(price, (362 + buttons.index(button) * 90, 450))
            DISPLAY.blit(lvl, (415 + buttons.index(button) * 90, 450))
        # create coins
        idx = random.randint(0, cntcoins[buttons[1].lvl - 1]) # num of coins
        for i in range(numofcoins[idx]): 
            coin = Coin()
            coin.value = valuecoins[random.randint(0, 99)] # value of coin
            path = 'data/images/coinx' + str(coin.value) + '.png'
            coin.sprite = pygame.image.load(path)
            coin.position.xy = random.randint(0, DISPLAY.get_width() - coin.sprite.get_width()), 0
            coins.append(coin)
        # draw and remove coins
        idx = 0
        while idx < len(coins):
            coin = coins[idx]
            coin.position.y += 1
            delete = False
            if Check(player.position.x + 5, player.position.y, player.sprite.get_width() - 15, player.sprite.get_height(), coin.position.x, coin.position.y, coin.sprite.get_width(), coin.sprite.get_height()):
                pygame.mixer.Sound.play(s_coin)
                player.money += coin.value
                delete = True
            if delete or coin.position.y >= 380:
                coins.pop(idx)
                continue
            DISPLAY.blit(coin.sprite, (coin.position.x, coin.position.y))
            idx += 1
        # coin counter
        cnt = font_32.render(GetCoinCount(player.money), True, (BLACK))
        DISPLAY.blit(cnt, (70, 423))
        # player
        DISPLAY.blit(player.sprite, (player.position.x, player.position.y))

        pygame.display.update()


    ### FINAL
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(s_final)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(WHITE)
        DISPLAY.blit(final, (0,0))

        pygame.display.update()

if __name__ == "__main__":
    main()