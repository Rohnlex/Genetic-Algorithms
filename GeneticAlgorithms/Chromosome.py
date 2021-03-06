#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Chromosome(object): 
    
    # Class Attribute (Constant)
    coef = random.randint(1,230-1)
    
    # Constructor / Instance Attributes
    def __init__(self, large):
        
        # Chromosome's Genes
        self.body = []
        self.large = large
        for _ in range (large):
            self.body.append(str((random.randint(0,1))))
        
        # Initialize Objective Function Punctuation and Fitness
        realValue = self.getRealValue()
        self.objectivePunctuation = self.calcObjPunc(realValue)
        self.fitness = 0;
        # sum = self.getTotObjFunc() + self.objectivePunctuation
        # self.setTotObjFunc(sum)
        # self.fitness = self.calcFitness(self.objectivePunctuation
    
    # Show All Genes of the Chromosome
    def getBody(self):
        return self.body
    
    # Real Number to pass on Objective Function
    def getRealValue(self):
        return int(''.join(self.body),2) # Convert body to String and then to Binary Int
    
    def calcObjPunc(self,realValue):
        return (realValue/self.getCoef())**2
    
    def calcFitness(self,totalObj):
        if totalObj==0: totalObj=1 # Prevent Division by Zero Error
        self.fitness = (self.getObjectivePunctuation()/totalObj) # Update Fitness
        return self.fitness
    
    def copy(self,Chrom,num1,num2):
        pass
    
    def mutate(self):
        pass
    
    
    # Class Methods
    @classmethod
    def getCoef(cls):
        return cls.coef

    @classmethod
    def setCoef(cls,coeficient):
        cls.coef = coeficient
    
    '''
    @classmethod
    def getTotObjPunc(cls):
        return cls.totObjPunc

    @classmethod
    def setTotObjPunc(cls,objPunc):
        cls.totObjPunc = objPunc
    '''
    
    
    # Getters and Setters
    def getLarge(self):
        return self.large
    
    def setLarge(self,large):
        self.large = large
    
    def getObjectivePunctuation(self):
        return self.objectivePunctuation
    
    def setObjectivePunctuation(self,objectivePunctuation):
        self.objectivePunctuation = objectivePunctuation
    
    def getFitness(self):
        return self.fitness
    
    def setFintess(self,fitness):
        self.fitness = fitness
    