import numpy as np
import collections
import matplotlib.pyplot as plt

def listRet(a,b,c):

	final = a + b + c
	return final 

def cdfPlot (data, leg, mark):

	packets = []
	freq =[]

	count = 1
	cdf = 0
	xvalue = []
	cfreq = []
	xFinal = []
	yFinal = []
	xFinal1 = []
	yFinal1 = []
	print(len(data))
	#print(data)
	sorted_data = np.sort(data)
	for x in sorted_data:
		packets.append(int(x))
	print("Sorted array:")
	
	#print(packets)	
	counter = collections.Counter(packets)
	print("frequency of each packet " )
	#print(counter.values())
	frequency = list(counter.values())
	
	xxx =np.sort(list(counter.keys()))
	
	print("xvalues: kaeys")
	#print(xxx)
	for i in range(1400):
		#print(xxx[i])
		
		xFinal.append(xxx[i])
	xFinal1 = xFinal[0::50]	
	print(xFinal)
	#print(xxx)

	print("frequency of each packet " )
	#print(frequency)
	for i in range(len(frequency)):
		if i == 0:
			#print(i)
			cfreq.append(frequency[0])
		else:
			cfreq.append(cfreq[i-1] + frequency[i])
	print("cumulative frequency:")
	#print(cfreq)

	print("total sum " )
	#print(sum(counter.values()))
	total = sum(counter.values())
	for i in range(len(cfreq)):
		cdf = float(cfreq[i])/float(total)
		xvalue.append(float(cdf))
	print("cdf values ")
	#print(xvalue)
	for i in range(1400):
		
		yFinal.append(xvalue[i])
	yFinal1 = yFinal[0::50]	
	#print(yFinal)
	#for w in packets:
		#freq.append(packets.count(w))
	#print(freq)


	xvalues = np.array(xvalue)

	plt.plot(xFinal1,yFinal1,label= leg, marker=mark, linestyle=':')
	plt.legend(loc='lower right')

#-----
'''
c = list(np.loadtxt('demo.txt', usecols=(1,), delimiter=','))
print(len(c))
c1 = list(np.loadtxt('demo1.txt', usecols=(1,), delimiter=','))
c2 = list(np.loadtxt('demo2.txt', usecols=(1,), delimiter=','))
data = listRet(c,c1,c2)
cdfPlot(data,'Home Network')
'''
#data = np.loadtxt('demo.txt', usecols=(1,), delimiter=',')
#cdfPlot(data,'Home Network')	
fig, ax = plt.subplots()
mark = '.'
mark1 = '+'
mark2 = 's'
mark3 = 'o'
mark4 = '*'
mark5 = '^'
mark6 = 'd'
mark7 = '<'
mark8='v'


c = list(np.loadtxt('D:/Datasets/Normal/Reduced/icmpstat.txt', usecols=(4,), delimiter=','))
c1 = list(np.loadtxt('D:/Datasets/Normal/Reduced/tcpstat.txt', usecols=(4,), delimiter=','))
c2 = list(np.loadtxt('D:/Datasets/Normal/Reduced/udpstat.txt', usecols=(4,), delimiter=','))
data = listRet(c,c1,c2)

b = list(np.loadtxt('D:/Datasets/Normal/ISCX/icmpstat.txt', usecols=(4,), delimiter=','))
b1 = list(np.loadtxt('D:/Datasets/Normal/ISCX/tcpstat.txt', usecols=(4,), delimiter=','))
b2 = list(np.loadtxt('D:/Datasets/Normal/ISCX/udpstat.txt', usecols=(4,), delimiter=','))
data1 = listRet(b,b1,b2)

a = list(np.loadtxt('D:/Datasets/Normal/UNIBS/icmpstat.txt', usecols=(4,), delimiter=','))
a1 = list(np.loadtxt('D:/Datasets/Normal/UNIBS/tcpstat.txt', usecols=(4,), delimiter=','))
a2 = list(np.loadtxt('D:/Datasets/Normal/UNIBS/udpstat.txt', usecols=(4,), delimiter=','))
data2 = listRet(a,a1,a2)


#data = np.loadtxt('D:/Datasets/Normal/Reduced/ndsthwn.txt', usecols=(0,), delimiter=',')
#data1 = np.loadtxt('D:/Datasets/Normal/ISCX/ndstiscx.txt', usecols=(0,), delimiter=',')
#data2 = np.loadtxt('D:/Datasets/Normal/UNIBS/ndstunibs.txt', usecols=(0,), delimiter=',')
#data3 = np.loadtxt('D:/Datasets/Attack/ISCX/adstiscx.txt', usecols=(0,), delimiter=',')
#data4 = np.loadtxt('D:/Datasets/Attack/CAIDA/aflstathwn.txt', usecols=(0,), delimiter=',')
cdfPlot(data,'Home Network', mark)
cdfPlot(data1, 'ISCX Normal', mark3)
cdfPlot(data2,'UNIBS', mark4)

ax.set_yticks([0.0,0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xticks([ 200, 400, 600, 800, 1000,1200,1400])
#plt.title('CDF for packet bytes')
plt.xlabel('Packet Size in Bytes')
plt.ylabel('CDF')
plt.show()