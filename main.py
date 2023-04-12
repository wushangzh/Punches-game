import random
from winsound import PlaySound
from easygui import *


def show(U, C):
    msgbox('\t————猜拳过程————\n   电脑出了：%s \n   你出了：%s\n' % (C, U), '猜拳', 'OK')


def competition(U, C):
    if ((U == '石头' and C == '剪刀')
            or (U == '剪刀' and C == '布')
            or (U == '布' and C == '石头')):
        PlaySound("欧耶.wav", 1)
        msgbox('\t—————结果—————\n\t你赢了！', '猜拳', '欧耶~')
    elif U == C:
        PlaySound("6.wav", 1)
        msgbox('\t—————结果—————\n\t平局！', '猜拳', '6')
    else:
        PlaySound("屑.wav", 1)
        msgbox('\t—————结果—————\n\t你输了！', '猜拳', '焯！')


while True:
    P = ['石头', '剪刀', '布']
    C = random.choice(P)
    U = buttonbox('请出拳：（石头、剪刀、布）', '猜拳', P, "猜拳.gif")

    show(U, C)
    competition(U, C)

    if ccbox("游戏结束！想再来一次嘛？", "提示", ["再来一次！", "退出，不玩了！"]):
        continue
    else:
        break
