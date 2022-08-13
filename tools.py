from player import Player
from button import Button

def GetPos(player, mouseX):
    if player.position.x < mouseX:
        return min(player.position.x + player.speed, mouseX)
    else:
        return max(player.position.x - player.speed, mouseX)

def GetCoinCount(money):
    if money >= 10000:
        return "HELLA RICH!"
    return str(money // 10000 % 10) + str(money // 1000 % 10) + str(money // 100 % 10) + str(money // 10 % 10) + str(money % 10)

def GetPrice(button, maxlvl):
    if button.lvl > maxlvl:
        return "MAX"
    return str(button.price)

def GetLvl(button, maxlvl):
    if button.lvl > maxlvl:
        return "X"
    return str(button.lvl)

def Check(a_x, a_y, a_w, a_h, b_x, b_y, b_w, b_h): # left up coordinates and width, height
    return (a_x + a_w >= b_x) and (a_x <= b_x + b_w) and (a_y + a_h >= b_y) and (a_y <= b_y + b_h)
