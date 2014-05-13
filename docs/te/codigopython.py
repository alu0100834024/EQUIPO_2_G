#!/usr/bin/python
#! enconding: utf-8
import math
import time

startubuntu=time.time()
startcpu=time.clock()
def funcionDada(x):
      return math.cos(x) - x

def derivadaFuncionDada(x):
      return -math.sin(x) - 1

i = int(0);

x = float(input("Ingrese el valor de x: "));

tempo = 0;
while(x != tempo and i<100):
     tempo = x
     x = x- funcionDada(x)/derivadaFuncionDada(x)
     e = abs ((x-tempo)/x)

     print("x" + str(i) + "=" + str(x) + "error=" + str(e) + "\n")
     i=i+1

if(i==100):
    print("\n\nNo converge")

else:
    print("\n\nSolucion x: " + str(x))
    
finishubuntu=time.time()
finishcpu=time.clock()
timecpu=finishcpu-startcpu
timeubuntu=finishubuntu-startubuntu
print 'Tiempo Ubuntu:%2.10f \n Tiempo CPU: %2.10f' %(timeubuntu,timecpu)

    
    
    
    
    
   