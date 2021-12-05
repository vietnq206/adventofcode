import math 

from os import truncate


def split(word):
    return list(word)



def part1():
    set = list()
    deepth = 0
    trigger = True
    with open('data.dat') as file:
        for line in file:
            data = split(line)
            deepth = deepth + 1
            if trigger:
                for i in range(0,len(data)-1):
                    set.append(0)
                trigger = False    
            for i in range(0,len(set)):
                if int(data[i]) == 0:
                    set[i] = set[i] + 1
        
        gamma = 0
        epsilon = 0
        
        for i in range(0,len(set)):   
            if set[i] < deepth/2:
                gamma = gamma + math.pow(2,len(set)-i-1)
            else:
                epsilon = epsilon + math.pow(2,len(set)-i-1)
    
    return gamma*epsilon

def splitSet(setIn,pos):
    if len(setIn) == 1:
        return [setIn,setIn]
    out0 = list()
    out1 = list()
    for data in setIn:
        if int(data[pos]) == 0 :
            out0.append(data)
        else:
            out1.append(data)

    if(len(out0) > len(out1)):
        return [out0,out1]
    else :
        return [out1,out0]


def part2():
    set = list()
    deepth = 0

    with open('data.dat') as file:
        for line in file:
            line = line.replace("\n", "")
            data = split( line )
            set.append(data)
    
    oxy = 0
    co2 = 0
    setBig = set
    setSmall = set
    for i in range(0,len(set[0])):
        [setBig, _] = splitSet(setBig,i)
        oxy = oxy + int(setBig[0][i])*math.pow(2,len(set[0])-i-1)

        [_,setSmall] = splitSet(setSmall,i)
        co2 = co2 + int(setSmall[0][i])*math.pow(2,len(set[0])-i-1)  
  
    
    print(oxy*co2)



def main():
    print(part2())

if __name__ == "__main__":
    main()