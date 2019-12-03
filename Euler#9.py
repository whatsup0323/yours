import time

def isPythagorean(a,b,c):
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        return True
    return False

def isSum(a,b,c,sumVal):
    if (a + b + c) == sumVal:
        return True
    return False

def main(number):
    answer = 0
    done_flag = False
    
    num = int(number)
    for a in range(1,num-1):
        if done_flag: break
        for b in range(a+1,num):
            if done_flag: break
            for c in range(b+1,num+1):
                if done_flag: break
                if isPythagorean(a,b,c) and isSum(a,b,c,num):
                    answer = a * b * c
                    print('a=%d, b=%d, c=%d' %(a,b,c))
                    done_flag = True

    print('The answer is %d' %answer)

number = input('Enter the sum of a,b and c: ')
start = time.time()
main(number)
print("execution time = %s sec" %(time.time() - start))
