
import numpy as np


def part1():
    setVector = list() 
    mapOL = {}
    with open('data.dat') as file:
        for line in file:
            [data1,_,data2] = line.split()
            [X1,Y1] = data1.split(",")
            [X2,Y2] = data2.split(",")
            listTmp = list()
            setVector.append([np.array([int(X1),int(Y1)],dtype=int),np.array([int(X2),int(Y2)],dtype= int)])
            if (X1 == X2):
                if (int(Y1)>int(Y2)):
                    for i in range(int(Y2),int(Y1)+1):
                        if X1+","+str(i) in mapOL.keys():
                            mapOL[X1+","+str(i)] = mapOL[X1+","+str(i)] +1
                        else:
                             mapOL[X1+","+str(i)] = 1
                else:
                    for i in range(int(Y1),int(Y2)+1):
                        if X1+","+str(i) in mapOL.keys():
                            mapOL[X1+","+str(i)] = mapOL[X1+","+str(i)] +1
                        else:
                             mapOL[X1+","+str(i)] = 1             
            elif (Y1 == Y2):
                if (int(X1)>int(X2)):
                    for i in range(int(X2),int(X1)+1):
                        if str(i)+","+Y1 in mapOL.keys():
                            mapOL[str(i)+","+Y1] = mapOL[str(i)+","+Y1] +1
                        else:
                             mapOL[str(i)+","+Y1] = 1
                else:
                    for i in range(int(X1),int(X2)+1):
                        if str(i)+","+Y1 in mapOL.keys():
                            mapOL[str(i)+","+Y1] = mapOL[str(i)+","+Y1] +1
                        else:
                             mapOL[str(i)+","+Y1] = 1                    
    return(len([x for x in mapOL.values() if x > 1]))

def main():
    print(part1())

if __name__ == "__main__":
    main()