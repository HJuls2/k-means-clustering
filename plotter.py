import matplotlib.pyplot as plt
import sys
import csv
import pandas as pd

if __name__ == '__main__':
    filename=sys.argv[1]

    dataframe = pd.read_csv(filename)
    dataframe.plot(kind='scatter',x='x', y='y')
    plt.show()
    
