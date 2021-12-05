
import numpy as np
def part1():
    setOrd = list()
    deepth = 0
    setBoard = list(list())
    finalSum = 0
    with open('data.dat') as file:
        line = file.readline().replace("\n", "")
        setOrd = line.split(",")
        file.readline()
        setTmp = list()
        for line in file:
            if (line == "\n"):
                setBoard.append(setTmp)
                setTmp = list()
            else:
                line = line.replace("\n", "")
                setTmp.append(line.split())
        setBoard.append(setTmp)
    
    # checkBoard = [[[0]*len(setBoard[0][0])]*2]*len(setBoard)
    checkBoard = np.zeros((len(setBoard),2,len(setBoard[0][0])),dtype = int)
    # print(checkBoard)
    for numCheck in setOrd:
        # print(numCheck)

        for numBoard in range(0,len(setBoard)):
            for numRow in range(0,len(setBoard[0])):
                for numCol in range(0,len(setBoard[0][0])):
                    if setBoard[numBoard][numRow][numCol] == numCheck:
                        # print([numBoard,numRow,numCol])
                        setBoard[numBoard][numRow][numCol] = -1
                        # print(checkBoard)
                        checkBoard[numBoard][1][numRow] = checkBoard[numBoard][1][numRow] + 1
                        checkBoard[numBoard][0][numCol] = checkBoard[numBoard][0][numCol] + 1
                        # print(checkBoard)
        for i in range(0,len(checkBoard)):
            for j in checkBoard[i]:
                for k in j:
                    if k == len(j):
                        print(i)
                        for row in setBoard[i]:
                            for col in row:
                                if col != -1:
                                    finalSum = finalSum + int(col)
                        return finalSum*int(numCheck)

def part2():
    setOrd = list() 
    setBoard = list(list())
    setWin = set()
    finalSum = 0
    with open('data.dat') as file:
        line = file.readline().replace("\n", "")
        setOrd = line.split(",")
        file.readline()
        setTmp = list()
        for line in file:
            if (line == "\n"):
                setBoard.append(setTmp)
                setTmp = list()
            else:
                line = line.replace("\n", "")
                setTmp.append(line.split())
        setBoard.append(setTmp)
    
    # checkBoard = [[[0]*len(setBoard[0][0])]*2]*len(setBoard)
    checkBoard = np.zeros((len(setBoard),2,len(setBoard[0][0])),dtype = int)
    # print(checkBoard)
    setWin.update([elm for elm in range(0,len(setBoard))])
    for numCheck in setOrd:
        # print(numCheck)

        for numBoard in range(0,len(setBoard)):
            for numRow in range(0,len(setBoard[0])):
                for numCol in range(0,len(setBoard[0][0])):
                    if setBoard[numBoard][numRow][numCol] == numCheck:
                        # print([numBoard,numRow,numCol])
                        setBoard[numBoard][numRow][numCol] = -1
                        # print(checkBoard)
                        checkBoard[numBoard][1][numRow] = checkBoard[numBoard][1][numRow] + 1
                        checkBoard[numBoard][0][numCol] = checkBoard[numBoard][0][numCol] + 1
                        # print(checkBoard)
        for i in range(0,len(checkBoard)):
            for j in checkBoard[i]:
                for k in j:
                    if k == len(j):
                        if(len(setWin) > 1):
                            if i in setWin:
                                setWin.remove(i)
                            # print(setWin)
                        elif i in setWin:
                            # print(i)
                            for row in setBoard[i]:
                                for col in row:
                                    if col != -1:
                                        finalSum = finalSum + int(col)
                            return finalSum*int(numCheck)

def main():
    print(part2())

if __name__ == "__main__":
    main()