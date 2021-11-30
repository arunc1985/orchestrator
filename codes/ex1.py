# Program to simulate Fibonacci series
'''
  F0	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12	F13	F14	F15	F16	F17	F18	F19	F20
  0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	987	1597	2584	4181	6765
'''
def fib(n):
    counter=0
    init_fib=[0,1]
    i,j=0,1
    while True:
      if counter==n:
        break;    
      counter+=1
      init_fib.append(init_fib[i]+init_fib[j])
      i+=1;j+=1
    return init_fib

result=fib(20)
print(result)
