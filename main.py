from random import randint

import pygame

pygame.init()
## Muutujad

# Värvid
toiduvarv = (165, 42, 42)
boonusvarv = (255, 165, 0)
maovarv = (124, 252, 0)
ekraanivarv = (245, 245, 220)
seinavarv = (255, 0, 0)

# Suurused
madu_korgus = 15
madu_laius = 15
madu_vahe = 3  # Mao juppide vahe

# Muu
kiirus = 250  # 1000 = 1sec
skoor = 0
liigu_x = 0  # X teljel liikumine
liigu_y = madu_laius + madu_vahe  # Y teljel liiumine, hetkel määrab liikumisuunaks alla
mang = True  # Kui false siis mäng ei käi

# Ristkülikud
ekraan = pygame.display.set_mode((600, 600))  # Määrab mängu resolutsiooni

seinad = [
    pygame.Rect(0, 0, 570, 30),
    pygame.Rect(0, 570, 570, 30),
    pygame.Rect(0, 0, 30, 600),
    pygame.Rect(570, 0, 30, 600)
]

madu = []  # Tühi list, hiljem sisaldab mao juppe

toit = pygame.Rect((30 + (18 * randint(0, 29))), (30 + (18 * randint(0, 29))), madu_laius, madu_korgus)
print(toit)

##Funktsioonid

def liigu(x, y, force):
    global skoor, kiirus, madu_laius, madu_korgus, toit
    jupp = pygame.Rect(x, y, madu_laius, madu_korgus)
    for i in madu:
        if jupp.colliderect(i):
            surm()
    for i in seinad:
        if jupp.colliderect(i):
            surm()
    if jupp.colliderect(toit) or force == True:
        madu.append(jupp)
        pygame.draw.rect(ekraan, ekraanivarv, toit)
        pygame.draw.rect(ekraan, maovarv, jupp)
        toit = pygame.Rect((30 + (8 * randint(0, 29))), (30 + (18 * randint(0, 29))), madu_laius, madu_korgus)
        pygame.draw.rect(ekraan, toiduvarv, toit)
        print(toit)
        skoor = skoor + 1
        kiirus = kiirus - 5
        print(skoor)
    else:
        pygame.draw.rect(ekraan, ekraanivarv, madu.pop(0))
        pygame.draw.rect(ekraan, maovarv, jupp)
        madu.append(jupp)


def surm():
    global mang
    mang = False


def pea():  # Aju
    global x, y, liigu_x, liigu_y
    while mang:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    liigu_x = 0
                    liigu_y = (madu_vahe + madu_korgus) * -1
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    liigu_x = (madu_vahe + madu_laius) * -1
                    liigu_y = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    liigu_x = 0
                    liigu_y = (madu_vahe + madu_korgus)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    liigu_x = (madu_vahe + madu_laius)
                    liigu_y = 0
        x = x + liigu_x
        y = y + liigu_y
        liigu(x, y, False)
        pygame.display.flip()  # uus kaader
        pygame.time.wait(kiirus)
    if mang == False:
        print(skoor)  # Hiljem tekitab hüpikakna skooriga vms

## Graafika

pygame.display.set_caption("Snake v0.1")  # Määrab akna pealkirja
ekraan.fill(ekraanivarv)  # Värvib tausta

for i in seinad:  # Tekitab 4 seina
    pygame.draw.rect(ekraan, seinavarv, i)

for i in range(5):  # Tekitab 5 tükilise mao
    x = 230
    y = 140 + ((madu_korgus + madu_vahe) * i)
    liigu(x, y, True)

pygame.draw.rect(ekraan, toiduvarv, toit)
pygame.display.flip()

pea()
