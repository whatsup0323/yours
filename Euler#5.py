# Euler#5.py
import time

def getFactorization(number, tmp):
    inputNum = int(number)

    for data in range(2, int(number)+1):
        cnt = 0
        while inputNum % data == 0:
            cnt += 1
            inputNum = inputNum / data
        if tmp[data] < cnt:
            tmp[data] = cnt
        if input == 1:
            break

def main(number):
    answer = 1
    PF = [0 for i in range(int(number) + 1)]

    for data in range(2, int(number)+1):
        getFactorization(data, PF)

    for index, value in enumerate(PF):
        if value > 0:
            answer = answer * pow(index, value)

    print("the smallest number is %d" % answer)


num = input('Enter the number: ')
start_time = time.time()

main(num)

print('Execution time : %f sec' % (time.time() - start_time))
