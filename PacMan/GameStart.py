import pygame
import TileMap
import pacman

# Load all required images for building the game map
dotImg = pygame.image.load('dot.png')
energizerImg = pygame.image.load('energizer.png')
horLImg = pygame.image.load('horL.png')
verLImg = pygame.image.load('verL.png')
BoRiCImg = pygame.image.load('BoRiC.png')
BoLeCImg = pygame.image.load('BoLeC.png')
ToRiCImg = pygame.image.load('ToRiC.png')
ToLeCImg = pygame.image.load('ToLeC.png')
PinkLImg = pygame.image.load('PinkL.png')
PacManImg = pygame.image.load('PacMan2.png')

# The length of one tile
TileLen = 16

black = (0,0,0)

class GameStart:
    '''
    Start the game
    '''
    def __init__(self):
        pygame.init()

        screen_width = 800
        screen_height = 600

        self.gameScreen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Pac-Man Game')

        self.clock = pygame.time.Clock()

        # background color
        self.gameScreen.fill(black)
        # Build the tile map, pass the game screen to the map
        self.gamemap = TileMap.Tilemap(self.gameScreen)
        self.PacMan = pacman.PacMan('right','right',13*TileLen,23*TileLen,3,PacManImg,self.gameScreen, 0)

    def gameloop(self):
        Exit = False
        while not Exit:
            # Every event that happens
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Hits 'x'
                    Exit = True

            self.PacMan.move_input(self.gamemap,self.gameScreen)
            # Update the whole window
            pygame.display.update()
            # Frame per second
            self.clock.tick(60)


if __name__ == "__main__":
    game = GameStart()
    game.gameloop()
