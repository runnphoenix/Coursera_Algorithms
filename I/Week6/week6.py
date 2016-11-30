from multiprocessing import Pool
import os

dic = {}
#result = 0

for number in open("/Users/workMac/Desktop/2sum.txt"):
    number.strip()
    dic.update({int(number): number})

def runn(a,b):
    print('process:',os.getpid())
    result = 0
    for t in range(a, b+1):
        for num in dic:
            if t-num in dic:
                if num != t-num:
                    result += 1
                    break
    print(result)


if __name__ == '__main__':

    p = Pool(4)
    p.apply_async(runn, args=(-10000,-7500),)
    p.apply_async(runn, args=(-7499,-5000),)
    p.apply_async(runn, args=(-4999,-2500),)
    p.apply_async(runn, args=(-2499,0),)
    p.apply_async(runn, args=(1,2500),)
    p.apply_async(runn, args=(2501,5000),)
    p.apply_async(runn, args=(5001,7500),)
    p.apply_async(runn, args=(7501,10001),)

    p.close()
    p.join()

#print(result)
