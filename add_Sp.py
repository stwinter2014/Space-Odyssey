import pygame
import random
import Sp_class

def Create_M_1(size, group1, group2, group3):
    block = Sp_class.Meteor_1()
    block.rect.x = random.randrange(size[0]-60)
    block.rect.y = random.randrange(-1030,0)
    group1.add(block)
    group2.add(block)
    group3.add(block)
def Create_M_2(size, group1, group2, group3):
    block2 = Sp_class.Meteor_2()
    block2.rect.x = random.randrange(size[0]-40)
    block2.rect.y = random.randrange(-730,0)
    group1.add(block2)
    group2.add(block2)
    group3.add(block2)
def Create_C(size, group):
    crystal = Sp_class.Crystal()
    crystal.rect.x = random.randrange(size[0]-40)
    crystal.rect.y = random.randrange(-730,0)
    group.add(crystal)
