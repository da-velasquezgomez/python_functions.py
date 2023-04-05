def max_num(a, b, c):
  if a >= b and a>= c:
        return a
  elif b >= a and b>= c:
        return b
  else: 
        return c

print(max_num(1,2,3))


import numpy
def mult_list(list):
  return numpy.prod(list)
list = [2,4,6,8]
print(mult_list(list))



def rev_string(a):
    return a[::-1]

a = ('My back hurts')

print(rev_string(a))



def num_within(n):
    if n in range(2,3,6):
        print(True)
    else :
        print(False)
        
print(num_within(2))
print(num_within(10))




def pascal(n):
  for i in range(n):
    print(' '*(n-1), end='')
    print(' '.join(map(str, str(11**i))))


print(pascal(6))