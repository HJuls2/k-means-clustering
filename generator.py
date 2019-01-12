'''
Created on 11 gen 2019

@author: giulio

'''

import sys
import csv
import random as rand


def generate(num,lowbound,upbound):
    return [(rand.randint(lowbound,upbound),rand.randint(lowbound,upbound)) for n in range(num)]

 
if __name__ == '__main__':
    filename=sys.argv[1]
    args=[int(arg) for arg in sys.argv[2:]]
    dataset=generate(args[0], args[1],args[2])
    
    file=open(filename+".csv", 'w')
    
    with file:
        fields=['x','y']
        writer=csv.DictWriter(file, fields)
        writer.writeheader()
        
        
        for pair in dataset:
            x=pair[0]
            y=pair[1]
            writer.writerow({'x': x,'y':y})
    