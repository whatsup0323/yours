# Euler#6.py
import time


def isPrime(n, prime_list):
    for div in prime_list:
        if n % div == 0:
            #print('%d is not prime' % n)
            return False
    #print('%d is prime' % n)
    return True

def main(n):
    answer = 0
    tmp = 3
    prime_list = [2]

    if int(n) == 1:
        return 2

    while True:
        if isPrime(tmp, prime_list):
            prime_list.append(tmp)
        tmp += 1

        if len(prime_list) == int(n):
            break
    answer = prime_list[-1]

    print(prime_list)
    print('the number of prime = %d' % len(prime_list))
    print('answer is %d' % answer)


number = input('Enter the number: ')
start_time = time.time()

main(number)

print('Execution time : %f sec' % (time.time() - start_time))
