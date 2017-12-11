# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:12:01 2016

@author: ambat
"""

#qn1
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

import random

def generateReads(genome, numReads, readLen):
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome) - readLen) - 1
        reads.append(genome[start:start+readLen])
    return reads
    
def naive(p, t):
    occurences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences


def naive_2mm(p, t):
    occurences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        nm = 0
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                nm +=1
                
            if nm >=2:
                match = False
                break
        
        if match:
            occurences.append(i)
    return occurences
    
def reverseCompliment(s):
    compliment = {'A':'T','G':'C','T':'A','C':'G','N':'N'}
    t = ''
    for base in s:
        t = compliment[base] + t
    return t


def readFastq(filename):
    sequences = []
    quality = []
    with open(filename,'r') as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qty = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            quality.append(qty)
    return sequences, quality

def Phred33toQ(qual):
    return ord(qual) - 33
    
def creatHist(quality):
    hist = [0]  * 50
    for qual in quality:
        for phred in qual:
            q = Phred33toQ(phred)
            hist[q] +=1
    return hist
    
def findgcbypos(reads):
    gc = [0] * 100
    totals = [0] * 100
    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1
            totals[i] += 1
    
    for i in range(len(gc)):
        if totals[i] > 0:
            gc[i] /= float(totals[i])
    return gc    
