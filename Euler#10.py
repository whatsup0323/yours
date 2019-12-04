import time
import math

def isPrime(num, list_prime):
    for data in list_prime:
        if math.sqrt(num) < data: break
        if num %2 == 0: return False
        elif num % data == 0: return False
    return True

def getSum(list_prime):
    sum = 0
    for data in list_prime:
        sum = sum + data
    return sum

def main(number):
    answer = 0
    num = int(number)
    list_prime = [2]

    for i in range(3, num + 1):
        if isPrime(i, list_prime):
            list_prime.append(i)

    answer = getSum(list_prime)
    #print(list_prime)
    print('The answer is %d' %answer)

number = input('Enter the number: ')
start = time.time()
main(number)
print("execution time = %s sec" %(time.time() - start))
