import pygame
from GameStart import *

class Tile:
    '''
    Tile object: Each tile is 16 x 16 pixel
                legal space tile (tilechar = '1', 'D' or 'E')
                dead space tile (rest of tilechars)

    Input Argument: gameScreen: the gameScreen window from GameStart
                    tilelocation: (i,j) Note: j: tile index in x direction
                                              i: tile index in y direction

    '''
    def __init__(self, tilechar, tilelocation, gameScreen):
        # The char representing the property of the tile
        self.tilechar = tilechar
        # The location of the tile
        self.tilelocation = tilelocation
        # The game screen
        self.gameScreen = gameScreen
        # Tile's dot and energizer indicator, True if there are dot or energizer
        self.dot = False
        self.energizer = False

        if tilechar == '1':
            # A blank legal space tile
            pass
        elif tilechar == 'D':
            # Tile with dot
            self.dot = True
            # Load the dot image on the tile location in pixel
            gameScreen.blit(dotImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == 'E':
            # Tile with energizer
            self.energizer = True
            # Load the energizer image on the tile location in pixel
            gameScreen.blit(energizerImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == '0':
            # A blank dead space tile
            pass
        elif tilechar == 'H':
            # A dead space tile with horizontal blue line
            # Load the horizontal blue line on the tile location in pixel
            gameScreen.blit(horLImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == 'V':
            # A dead space tile with vertical blue line
            # Load the vertical blue line on the tile location in pixel
            gameScreen.blit(verLImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == '2':
            # A dead space tile with a blue bottom right corner
            # Load the blue bottom right corner on the tile location in pixel
            gameScreen.blit(BoRiCImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == '3':
            # A dead space tile with a blue bottom left corner
            # Load the blue bottom left corner on the tile location in pixel
            gameScreen.blit(BoLeCImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == '4':
            # A dead space tile with a blue top right corner
            # Load the blue top right corner on the tile location in pixel
            gameScreen.blit(ToRiCImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == '5':
            # A dead space tile with a blue top left corner
            # Load the blue top left corner on the tile location in pixel
            gameScreen.blit(ToLeCImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == 'P':
            # A dead space tile with the pink line (the door of the ghost house)
            # Load the pink line on the tile location in pixel
            gameScreen.blit(PinkLImg, (tilelocation[1]*TileLen, tilelocation[0]*TileLen))
        elif tilechar == 'G':
            # The tile represent the ghost house
            # The ghosts Blue, Pink and Orange are initial in one of this tile
            # The ghosts can only exit the house, may enter only be eaten by the pacman
            pass
