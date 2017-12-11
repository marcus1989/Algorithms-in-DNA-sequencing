# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'ATTGGC'
v = 'GCCTTA'
seq = 'ACGT'
e = ''
seq1 = 'CCGG'
seq2 = 'AATT'
seq3 = ['A','C','G', 'T']
import random
#random.seed(1)
#out = random.choice('ACGT')
seq = ''
for _ in range(10):
    seq += random.choice('ACGT')

seq1 = ''.join([random.choice('AGCT') for _ in range(10)])

def longestCommonPrefix(s1, s2):
    i = 0    
    while i < len(s1) and i < len(s2) and s1[i]==s2[i]:
        i += 1
    return s1[:i]

def match(s1, s2):
    
    if not len(s1) == len(s2):
        return False
     
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            return False

    return True
    
def reverseCompliment(s):
    compliment = {'A':'T','G':'C','T':'A','C':'G'}
    t = ''
    for base in s:
        t = compliment[base] + t
    return t


def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

import collections
collections.Counter(genome)


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
            q = PhredtoQ(phred)
            hist[q] +=1
    return hist
                

import matplotlib.pyplot as plt
plt.bar(range(len(h)),h)
plt.show()            
    

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

import collections
count = collections.Counter()    
for seq in seqs:
    count.update(seq)
    
    
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
    
import random
def generateReads(genome, numReads, readLen):
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome) - readLen) - 1
        reads.append(genome[start:start+readLen])
    return reads