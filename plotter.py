import matplotlib.pyplot as plt
import sys
import csv

if __name__ == '__main__':
    filename=sys.argv[1]
    
    
    with open(filename, mode="r") as file:
        reader=csv.reader(file)
        
        for pair in reader:
            try:
                plt.plot(int(pair[0]),int(pair[1]),'bo')
                print
            except ValueError:
                print('The first line is ignored')
                     
            
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
