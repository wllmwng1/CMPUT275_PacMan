import TileMap
import GameStart
import pygame

class PacMan(pygame.sprite.Sprite):
    def __init__(self, direction, prev_direction, x_value, y_value, lives, image, gameScreen, score):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.prev_direction = prev_direction
        self.x_value = x_value
        self.y_value = y_value
        self.lives = lives
        self.image = image
        self.rect = self.image.get_rect()
        self.score = score
        gameScreen.blit(self.image,(self.x_value,self.y_value))

    def move(self, direction, x, y, TileMap, gameScreen):
        if direction == 'up':
            y = y-1
        elif direction == 'down':
            y = y+1
        elif direction == 'left':
            x = x-1
        elif direction == 'right':
            x = x+1
        if int(x/16) == 0 and int(y/16) == 14 and direction == 'left':
            x = 27*16
        elif int(x/16) == 27 and int(y/16) == 14 and direction == 'right':
            x = 0*16
        fail = True
        if direction == 'up':
            if (int(y/16),int((x/16))) in TileMap.legaltile.keys() and x%16 == 0:
                pygame.draw.circle(gameScreen, (0,0,0), (self.x_value+8,self.y_value+8), 11)
                self.x_value = x
                self.y_value = y
                gameScreen.blit(self.image,(x,y))
                fail = False
        if direction == 'down':
            if (int(y/16)+1,int((x/16))) in TileMap.legaltile.keys() and x%16 == 0 or y%16 == 0:
                pygame.draw.circle(gameScreen, (0,0,0), (self.x_value+8,self.y_value+8), 11)
                self.x_value = x
                self.y_value = y
                gameScreen.blit(self.image,(x,y))
                fail = False
        if direction == 'left':
            if (int(y/16),int((x/16))) in TileMap.legaltile.keys() and y%16 == 0:
                pygame.draw.circle(gameScreen, (0,0,0), (self.x_value+8,self.y_value+8), 11)
                self.x_value = x
                self.y_value = y
                gameScreen.blit(self.image,(x,y))
                fail = False
        if direction == 'right':
            if (int(y/16),int((x/16)+1)) in TileMap.legaltile.keys() and y%16 == 0 or x%16 == 0:
                pygame.draw.circle(gameScreen, (0,0,0), (self.x_value+8,self.y_value+8), 11)
                self.x_value = x
                self.y_value = y
                gameScreen.blit(self.image,(x,y))
                fail = False
        if fail:
            if self.direction != self.prev_direction:
                self.direction = self.prev_direction
                self.move(self.direction, self.x_value, self.y_value, TileMap, gameScreen)

    def eat_dots(self, TileMap):
        (y,x) = (self.y_value, self.x_value)
        if TileMap.legaltile[(int(y/16),int(x/16))].dot == True:
            self.score += 10
            TileMap.legaltile[(int(y/16),int(x/16))].dot = False
            print(self.score)
        if TileMap.legaltile[(int(y/16),int(x/16))].energizer == True:
            print("ENERGIZED")
            TileMap.legaltile[(int(y/16),int(x/16))].energizer = False
            
    def move_input(self, TileMap, gameScreen):
        if pygame.key.get_focused():
            self.prev_direction = self.direction
            if pygame.key.get_pressed()[pygame.K_UP] != 0:
                self.direction = 'up'
            elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
                self.direction = 'down'
            elif pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
                self.direction = 'right'
            elif pygame.key.get_pressed()[pygame.K_LEFT] != 0:
                self.direction = 'left'
            self.move(self.direction, self.x_value, self.y_value, TileMap, gameScreen)
            self.eat_dots(TileMap)
