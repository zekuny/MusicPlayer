import pygame;


class Button():
    
    def __init__(self, name, x, y, image):
        self.name = name;
        self.x = x;
        self.y = y;
        self.image = pygame.image.load(image).convert_alpha();
        
    def draw(self,screen):
        screen.blit(self.image, 
                    (self.x - self.image.get_width(),
                     self.y - self.image.get_height()));
                     
    def isIn(self,pos):
        x = pos[0];
        y = pos[1];
        if abs(self.x-self.image.get_width()/2 - x) < self.image.get_width()/2  \
            and  abs(self.y-self.image.get_height()/2  - y) < self.image.get_height()/2 :
            return True;
        else :
            return False;
