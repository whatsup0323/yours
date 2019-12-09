import time

def getNumofFactor(triNum):
    list_temp = []
    for i in range(1, int(triNum**0.5)+1):
        if triNum % i == 0:
            list_temp.append(i)
            list_temp.append(triNum/i)

    #print('%d has factors:' %triNum, set(list_temp))
    return len(set(list_temp))

def main(number):
    answer = 0
    order = 1
    list_triangle = [1]

    while True:
        nFactor = 0
        temp = list_triangle[order-1]
        order += 1
        list_triangle.append(temp + order)
        nFactor = getNumofFactor(list_triangle[-1])

        if number <= nFactor:
            print('the number of factors (%d) is %d' %(list_triangle[-1], nFactor))
            break    

    answer = list_triangle[-1]
    print('The answer is %d' %answer)

num = input('Enter the number: ')
start = time.time()
main(num)
print("execution time = %s sec" %(time.time() - start))
