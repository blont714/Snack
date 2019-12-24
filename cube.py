import random

def cube_root(x):
    #許容誤差
    eps = 0.0001
    #初期の始端、終端を設定　求めたい値(xの三乗根)solは1<=sol<=(x+2)/3の範囲にある
    front = 1
    end = (x+2)/3
    #始端もしくは終端を修正して、範囲を狭めていく。
    for i in range(10):
        #誤差許容を越えていれば始端を返す
        if(abs(x-front**3)>eps):
            #始端と終端を結ぶ線分を三分割し、solがどの範囲にあるか調べる。
            #例えば 始端+(終端-始端)/3 > sol
            #すなわち (始端+(終端-始端)/3)**3 > x
            #であるなら、終端のみを修正すれば良い

            if (front+(end-front)/3)**3 > x:
                end = (front+(end-front)/3)
                if i==9:
                    return end
            elif (front+2*(end-front)/3)**3 > x:
                front = (front+(end-front)/3)
                end = (front+2*(end-front)/3)
                if i==9:
                    return end
            else:
                front = (front+2*(end-front)/3)
                if i==9:
                    return front
        else:
            return front

#検証用

if __name__ == '__main__':
    x = random.randint(1, 10)
    sol = cube_root(x)
    print(x, sol)

    #検証用
    for i in range(1,11):
        sol = cube_root(i)
        sol_cube = sol**3
        print('与えられた実数:',str(i).rjust(2),' 求めた近似解:',str(sol).rjust(18),' 近似誤差:', str(abs(i-sol_cube)).rjust(22))
