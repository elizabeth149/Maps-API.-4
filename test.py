import sys
import requests
import pygame

address_ll = float(sys.argv[1])
address_ll_2 = float(sys.argv[2])
response = None


def sizze():
    global address_ll
    global address_ll_2
    global response
    sp = f"https://static-maps.yandex.ru/1.x/?ll={address_ll},{address_ll_2}" \
         f"&z=5&l=sat"
    response = requests.get(sp)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((600, 450))
sizze()
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if 0 <= address_ll_2 + 1 <= 180:
                address_ll_2 += 0.1
                sizze()
        if keys[pygame.K_DOWN]:
            if 0 <= address_ll_2 - 1 <= 180:
                address_ll_2 -= 0.1
                sizze()
        if keys[pygame.K_LEFT]:
            if 0 <= address_ll - 1 <= 180:
                address_ll -= 0.1
                sizze()
        if keys[pygame.K_RIGHT]:
            if 0 <= address_ll + 1 <= 180:
                address_ll += 0.1
                sizze()
