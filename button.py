import pygame

pygame.init()

# Function to extract the song name from the file path
def get_song_name(song):
    song = song.split("/")[-1]  # Get the file name
    song = song.split(".")[0]   # Remove the file extension
    return song



# Button class to create and manage buttons
class Button():
    def __init__(self, x, y, width, height, song):
        self.rect = pygame.Rect(x, y, width, height)  # Button rectangle
        self.song = pygame.mixer.Sound(song)  # Load the specific song for this button
        self.text = get_song_name(song)  # Button text
        size = 25 - (len(self.text) // 10)  # Adjust font size based on text length
        self.font = pygame.font.Font(None, size)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))  # Render text
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)  # Center text in button

        

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)  # Draw button rectangle
        screen.blit(self.text_surf, self.text_rect)  # Draw button text

    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):  # Check if button is clicked
            pygame.mixer.stop()  # Pause any currently playing song
            self.song.play()  # Play the button's song
            return True
        return False
    
