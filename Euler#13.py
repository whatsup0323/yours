# Euler#13.py
import time


def main(num):
    lines = []
    answer = ''
    sum_val = 0

    f = open("D:/Pjt-PyCharm/sample/sample_Euler#13.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.replace('\n', ''))
    f.close()

    for i in range(len(lines)):
        sum_val = sum_val + int(lines[i])

    sum_str = str(sum_val)
    if int(num) <= len(sum_str):
        for y in range(int(num)):
            answer = answer + sum_str[y]
    else:
        answer = 'None'

    print("answer is %s" %answer)


number = input('Enter first number digits of the sum: ')
start_time = time.time()

main(number)

print('Execution time : %f sec' % (time.time() - start_time))
