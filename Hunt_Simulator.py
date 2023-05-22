import pygame
import random
from pygame import mixer 

# Initialize pygame
pygame.init()

# Set up the display
height = 600
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hunt Simulator")
FPS = 60
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# Load the duck and gun images, background, crosshair etc
duck_img = pygame.image.load("C:/Users/TRiiTRii/Desktop/Hunt Simulator/images/bird1.png")
gun_img = pygame.image.load("C:/Users/TRiiTRii/Desktop/Hunt Simulator/images/gun.png")
background_img = pygame.image.load("C:/Users/TRiiTRii/Desktop/Hunt Simulator/images/background.png")
background_img = pygame.transform.scale(background_img, (width, height))
crosshair_image = pygame.image.load("C:/Users/TRiiTRii/Desktop/Hunt Simulator/images/crosshair.png")
crosshair_width, crosshair_height = crosshair_image.get_size()

# Load the Sound
gun_sound = mixer.Sound("C:/Users/TRiiTRii/Desktop/Hunt Simulator/sounds/gun_sound.wav")
hit_sound = mixer.Sound("C:/Users/TRiiTRii/Desktop/Hunt Simulator/sounds/hit_sound.wav")
background_sound = mixer.music.load("C:/Users/TRiiTRii/Desktop/Hunt Simulator/sounds/background_sound.wav")
mixer.music.play(-1,0.0)
mixer.music.set_volume(0.60)


# Set the duck's initial position
duck_x = 0
duck_y = 100

# Set the duck speed
duck_speed = 15

# Set duck spawn range 
duck_spawn_max = 250
duck_spawn_min = 1

# Set duck height
duck_img_height = 80
duck_img = pygame.transform.scale(duck_img, (duck_img_height, duck_img_height))
duck_img_height_min = 50
duck_img_height_max = 130

# Set the score
score = 0

# Set the number of ducks
ducks_left = 20

# Set up the game loop
running = True
paused = False

while running:
  #  background_sound.play(-1,0.0)
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_p:
                paused = not paused  # Toggle the paused state
                if not paused:
                    mixer.music.unpause()
    
    if not paused:
    
        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check if the left mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            gun_sound.play()
            # Check if the mouse is over the duck
            if (
                mouse_x > duck_x
                and mouse_x < duck_x + duck_img.get_width()
                and mouse_y > duck_y
                and mouse_y < duck_y + duck_img.get_height()
            ):
                # The duck was hit
                hit_sound.play()
                duck_speed += 1
                score += 1
                ducks_left -= 1
                # Reset the duck's position
                duck_x = 0
                duck_y = random.randint(duck_spawn_min, duck_spawn_max)
                duck_img = pygame.image.load("C:/Users/TRiiTRii/Desktop/pygame/PNG/images/alien.png")
                duck_img_height = random.randint(duck_img_height_min, duck_img_height_max)
                duck_img = pygame.transform.scale(duck_img, (duck_img_height, duck_img_height))

        # Move the duck
        duck_x += duck_speed

        # Check if the duck is off the screen
        if duck_x > width:
            duck_x = random.randint(0, 0)
            duck_y = random.randint(duck_spawn_min, duck_spawn_max)
            ducks_left -= 1

            # Check if the duck was not hit
            if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
                # Decrease the duck speed
                if duck_speed > 3:
                    duck_speed -= 1
                    duck_x = 0
                    duck_y = random.randint(duck_spawn_min, duck_spawn_max)
                    ducks_left -= 1
                    duck_img = pygame.image.load("C:/Users/TRiiTRii/Desktop/pygame/PNG/images/alien.png")
                    duck_img_height = random.randint(duck_img_height_min, duck_img_height_max)
                    duck_img = pygame.transform.scale(duck_img, (duck_img_height, duck_img_height))

        # Draw the background
        screen.blit(background_img, (0, 0))

        # Draw the duck
        if ducks_left >= 1:
            screen.blit(duck_img, (duck_x, duck_y))

        # Draw the gun
        screen.blit(gun_img, (mouse_x, mouse_y))

        # Crosshair placement
        crosshair_x = mouse_x - (crosshair_width / 2)
        crosshair_y = mouse_y - (crosshair_height / 2)

        # Right position of the Crosshair
        screen.blit(crosshair_image, (crosshair_x, crosshair_y))

        # Draw the score
        score_text = "Score: {}".format(score)
        score_surface = pygame.font.Font(None, 30).render(score_text, True, (255, 255, 255))
        screen.blit(score_surface, (650, 550))

        if ducks_left <= 0:
            final_text = "Final Score: {}".format(score)
            final_surface = pygame.font.Font(None, 50).render(final_text, True, (0, 0, 0))
            screen.blit(final_surface, (250, 300))
    else:
        #stop the music
        mixer.music.pause()
        # Paused menu code
        screen.fill((0, 0, 0))  # Fill the screen with black

        # Draw the paused text
        paused_text = pygame.font.Font(None, 50).render("Paused", True, (255, 255, 255))
        paused_text_rect = paused_text.get_rect(center=(width // 2, height // 2))
        screen.blit(paused_text, paused_text_rect)

    # Update the display
    pygame.display.update()

pygame.quit()
