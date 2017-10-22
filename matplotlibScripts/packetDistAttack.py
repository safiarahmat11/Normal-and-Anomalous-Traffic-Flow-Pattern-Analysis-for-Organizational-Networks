import numpy as np
import collections
import matplotlib.pyplot as plt



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
		packets.append(x)
	print("Sorted array:")
	#print(packets)	
	counter = collections.Counter(packets)
	print("frequency of each packet " )
	#print(counter.values())
	frequency = list(counter.values())
	xxx =np.sort(list(counter.keys()))
	print("xvalues: kaeys")
	for i in range(7446):
		#print(xxx[i])
		xFinal.append(xxx[i])
	xFinal1=xFinal[0::200]
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
	print(sum(counter.values()))
	total = sum(counter.values())
	for i in range(len(cfreq)):
		cdf = float(cfreq[i])/float(total)
		xvalue.append(float(cdf))
	print("cdf values ")
	#print(xvalue)
	for i in range(7446):
		yFinal.append(xvalue[i])
	yFinal1=yFinal[0::200]
	#print(yFinal)
	#for w in packets:
		#freq.append(packets.count(w))
	#print(freq)


	xvalues = np.array(xvalue)

	plt.plot(xFinal1,yFinal1,label= leg,marker=mark)
	plt.legend(loc='lower right')

#-----
mark = '.'
mark1 = '+'
mark2 = 's'
mark3 = 'o'
mark4 = '*'
mark5 = '^'
mark6 = 'd'
mark7 = '<'
mark8='v'
fig, ax = plt.subplots()
'''data = np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/aflstathwn.txt', usecols=(0,), delimiter=',')
data1 = np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/aflstathwn.txt', usecols=(0,), delimiter=',')
data2 = np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/aflstathwn.txt', usecols=(0,), delimiter=',')
data3 = np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/aflstathwn.txt', usecols=(0,), delimiter=',')'''
data4 = np.loadtxt('D:/Datasets/Attack/CAIDA/aflstathwn.txt', usecols=(0,), delimiter=',')
'''cdfPlot(data,'ISCX Brute Force', mark)
cdfPlot(data1, 'ISCX DDoS Botnet',mark8)
cdfPlot(data2,'ISCX HTTP DDoS',mark4)
cdfPlot(data3,'ISCX Infiltration from inside',mark2)'''
cdfPlot(data4,'CAIDA',mark3)
#plt.title('CDF for Packet Distribution')
ax.set_yticks([0.0,0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xticks([ 20000,40000, 60000, 80000,100000,120000])
plt.xlabel('Number of packets')
plt.ylabel('CDF')
plt.show()