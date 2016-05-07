﻿# Créé par Pierre, le 28/02/2016 en Python 3.2

import pygame
import time
import jeu as Jeu
from replay import ReplayLoaded

class Fenetre:
    """Classe Fenêtre, s'occupant de l'affichage."""

    def __init__(self, titre, largeur, hauteur):
        self.fen = pygame.display.set_mode((largeur, hauteur))
        self.largeur = largeur
        self.hauteur = hauteur
        self.font = pygame.font.Font(None, 30)
        #self.imgList = []
        self.entites = [] #une liste qui contient des listes comme ça : [image, tuple_de_position]
        #self.fond = fond
        pygame.display.set_caption(titre)
        self.explosions = [] #La liste des explosions: [ [ImageExplosion, ListeDeTuplesDePositions] ]
        #self.imgList.append(image.load("hakase_nyan.png").convert_alpha())
        #self.fenetre.blit(fond, (0, 0))
        self.clock = pygame.time.Clock()

    def __del__(self):
        """Possible qu'on n'ait pas à se servir de cette fonction, mais je l'ai créée quand même au cas où."""
        pygame.quit()


    """def addImgList(self, img, pos):
        lis = [img , pos]
        self.imgList.append(lis)"""


    def rafraichir(self):
        #print(self.imgList)
        """for lis in self.imgList:
            self.fen.blit(lis[0], lis[1])"""
        self.fen.blit(self.fond, (0,0))
        for ent in self.entites:
            self.fen.blit(ent.img, (ent.posX, ent.posY))
            #self.fen.fill((255,0,0),ent.rect)    #montre les hitboxs
        for exp in self.explosions:
            #print("On affiche des explosions !")
            for pos in exp[1]:
                self.fen.blit(exp[0], pos)
                #print("Il y a une explosion à :", pos)
        self.clock.tick(60)
        self.fen.blit(self.font.render(str(self.clock.get_fps()), 1, (180, 180, 255)), (0, 0))
        pygame.display.flip()
        self.entites = []
        self.explosions = []

    def dessinerCadre(self, posX, posY, hauteur, largeur):
        pygame.draw.rect(self.fen, pygame.Color(255, 255, 255, 0), pygame.Rect(posX, posY, largeur, hauteur))

    def ecrireTexte(self, texte, posX, posY):
        """Attention, le texte doit être affiché en dernier, car il faut le flip() 'manuellement'."""
        surface = self.font.render(texte, 0, pygame.Color(255, 0, 0, 0))
        self.fen.blit(surface, (posX, posY))
        pygame.display.flip()

    def fermer(self):
        pygame.quit()

    def afficherPause(self):
        sombre = pygame.Surface((self.largeur, self.hauteur))
        sombre.set_alpha(128)
        sombre.fill((0, 0, 0))
        font = pygame.font.Font(None, 40)
        font2 = pygame.font.Font(None, 20)
        font2.set_italic(True)
        surface = font.render("Pause", 0, pygame.Color(255, 255, 255, 0))
        surface2 = font2.render("Appuyez sur ECHAP pour continuer.", 0, pygame.Color(255, 255, 255, 0))
        self.fen.blit(sombre, (0,0))
        self.fen.blit(surface, ((self.largeur/2)-60, (self.hauteur/2)-40))
        self.fen.blit(surface2, (0, 20))
        pygame.display.flip()

    def playReplay(self,nom):
        replay = ReplayLoaded(nom)
        for a in replay.listeFrames:
            image = pygame.image.frombuffer(a,replay.taille,"RGB")
            self.fen.blit(image, (0,0))
            pygame.display.flip()
            time.sleep(1/60)

"""if __name__ == "__main__":
    f = Fenetre("test", 768, 600)
    f.fond = pygame.image.load("resources/hakase_nyan.png").convert_alpha()
    #f.addImgList(pygame.image.load("hakase_nyan.png").convert_alpha(), (0, 0))
    #f.dessinerCadre(0, 50, 100, 300)
    f.rafraichir()
    #f.ecrireTexte("lel", 500, 200)
    time.sleep(2)
    f.fermer()"""
