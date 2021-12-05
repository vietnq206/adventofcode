


def main():
    data = list()
    horizontal = 0
    deepth = 0
    aim = 0
    with open('data.dat') as file:
        for line in file:
            data = line.split()
            if data[0] == "forward":
                horizontal = horizontal + int(data[1])
                aim = aim + int(data[1])*deepth
 
            elif data[0] == "down":
                deepth = deepth + int(data[1])
            else :
             
                deepth = deepth - int(data[1])
    print(aim*horizontal)            

if __name__ == "__main__":
    main()