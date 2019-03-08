import matplotlib.pyplot as plt
import random as r
import math as m
import statistics

def ytFunction(f1, f2, t, nois):
    return m.sin(2*m.pi*f1*t) + m.sin(2*m.pi*f2*t) + nois

def meanFilter(list_value, m_value, outputx, outputy, lens):
    count = 0
    for i in range(0,(lens-m_value)):
        slice_output = list_value[i:(m_value+i)]
        mean = statistics.mean(slice_output)
        outputy.append(mean)
        outputx.append(count*0.01)  
        print(mean)
        count = count + 1

def showOriginal():
    plt.figure(1)
    plt.subplot(311)

    plt.plot(outputx1,outputy1)

    plt.subplot(312)
    plt.plot(outputx2,outputy2)

    plt.subplot(313)
    plt.plot(outputx3,outputy3)

    plt.show()

def showFilterOutput():
    plt.figure(1)
    plt.subplot(311)
    plt.title("m = 100")

    plt.plot(outputx_filter1,outputy_filter1)

    plt.subplot(312)
    plt.title("m = 100")
    plt.plot(outputx_filter2,outputy_filter2)

    plt.subplot(313)
    #plt.plot(outputx,outputy)
    plt.title("m = 100")
    plt.plot(outputx_filter3,outputy_filter3)

    plt.show()

fs = 1000
t_sampling = 1/fs
f_input = [5,2,7,10]
alphas = [0.1,0.3,0.5]
mi = [1,5,10,100]

outputy1 = []
outputx1 = []
outputy2 = []
outputx2 = []
outputy3 = []
outputx3 = []


for i in range(0,1000):
    nois = (2*r.randint(0,2)-2) *alphas[0]
    outputy1.append(ytFunction(f_input[0],f_input[1],(i*t_sampling),nois))
    outputx1.append(i*t_sampling)

for i in range(0,1000):
    nois = (2*r.randint(0,2)-2) *alphas[1]
    outputy2.append(ytFunction(f_input[0],f_input[2],(i*t_sampling),nois))
    outputx2.append(i*t_sampling)

for i in range(0,1000):
    nois = (2*r.randint(0,2)-2) *alphas[2]
    outputy3.append(ytFunction(f_input[0],f_input[3],(i*t_sampling),nois))
    outputx3.append(i*t_sampling)

# Orinal sampling

showOriginal()
    


outputy_filter1 = []
outputx_filter1 = []

outputy_filter2 = []
outputx_filter2 = []

outputy_filter3 = []
outputx_filter3 = []

# average filter 
leng1 = len(outputy1)
leng2 = len(outputy2)
leng3 = len(outputy3)
meanFilter(outputy1,mi[3], outputx_filter1,outputy_filter1, leng1)
meanFilter(outputy2,mi[3], outputx_filter2,outputy_filter2, leng2)
meanFilter(outputy3,mi[3], outputx_filter3,outputy_filter3, leng3)

showFilterOutput()


'''
series_output = []

fs = 1000
pi = 3.142
tsame = 1/fs
t = []
nf = m.ceil(4*m.pi)
for i in range(0, nf):
    t.append(i*tsame)

ft = 0

bn_list = []
f_output = []


for n in range(0,10000):
  bn = 20/(m.pi*(2*n-1))
  bn_list.append(bn)
  partial_sum = 0
  for t in t:
    ft = bn*m.sin((2*n-1)*t) + ft
    partial_sum = partial_sum + ft
  series_output.append(partial_sum)


for i in range(1, len(bn_list)):
    f_output.append(i/(2*m.pi))



plt.figure(1)
plt.subplot(311)
plt.plot(t,series_output)
'''