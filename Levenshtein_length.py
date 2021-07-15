# -*- coding: utf-8 -*-

import csv
import numpy

def LevenshteinDistance(string1, string2):
    distances = numpy.zeros((len(string1) + 1, len(string2) + 1))

    for t1 in range(len(string1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(string2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(string1) + 1):
        for t2 in range(1, len(string2) + 1):
            if (string1[t1-1] == string2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(string1)][len(string2)]

with open('20210103_hundenamen.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if(LevenshteinDistance(row[0],'Luca')==1.0):
            print(row[0]+', ')
        
