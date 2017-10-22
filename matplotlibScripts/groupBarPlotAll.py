import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1)
ax = fig.add_subplot(111)# 111 denotes 1 row, 1 column, 1 graph
fig.tight_layout()
## the data

N = 4
#--- Total packets Reduced
totalpacketsHN = sum(np.loadtxt('D:/Datasets/Normal/Reduced/nflstathwn.txt', usecols=(0,), delimiter=','))
totalpacketsISCX = sum(np.loadtxt('D:/Datasets/Normal/ISCX/nflstathwn.txt', usecols=(0,), delimiter=','))
totalpacketsUNIBS = sum(np.loadtxt('D:/Datasets/Normal/UNIBS/nflstatunibs.txt', usecols=(0,), delimiter=','))
totalpacketsCAIDA = sum(np.loadtxt('D:/Datasets/Attack/CAIDA/aflstathwn_prev.txt', usecols=(0,), delimiter=','))
'''totalpacketsBF = sum(np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/aflstathwn.txt', usecols=(0,), delimiter=','))
totalpacketsBotnet = sum(np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/aflstathwn.txt', usecols=(0,), delimiter=','))
totalpacketsHTTP = sum(np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/aflstathwn.txt', usecols=(0,), delimiter=','))
totalpacketsInf = sum(np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/aflstathwn.txt', usecols=(0,), delimiter=','))'''



print(totalpacketsHN)
print(totalpacketsISCX)
print(totalpacketsUNIBS)
print(totalpacketsCAIDA)
#--- ICMP
data = sum(np.loadtxt('D:/Datasets/Normal/Reduced/icmpstat.txt', usecols=(0,), delimiter=','))
data1 = sum(np.loadtxt('D:/Datasets/Normal/ISCX/icmpstat.txt', usecols=(0,), delimiter=','))
data2 = sum(np.loadtxt('D:/Datasets/Normal/UNIBS/icmpstat.txt', usecols=(0,), delimiter=','))
dataA1 = sum(np.loadtxt('D:/Datasets/Attack/CAIDA/icmpstat_prev.txt', usecols=(0,), delimiter=','))
'''dataA4 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/icmpstat.txt', usecols=(0,), delimiter=','))
dataA7= sum(np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/icmpstat.txt', usecols=(0,), delimiter=','))
dataA10= sum(np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/icmpstat.txt', usecols=(0,), delimiter=','))
dataA13= sum(np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/icmpstat.txt', usecols=(0,), delimiter=','))'''



icmp = (data/totalpacketsHN)*100
icmp1 = (data1/totalpacketsISCX)*100
icmp2 = (data2/totalpacketsUNIBS)*100
icmp3 = (dataA1/totalpacketsCAIDA)*100
'''icmp4 = (dataA4/totalpacketsBF)*100
icmp5 = (dataA7/totalpacketsBotnet)*100
icmp6 = (dataA10/totalpacketsHTTP)*100
icmp7 = (dataA13/totalpacketsInf)*100'''

print(icmp)
print(icmp1)
print(icmp2)


#--- TCP
data3 = sum(np.loadtxt('D:/Datasets/Normal/Reduced/tcpstat.txt', usecols=(0,), delimiter=','))
data4 = sum(np.loadtxt('D:/Datasets/Normal/ISCX/tcpstat.txt', usecols=(0,), delimiter=','))
data5 = sum(np.loadtxt('D:/Datasets/Normal/UNIBS/tcpstat.txt', usecols=(0,), delimiter=','))
dataA2 = sum(np.loadtxt('D:/Datasets/Attack/CAIDA/tcpstat_prev.txt', usecols=(0,), delimiter=','))
'''dataA5 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/tcpstat.txt', usecols=(0,), delimiter=','))
dataA8 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/tcpstat.txt', usecols=(0,), delimiter=','))
dataA11 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/tcpstat.txt', usecols=(0,), delimiter=','))
dataA14 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/tcpstat.txt', usecols=(0,), delimiter=','))'''

tcp = (data3/totalpacketsHN)*100
tcp1 = (data4/totalpacketsISCX)*100
tcp2 = (data5/totalpacketsUNIBS)*100
tcp3 = (dataA2/totalpacketsCAIDA)*100
'''tcp4 = (dataA5/totalpacketsBF)*100
tcp5 = (dataA8/totalpacketsBotnet)*100
tcp6 = (dataA11/totalpacketsHTTP)*100
tcp7 = (dataA14/totalpacketsInf)*100'''

print(tcp2)


#--- UDP
data6 = sum(np.loadtxt('D:/Datasets/Normal/Reduced/udpstat.txt', usecols=(0,), delimiter=','))
data7 = sum(np.loadtxt('D:/Datasets/Normal/ISCX/udpstat.txt', usecols=(0,), delimiter=','))
data8 = sum(np.loadtxt('D:/Datasets/Normal/UNIBS/udpstat.txt', usecols=(0,), delimiter=','))
dataA3 = sum(np.loadtxt('D:/Datasets/Attack/CAIDA/udpstat_prev.txt', usecols=(0,), delimiter=','))
'''dataA6 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/BruteForceSSH/udpstat.txt', usecols=(0,), delimiter=','))
dataA9 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/DDoSBotnet/udpstat.txt', usecols=(0,), delimiter=','))
dataA12 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/HTTPDDoS/udpstat.txt', usecols=(0,), delimiter=','))
dataA15 = sum(np.loadtxt('D:/Datasets/Attack/ISCX/infiltration/udpstat.txt', usecols=(0,), delimiter=','))'''

udp = (data6/totalpacketsHN)*100
udp1 = (data7/totalpacketsISCX)*100
udp2 = (data8/totalpacketsUNIBS)*100
udp3 = (dataA3/totalpacketsCAIDA)*100
'''udp4 = (dataA6/totalpacketsBF)*100
udp5 = (dataA9/totalpacketsBotnet)*100
udp6 = (dataA12/totalpacketsHTTP)*100
udp7 = (dataA15/totalpacketsInf)*100'''



ICMP = [icmp, icmp1, icmp2,icmp3]

TCP = [tcp,tcp1,tcp2,tcp3]

UDP = [udp, udp1, udp2,udp3]


## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.30                      # the width of the bars

## the bars
rects1 = ax.bar(ind, ICMP, width,
                color='#FFFFFF'
               )

rects2 = ax.bar(ind+width, TCP, width,
                    color='#C0C0C0')
	#,
                    #yerr=womenStd,
                    #error_kw=dict(elinewidth=3,ecolor='black')				
rects3 = ax.bar(ind+width+width,UDP, width,
                    color='#000000')
					

# axes and labels
ax.set_xlim(-width/2,len(ind)+width)
ax.set_ylim(0,120)
ax.set_ylabel('Packet Percentage')
#ax.set_title('Normal and Attack Datasets')
#xTickMarks = ['Home\n Network' , 'ISCX', 'UNIBS','CAIDA', 'ISCX \n Brute Force\n SSH', 'ISCX \n DDoS\n Botnet','ISCX \n HTTP\n DDoS','ISCX \n Infiltration \nfrom Inside']
xTickMarks = ['Home\n Network' , 'ISCX', 'UNIBS','CAIDA']

ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=14)



## add a legend
ax.legend( (rects1[0], rects2[0],rects3[0]), ('ICMP', 'TCP','UDP'), loc='upper left' )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%.2f' % float(height),
                ha='center', va='bottom',fontsize='12')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)




plt.show()




