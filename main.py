# Import the modules
import pygame
import button
import time
import os

# Initialize Pygame and the mixer module
pygame.init()
pygame.mixer.init()

# List all songs in the "music" directory
songs = os.listdir("music/")


def get_full_filepaths(directory):
    filepaths = []
    for file in os.listdir(directory):
        path = directory+"/"+file
        if os.path.isdir(path):
            filepaths.extend(get_full_filepaths(path))
        else:
            filepaths.append(path)

    return filepaths


# Set up the display window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test game")

# Set up the font and render the title text
font = pygame.font.Font(None, 74)
text = font.render('Song Player', True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (screen.get_width() // 2, 50)

print(get_full_filepaths("music"))

  
# Create a list of buttons for each song
# Create buttons for each song
music = get_full_filepaths("music")
button_list = []

y = 100
x = 50

for song in music:
    button_list.append(button.Button(x, y, 200, 50, song))
    x+= 250
    if x > 600:
        y += 100
        x = 50


def Main():
    # Main game loop
    while True:
        screen.fill((255, 0, 0))  # Fill the screen with red color
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # Quit event
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
                for button in button_list:
                    if button.is_clicked():# Check if any button is clicked 
                        show_song(button.text)
        
        for button in button_list:
            button.draw(screen)  # Draw all buttons

        screen.blit(text, text_rect)  # Draw the title text
        
        pygame.display.update()  # Update the display
        
def show_song(song):
     back = button.Button(250,400, 100, 50, "back.mp3")
     song_percentage = 0
     while True:
        screen.fill((255, 0, 0))  # Fill the screen with red color
        song_percentage = time.time()
        pygame.draw.rect(screen, (150=,150,150), [200, 200, 400, 25], 0, 10)
        pygame.draw.rect(screen, (255,255,255), [200, 200, 400, 25], 0, 10)
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # Quit event
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
                if back.is_clicked():
                    Main()

        font = pygame.font.Font(None, 36)
        text = font.render('Now Playing: '+ song, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen.get_width() // 2, 50)
        
        screen.blit(text, text_rect)  # Draw the title text
        back.draw(screen)
        
        pygame.display.update()  # Update the display 


Main()