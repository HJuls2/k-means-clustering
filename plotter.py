
import matplotlib.pyplot as plt
import sys
import csv

if __name__ == '__main__':
    filename=sys.argv[1]
    
    
    with open(filename, mode="r") as file:
        reader=csv.reader(file)
        
        i=0
        for pair in reader:
            if(i is not 0):
                plt.plot(int(pair[0]),int(pair[1]),'bo')
            
            i=i+1
           
            
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    