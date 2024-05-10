import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Звездная схватка")

rocket_image = pygame.image.load("rocket.png")
rocket_rect = rocket_image.get_rect()

bullet_image = pygame.image.load("bullet.png")
bullet_rect = bullet_image.get_rect()

enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()

meteor_image = pygame.image.load('meteor.png')
meteor_rect = meteor_image.get_rect()

planet_image1 = pygame.image.load("земля.png")
planet_rect1 = planet_image1.get_rect()

planet_image2 = pygame.image.load("меркурий.png")
planet_rect2 = planet_image2.get_rect()

planet_image3 = pygame.image.load("марс.png")
planet_rect3 = planet_image3.get_rect()

planet_image4 = pygame.image.load("венера.png")
planet_rect4 = planet_image4.get_rect()

planet_image5 = pygame.image.load("сатурн.png")
planet_rect5 = planet_image5.get_rect()

planet_image6 = pygame.image.load("юпитер.png")
planet_rect6 = planet_image6.get_rect()

planet_image7 = pygame.image.load("нептун.png")
planet_rect7 = planet_image7.get_rect()


rocket_rect.x = WIDTH // 2 - rocket_rect.width // 2
rocket_rect.y = HEIGHT - rocket_rect.height - 10

planet_rect1.x = 100
planet_rect1.y = 80

planet_rect2.x = 150
planet_rect2.y = 250

planet_rect3.x = 650
planet_rect3.y = 400

planet_rect4.x = 560
planet_rect4.y = 520

planet_rect5.x = 500
planet_rect5.y = 200

planet_rect6.x = 220
planet_rect6.y = 470

planet_rect7.x = 480
planet_rect7.y = 50

rocket_speed = 5
bullet_speed = 8
enemy_speed = 3
meteor_speed = 3

bullets = []
enemies = []
meteors = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet_rect = bullet_image.get_rect()
            bullet_rect.x = rocket_rect.x + rocket_rect.width // 2 - bullet_rect.width // 2
            bullet_rect.y = rocket_rect.y
            bullets.append(bullet_rect)

    screen.fill((0, 0, 128))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and rocket_rect.x < WIDTH - rocket_rect.width:
        rocket_rect.x += rocket_speed
    if keys[pygame.K_LEFT] and rocket_rect.x > 0:
        rocket_rect.x -= rocket_speed

    for bullet in bullets:
        bullet.y -= bullet_speed

    bullets = [bullet for bullet in bullets if bullet.y > 0]

    if random.randint(1,130) <= 2:
        meteor_rect = meteor_image.get_rect()
        meteor_rect.x = random.randint(0, WIDTH - meteor_rect.width)
        meteor_rect.y = 0
        meteors.append(meteor_rect)

    if random.randint(1,100) <= 3:
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)
        enemy_rect.y = 0
        enemies.append(enemy_rect)

    for meteor in meteors:
        meteor.y += meteor_speed
        if meteor.y + meteor.height > HEIGHT:
            meteors.remove(meteor)

    for meteor in meteors:
        if meteor.colliderect(rocket_rect):
            meteors.remove(meteor)

    for bullet in bullets:
        for meteor in meteors:
            if bullet.colliderect(meteor):
                bullets.remove(bullet)
                meteors.remove(meteor)

    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y + enemy.height > HEIGHT:
            enemies.remove(enemy)

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)


    for bullet in bullets:
        screen.blit(bullet_image, bullet)

    for enemy in enemies:
        screen.blit(enemy_image, enemy)

    for meteor in meteors:
        screen.blit(meteor_image, meteor)

    screen.blit(planet_image1, planet_rect1)
    screen.blit(planet_image2, planet_rect2)
    screen.blit(planet_image3, planet_rect3)
    screen.blit(planet_image4, planet_rect4)
    screen.blit(planet_image5, planet_rect5)
    screen.blit(planet_image6, planet_rect6)
    screen.blit(planet_image7, planet_rect7)
    screen.blit(rocket_image, rocket_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

print('hello world!')






