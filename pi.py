import math

def area(r,n):
  a = 2*r*math.sin(math.radians(180/n))
  return n*a*a/(4*math.tan(math.radians(180/n)))

if __name__ == "__main__":
  Rad = 1
  for i in range(3,1000000):
    r = area(Rad,i)/(Rad*Rad)
    print(r)
