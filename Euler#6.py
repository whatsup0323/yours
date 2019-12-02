# Euler#6.py
import time

def main(n):
    N = int(n)

    sumOfSquare = pow((N * (N + 1)) / 2, 2)
    squareOfSum = (N * (N + 1) * (2 * N + 1)) / 6
    print('sumOfSquare = %d, squareOfSum = %d' %(sumOfSquare, squareOfSum))
    answer = sumOfSquare - squareOfSum

    print("the diff is %d" % answer)


number = input('Enter the number: ')
start_time = time.time()

main(number)

print('Execution time : %f sec' % (time.time() - start_time))
