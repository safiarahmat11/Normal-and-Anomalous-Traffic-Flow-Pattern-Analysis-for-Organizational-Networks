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
	for i in range(100):
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
	for i in range(100):
		yFinal.append(xvalue[i])
	#print(yFinal)
	#for w in packets:
		#freq.append(packets.count(w))
	#print(freq)


	xvalues = np.array(xvalue)

	plt.plot(xFinal,yFinal,label= leg,linestyle=':', marker=mark)
	plt.legend(loc='lower right')

#-----
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
data = np.loadtxt('D:/Datasets/Normal/Reduced/ndsthwn.txt', usecols=(0,), delimiter=',')
data1 = np.loadtxt('D:/Datasets/Normal/ISCX/ndstiscx.txt', usecols=(0,), delimiter=',')
data2 = np.loadtxt('D:/Datasets/Normal/UNIBS/ndstunibs.txt', usecols=(0,), delimiter=',')
#data3 = np.loadtxt('D:/Datasets/Attack/ISCX/adstiscx.txt', usecols=(0,), delimiter=',')
#data4 = np.loadtxt('D:/Datasets/Attack/CAIDA/aflstathwn.txt', usecols=(0,), delimiter=',')
cdfPlot(data,'Home Network',mark)
cdfPlot(data1, 'ISCX Normal',mark1)
cdfPlot(data2,'UNIBS', mark2)
#cdfPlot(data3,'ISCX Attack')
#cdfPlot(data4,'CAIDA')
#plt.title('CDF for Number of Flows')
ax.set_yticks([0.0,0.2, 0.4, 0.6, 0.8, 1.0])
ax.set_xticks([  20, 40, 60,80, 100])
plt.xlabel('Number of Flows')
plt.ylabel('CDF')
plt.show()