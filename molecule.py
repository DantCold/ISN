﻿# Créé par Pierre, le 07/03/2016 en Python 3.2
import pygame
pygame.init()
from PIL import Image
from atome import *
from jeu import Jeu
from pattern import *



class Molecule:
    """La classe Molécule, qui est un ensemble d'atomes."""

    def __init__(self, atome, posX, posY):
        self.addAtome(atome)
        self.posX = posX
        self.posY = posY
        self.isAlive = True
        #self.mv_x = 0
        #self.mv_y = 0


    def __init__(self,nomMol,hauteur,largeur,pattern):
        self.atomeList = listerAtomes(nomMol,hauteur,largeur) #La liste qui contient tous les atomes.
        #self.isAlive = true #Booléen qui rend compte de l'état de la molécule.  #Pour l'instant je l'ai viré parce qu'il faisait une erreur
        self.hpMax = vieMol(self.atomeList) #La vie maximale de la molécule, somme de ceux des atomes.
        self.hp = 0 #La vie de la molécule.
        self.posX = 0
        self.posY = 0
        #self.mv_y = 0
        #self.mv_x = 0   #les variables de mouvements.
        self.img = pygame.image.load('resources/photos/'+str(nomMol)).convert_alpha()
        self.rect = self.img.get_rect()
        self.pattern=pattern
        self.hauteur=hauteur
        self.largeur=largeur
        self.dead=False


    """def addAtome(atome,pos):
        self.atomeList.append(atome)
        self.hpMax += atome.hp
        self.hp = self.hpMax
        self.pos = pos"""

    def move(self):
        """self.posX += self.mv_x
        self.posY += self.mv_y
        self.rect = self.rect.move(self.mv_x, self.mv_y)"""
        self.posX, self.posY = self.pattern.deplacer(self.posX, self.posY)
        self.rect.x = self.posX
        self.rect.y = self.posY
        #TODO: ici, prendre la décision de tirer ou non.
        if self.posX+self.largeur<-5 or self.posX>355 or self.posY+self.hauteur<-5 or self.posY>768+5:     #changer valeur ici aussi
            self.dead=True   #pas besoin de passer par hit, il n'y aura pas d'animation comme c'est hors de l'écran

        if self.__name__()=="moleculeJoueur":  #condition qui regarde si le joueur ne dépasse pas les limites de l'entendement
            if self.posX<10:
                self.posX=10
            elif self.posX>340:  #changer encore ici
                self.posX=340
            if self.posY <10:
                self.posY=10
            elif self.posY>758:
                self.posY=758

    def tirer(self):
        projectiles = []
        for atome in self.atomeList:
            if atome.delayTir<0:
                projectiles+=(atome.tir())
            else:
                atome.delayTir-=1
        return projectiles

    def hit(self):
        self.hp -= 1
        if hp <= 0:
            print("Aaaaaaaaaah ! Je meurs !")
            self.dead=True


def listerAtomes( nomMol,hauteur,largeur):
        img = Image.open(nomMol)
        listeAtomes=[]
        for y in range(hauteur):
            for x in range(largeur):

                pixel = img.getpixel((x,y))

                if pixel==(0,1,0,255) :
                    listeAtomes.append(Carbone(x,y))
                elif pixel == (0,0,1,255):
                    listeAtomes.append(Hydrogene(x,y))
                elif pixel == (1,0,0,255):
                    listeAtomes.append(Oxygene(x,y))
                elif pixel == (0,1,1,255):
                    listeAtomes.append(Azote(x,y))
        return listeAtomes
    #pour tester pour l'instant vous pouvez faire la commande CH4=Molecule('CH4.png')puis print(CH4.atomeList) dans la console


def vieMol(atomeList):
    vie =0
    for a in atomeList :
        vie+=a.hp
    return vie


"""
Marre que ce code là soit exécuté tout le temps.
Cortizone=Molecule('resources/photos/cortizone.png',500,500)
print(Cortizone.atomeList)
print(Cortizone.hpMax," est la vie max de la cortizone")"""