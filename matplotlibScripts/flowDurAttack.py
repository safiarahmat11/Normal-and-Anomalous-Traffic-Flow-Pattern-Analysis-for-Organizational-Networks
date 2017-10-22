import numpy as np
import collections
import matplotlib.pyplot as plt
import itertools



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
	
	sorted_data = np.sort(data)
	for x in sorted_data:
		packets.append(int(x))
	print("Sorted array:")
	
	print(packets)	
	counter = collections.Counter(packets)
	print("frequency of each packet " )
	#print(counter.values())
	frequency = list(counter.values())
	
	xxx =np.sort(list(counter.keys()))
	
	print("xvalues: kaeys")
	print(xxx)
	for i in range(1663):
		#print(xxx[i])
		xFinal.append(xxx[i])
	xFinal1=xFinal[0::30]
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
	for i in range(1663):
		yFinal.append(xvalue[i])
	yFinal1=yFinal[0::30]
	#print(yFinal)
	#for w in packets:
		#freq.append(packets.count(w))
	#print(freq)


	xvalues = np.array(xvalue)

	plt.plot(xFinal1,yFinal1,label= leg,marker=mark)
	plt.legend(loc='lower right')

#-----
#data = np.loadtxt('demo.txt', usecols=(1,), delimiter=',')
#cdfPlot(data,'Home Network')	
#marker = itertools.cycle((',', '+', '.', 'o', '*')) 
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
#data = np.loadtxt('D:/Datasets/Normal/Reduced/nflstathwn.txt', usecols=(1,), delimiter=',')
#data1 = np.loadtxt('D:/Datasets/Normal/ISCX/nflstathwn.txt', usecols=(1,), delimiter=',')
#data2 = np.loadtxt('D:/Datasets/Normal/UNIBS/nflstatunibs.txt', usecols=(1,), delimiter=',')
#data3 = np.loadtxt('D:/Datasets/Attack/ISCX/aflstathwn.txt', usecols=(1,), delimiter=',')
data4 = np.loadtxt('D:/Datasets/Attack/CAIDA/aflstathwn.txt', usecols=(1,), delimiter=',')
'''data6 = np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/aflstathwn.txt', usecols=(1,), delimiter=',')
data7 = np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/aflstathwn.txt', usecols=(1,), delimiter=',')
data8 = np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/aflstathwn.txt', usecols=(1,), delimiter=',')
data9 = np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/aflstathwn.txt', usecols=(1,), delimiter=',')'''
#cdfPlot(data,'Home Network',mark)
#cdfPlot(data1, 'ISCX Normal',mark1)
#cdfPlot(data2,'UNIBS',mark2)
#cdfPlot(data3,'ISCX Attack',mark3)
cdfPlot(data4,'CAIDA',mark6)
'''cdfPlot(data6,'ISCX DDoS Botnet',mark6)
cdfPlot(data7,'ISCX HTTP DDoS',mark7)
cdfPlot(data8,'ISCX Infiltration from inside',mark8)
cdfPlot(data9,'ISCX Brute Force',mark)'''
#plt.title('CDF for Flow Duration Of Attack Datasets')
ax.set_yticks([0.0,0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xticks([500, 1000, 1500, 2000,2500, 3000])
plt.xlabel('Flow Duration (s)')
plt.ylabel('CDF')
plt.show()