import pygame
import random
import Sp_class
"""Creation of sprites. This modul is used in every levels in the game.
Functions include creation of meteors of smaller and bigger sizes, crystals and weapons,
adding the said sprites to their groups""" 
def Create_MM_1(size, group):
    """creates bigger meteor for the manual level, adds it to appropriate sprites group"""
    block = Sp_class.Meteor_1()
    block.rect.x = size[0]//2
    block.rect.y = random.randrange(-30,0)
    group.add(block)
def Create_MM_2(size, group):
    """creates smaller meteor for the manual level, adds it to appropriate sprites group"""
    block2 = Sp_class.Meteor_2()
    block2.rect.x = size[0]//2
    block2.rect.y = random.randrange(-30,0)
    group.add(block2)
def Create_M_1(size, group1, group2, group3):
    """creates bigger meteor for the gaming levels, adds it to appropriate sprites groups"""
    block = Sp_class.Meteor_1()
    block.rect.x = random.randrange(size[0]-60)
    block.rect.y = random.randrange(-1030,0)
    group1.add(block)
    group2.add(block)
    group3.add(block)
def Create_M_2(size, group1, group2, group3):
    """creates smaller meteor for the gaming levels, adds it to appropriate sprites groups"""
    block2 = Sp_class.Meteor_2()
    block2.rect.x = random.randrange(size[0]-40)
    block2.rect.y = random.randrange(-730,0)
    group1.add(block2)
    group2.add(block2)
    group3.add(block2)
def Create_C(size, group):
    """creates crystal for the gaming levels, adds it to appropriate sprites group"""
    crystal = Sp_class.Crystal()
    crystal.rect.x = random.randrange(size[0]-40)
    crystal.rect.y = random.randrange(-730,0)
    group.add(crystal)
