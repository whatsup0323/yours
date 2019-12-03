import time

def main(number):
    answer = 0
    num = int(number)
    sLine = []

    f = open("c:/hwasub/sample.txt", 'r')
    while True:
        tmpLine = []
        line = f.readline()
        if not line: break
        tmpLine = list(line)
        if tmpLine[-1] == '\n': del tmpLine[-1]
        sLine = sLine + tmpLine

    for index, data in enumerate(sLine):
        if index > len(sLine) - num:
            break
        else:
            tmp = 1
            tmp_list = []
            for pos in range(index, index + num):
                tmp = tmp * int(sLine[pos])

            if answer < tmp:
                answer = tmp
        
    f.close()
    print('The largest number is %d' %answer)

number = input('Enter the number: ')
start = time.time()
main(number)
print("execution time = %s sec" %(time.time() - start))
