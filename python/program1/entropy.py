# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 10:26:38 2017

@author: lulu
"""

from math import log
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}#dictionary
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt