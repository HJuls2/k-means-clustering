import sys
import csv
import random as rand
from numpy import float64
from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd


def generateClusters(samples, centers, devStd, lowBound, upBound):
    return make_blobs(n_samples=samples,n_features=2,centers=centers, cluster_std=devStd, center_box=(lowBound,upBound), shuffle=True)


def writeOnFile(points, filename):
    pd.DataFrame(points).to_csv(path_or_buf=filename+'.csv', header=['x','y'])

 
if __name__ == '__main__':
    filename = sys.argv[1]
    samples = int(sys.argv[2])
    clusters = int(sys.argv[3])
    devStd = float64(sys.argv[4])
    lowerBound = float64(sys.argv[5])
    upperBound = float64(sys.argv[6])

    points,_ = generateClusters(samples,clusters,devStd, lowBound=lowerBound,upBound=upperBound)
    writeOnFile(points,filename)
    
    
    