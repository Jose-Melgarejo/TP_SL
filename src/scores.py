import pygame
from tool import *
from globals import *
class Scores:
    logo = None
    def __init__(self,screen,difficult):
        self.screen = screen
        self.scores = read_scores(difficult)
        if not self.logo:
            self.logo = load_image("logo")
        self.soud_select = load_sound("select")

    def loadNewScore(self,name,score,difficult):
        max_score = 0;
        min_score = 0;
        min_index = -1;
        self.scores = read_scores(difficult)
        i = 0;
        for element in self.scores:
            if (i == 0):
                max_score = element[1];
                min_score = element[1];
            else:
                if (element[1] > max_score):
                    max_score = element[1];
                if (element[1] < min_score):
                    min_score = element[1];
                    min_index = i;
            i+=1;
                    
        if (score > min_score):
            self.scores.append((name,score));
            del self.scores[min_index];
            write_scores(self.scores,difficult);
            self.scores = read_scores(difficult);
            return self.scores, True;
        else:
            return None, False;

    def run(self):
        flag = True
        if Options.sound == True:
            self.soud_select.play()
        while flag:
            self.screen.blit(load_image("background"), self.screen.get_rect())
            colour =  WHITE
            for i in xrange(5):
                scor = self.scores[i]
                title =scor[0]+" "+str(scor[1])
                image = smallfont.render(title,True,colour)
                rect = image.get_rect()
                rect.centerx = self.screen.get_rect().centerx
                rect.top = self.logo.get_height() + i * rect.height * 1.1
                self.screen.blit(image, rect)
            rect = self.logo.get_rect()
            rect.centerx = self.screen.get_rect().centerx
            rect.top = 0
            self.screen.blit(self.logo, rect)
            pygame.display.flip()
            pygame.event.post(pygame.event.wait())
            for event in pygame.event.get():
                if event.type == QUIT:
                    flag = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_RETURN or event.key == K_ESCAPE:
                        flag = False
                        if Options.sound == True:
                            self.soud_select.play()
