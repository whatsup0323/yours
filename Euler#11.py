# Euler#11.py
import time

def checkRight(start_x, start_y, slist):
    result = int(slist[start_x][start_y]) * int(slist[start_x][start_y+1]) * \
             int(slist[start_x][start_y+2]) * int(slist[start_x][start_y+3])
    #print(slist[start_x][start_y], slist[start_x][start_y+1], slist[start_x][start_y+2], slist[start_x][start_y+3], result)
    return result

def checkDown(start_x, start_y, slist):
    result = int(slist[start_x][start_y]) * int(slist[start_x+1][start_y]) * \
             int(slist[start_x+2][start_y]) * int(slist[start_x+3][start_y])
    #print(slist[start_x][start_y], slist[start_x+1][start_y], slist[start_x+2][start_y], slist[start_x+3][start_y], result)
    return result

def checkDiagonally(start_x, start_y, slist, idir):
    if idir == 'left':
        result = int(slist[start_x][start_y]) * int(slist[start_x+1][start_y-1]) * \
                 int(slist[start_x+2][start_y-2]) * int(slist[start_x-3][start_y-3])
        #print(slist[start_x][start_y], slist[start_x+1][start_y-1], slist[start_x+2][start_y-2], slist[start_x+3][start_y-3], result)
    elif idir == 'right':
        result = int(slist[start_x][start_y]) * int(slist[start_x+1][start_y+1]) * \
                 int(slist[start_x+2][start_y+2]) * int(slist[start_x+3][start_y+3])
        #print(slist[start_x][start_y], slist[start_x + 1][start_y+1], slist[start_x + 2][start_y+2], slist[start_x + 3][start_y+3], result)
    else:
        return 0
    return result

def main():
    sLine = list()
    answer_list = []

    f = open("D:/Pjt-PyCharm/sample/sample.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        sLine.append((line.replace('\n', '')).split())
    f.close()

    for x in range(20):
        for y in range(20):
            if x < 17:
                answer_list.append(checkDown(x, y, sLine))
            if y < 17:
                answer_list.append(checkRight(x, y, sLine))
            if x < 17 and y < 17:
                answer_list.append(checkDiagonally(x, y, sLine, 'right'))
            if x < 17 and y > 2:
                answer_list.append(checkDiagonally(x, y, sLine, 'left'))

    #print(sLine)
    #print(len(answer_list), answer_list)
    print('answer is %d' % max(answer_list))


start_time = time.time()

main()

print('Execution time : %f sec' % (time.time() - start_time))
