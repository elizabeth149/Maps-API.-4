import sys
import requests
import pygame

address_ll = ",".join(sys.argv[1:3])
size = 3
response = None

def sizze(r):
    global address_ll
    global response
    sp = f"https://static-maps.yandex.ru/1.x/?ll={address_ll}&z={r}&l=sat"
    response = requests.get(sp)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((600, 450))
sizze(size)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if 0 <= size + 1 <= 18:
                size += 1
                sizze(size)
        if keys[pygame.K_DOWN]:
            if 0 <= size - 1 <= 18:
                size -= 1
                sizze(size)
