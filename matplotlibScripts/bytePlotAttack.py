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
	print(len(data))
	#print(data)
	sorted_data = np.sort(data)
	for x in sorted_data:
		packets.append(int(x))
	print("Sorted array:")
	
	print(packets)	
	counter = collections.Counter(packets)
	print("frequency of each packet " )
	print(counter.values())
	frequency = list(counter.values())
	
	xxx =np.sort(list(counter.keys()))
	
	print("xvalues: kaeys")
	print(xxx)
	for i in range(5):
		#print(xxx[i])
		xFinal.append(xxx[i])
	#print(xFinal)
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
	for i in range(5):
		yFinal.append(xvalue[i])
	#print(yFinal)
	#for w in packets:
		#freq.append(packets.count(w))
	#print(freq)


	xvalues = np.array(xvalue)

	plt.plot(xFinal,yFinal,label= leg,marker=mark)
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


#data = np.loadtxt('demo.txt', usecols=(1,), delimiter=',')
#cdfPlot(data,'Home Network')	
'''c = list(np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/icmpstat.txt', usecols=(4,), delimiter=','))
c1 = list(np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/tcpstat.txt', usecols=(4,), delimiter=','))
c2 = list(np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/udpstat.txt', usecols=(4,), delimiter=','))
data = listRet(c,c1,c2)

b = list(np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/icmpstat.txt', usecols=(4,), delimiter=','))
b1 = list(np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/tcpstat.txt', usecols=(4,), delimiter=','))
b2 = list(np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/udpstat.txt', usecols=(4,), delimiter=','))
data1 = listRet(b,b1,b2)

a = list(np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/icmpstat.txt', usecols=(4,), delimiter=','))
a1 = list(np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/tcpstat.txt', usecols=(4,), delimiter=','))
a2 = list(np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/udpstat.txt', usecols=(4,), delimiter=','))
data2 = listRet(a,a1,a2)

d = list(np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/icmpstat.txt', usecols=(4,), delimiter=','))
d1 = list(np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/tcpstat.txt', usecols=(4,), delimiter=','))
d2 = list(np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/udpstat.txt', usecols=(4,), delimiter=','))
data3 = listRet(d,d1,d2)'''

e = list(np.loadtxt('D:/Datasets/Attack/CAIDA/icmpstat.txt', usecols=(4,), delimiter=','))
e1 = list(np.loadtxt('D:/Datasets/Attack/CAIDA/tcpstat.txt', usecols=(4,), delimiter=','))
e2 = list(np.loadtxt('D:/Datasets/Attack/CAIDA/udpstat.txt', usecols=(4,), delimiter=','))
data4 = listRet(e,e1,e2)
print(data4);
#data = np.loadtxt('D:/Datasets/Normal/Reduced/ndsthwn.txt', usecols=(0,), delimiter=',')
#data1 = np.loadtxt('D:/Datasets/Normal/ISCX/ndstiscx.txt', usecols=(0,), delimiter=',')
#data2 = np.loadtxt('D:/Datasets/Normal/UNIBS/ndstunibs.txt', usecols=(0,), delimiter=',')
#data3 = np.loadtxt('D:/Datasets/Attack/ISCX/adstiscx.txt', usecols=(0,), delimiter=',')
#data4 = np.loadtxt('D:/Datasets/Attack/CAIDA/aflstathwn.txt', usecols=(0,), delimiter=',')
'''cdfPlot(data,'ISCX Brute Force',mark)
cdfPlot(data1, 'ISCX DDoS Botnet',mark2)
cdfPlot(data2,'ISCX HTTP DDoS', mark4)
cdfPlot(data3,'ISCX Infiltration from Inside',mark1)'''
cdfPlot(data4,'CAIDA',mark3)
ax.set_yticks([0.0,0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xticks([40, 50, 60, 70, 80])
#plt.title('CDF for packet bytes')
plt.xlabel('Packet Size in Bytes')
plt.ylabel('CDF')
plt.show()