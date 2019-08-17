import functools
import operator

def count(num):
    cnt = 0
    s = str(num)
    while(len(s)>1):
        cnt += 1
        array = list(map(int, s))
        s = functools.reduce(operator.mul, array)
        s = str(s)
    return cnt

def sorted(num):
    s = str(num)
    for n in range(0,len(s)-1):
        if s[n]>s[n+1]:
            return False
    return True

if __name__ == '__main__':
    lst = [10,25] #乗算回数と自然数のまとめリスト
    num = 1 #調べる自然数
    counter = 2 #現在の最大乗算回数
    tmp = 0 #調べた自然数の乗算回数
    while(1):
        if  (not '0' in str(num)) and (not '1' in str(num)) and ((not '5' in str(num)) or ('5' in str(num) and (not '2' in str(num) and not '4' in str(num) and not '6' in str(num) and not '8' in str(num)))) and (sorted(num)):
            print(str(num)+'を調べています        ',end='')
            for n in range(0,len(lst)):
                print(str(n+1)+'回：'+str(lst[n])+' ',end='')
            print('')
            tmp = count(num)
            if(tmp>counter):
                counter = tmp
                lst.append(num)
        num += 1
