import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

r1_pos = 100#screen.get_width() / 3
rect1 = pygame.Rect(r1_pos, 480, 0, 0).inflate(40, 40)
v1 = 0
m1 = 1
r2_pos = 200#screen.get_width() / 3 * 2
rect2 = pygame.Rect(r2_pos, 480, 0, 0).inflate(40, 40)
v2 = -500000
m2 = 1000000
wall = pygame.Rect(20, 460, 20, 80)
collision_count = 0

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if r1_pos + 20 >= r2_pos - 20 and (v1 >= v2):
        v1i = v1
        v2i = v2
        v1 = v1i + 2*m2*(v2i - v1i)/(m1 + m2)
        v2 = v2i + 2*m1*(v1i - v2i)/(m1 + m2)
        collision_count += 1

    if r1_pos < 60 and v1 < 0:
        v1 *= -1
        collision_count += 1

    r1_pos += dt * v1
    r2_pos += dt * v2

    rect1.centerx = r1_pos
    rect2.centerx = r2_pos

    screen.fill("black")
    pygame.draw.rect(screen, "red", rect1)
    pygame.draw.rect(screen, "blue", rect2)
    pygame.draw.rect(screen, "white", wall)

    if v2 >= v1 >= 0 and r1_pos < r2_pos:
        running = False
        print("collision:", collision_count)

    pygame.display.flip()

    dt = clock.tick(6000) / 10000000
    clock.tick(6000)  # limits FPS to 60

pygame.quit()