import logging
import sys
import glob, os
import numpy as np

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from collections import namedtuple
from scapy.all import *

fl_pkts = {} # Packets per flow 
fl_bytes= {} # total bytes per flow //change
fl_start = {} # Staring time of a flow
fl_end = {} # End time of a flow

tuf=namedtuple("TCPUDP",['proto', 'src', 'dst', 'sp', 'dp'])
icf=namedtuple("ICMP",['proto','src', 'dst', 'type'])

pif = (1,'','',0)# previous ICMP flow
pit = 0.0# previous ICMP packet time
ptf = (6,'','',0,0)# previous TCP flow
ptt = 0.0# previous TCP packet time
puf = (17,'','',0,0)# previous UDP flow
put = 0.0# previous UDP packet time

count = 0
def customAction(p):
	global fl_pkts, fl_start, fl_end 
	global icf, tuf
	global target
	global pif, ptf, puf, pit, ptt, put
	global count
	
	try:
		count = count + 1
		
		
		if p[0].proto == 1 and (p[0].type == 0 or p[0].type == 8):
			f = icf(1, p[0].src, p[0].dst, p[0].type)
			if not (f == pif and p[0].time == pit):
				pif = f 
				pit = p[0].time
			else:
				return
		else:
			return

		if f not in fl_start:
			fl_start[f] = p[0].time
			fl_end[f] = p[0].time
			fl_pkts[f] = 1
			fl_bytes[f] = p[0].len #change
		else:
			end_time = fl_end[f]
			time_diff = p[0].time - end_time
			if time_diff > 255:
				start_time = fl_start[f]
				fl_dur = end_time - start_time
				#line = str(f.proto)+','+f.src+','+f.dst
				#if f.proto == 1:
				#	line = line + ',' + str(f.type)
				#else:
				#	line = line + ',' + str(f.sp) + ',' + str(f.dp)
				pkt_rate = 0.0
				pkt_byte = fl_bytes[f]*1.0/fl_pkts[f] #change
				if fl_pkts[f] != 1 and fl_dur > 0.0 :
					pkt_rate = fl_pkts[f] / fl_dur
				line = str(fl_pkts[f])+','+str(fl_dur)+','+str(pkt_rate)+','+str(fl_bytes[f])+','+str(pkt_byte) #change
				#line = line +':'+str(fl_pkts[f])+','+str(fl_dur)+','+str(pkt_rate)
				#line = str(fl_pkts[f])+','+str(fl_dur)+','+str(pkt_rate)
				#target.write(line+'\n')
				if f.proto == 1: #change
					tgticmp.write(line+'\n') #change
				elif f.proto == 6: #change
					tgttcp.write(line+'\n') #change
				elif f.proto == 17: #change
					tgtudp.write(line+'\n')			 #change
				else:#change
					pass#change
				fl_pkts[f] = 0
				fl_bytes[f] = 0 #change
				fl_start[f] = p[0].time
									
			fl_pkts[f] = fl_pkts[f] + 1
			fl_bytes[f] = fl_bytes[f] + p[0].len #change
			fl_end[f] = p[0].time
	except:
		print('Error in packet: '+ str(count)+ ' source: '+ str(p[0].src) + ' destination: '+ str(p[0].dst) + ' protocol: '+ str(p[0].proto))
	

tgttcp = open('tcpstat.txt','w') #change
tgtudp = open('udpstat.txt', 'w') #change
tgticmp= open('icmpstat.txt','w')#change
filelist = ['ddostrace.20070804_141436.pcap','ddostrace.20070804_141936.pcap','ddostrace.20070804_142436.pcap',
'ddostrace.20070804_142936.pcap','ddostrace.20070804_143436.pcap','ddostrace.20070804_143936.pcap','ddostrace.20070804_144436.pcap',
'ddostrace.20070804_144936.pcap','ddostrace.20070804_145436.pcap']

for fn in filelist:
	print ('File processing: '+fn)
	sniff(offline=fn,filter="ip",store=0, prn=customAction)
	count = 0

for f in fl_start:
	fl_dur = fl_end[f] - fl_start[f]
	#line = str(f.proto)+','+f.src+','+f.dst
	#if f.proto == 1:
	#	line = line + ',' + str(f.type)
	#else:
	#	line = line + ',' + str(f.sp) + ',' + str(f.dp)
	pkt_rate = 0.0
	pkt_byte = fl_bytes[f]*1.0/fl_pkts[f] #change
	if fl_pkts[f] != 1 and fl_dur > 0.0 :
		pkt_rate = fl_pkts[f] / fl_dur
	#line = line +':'+str(fl_pkts[f])+','+str(fl_dur)+','+str(pkt_rate)
	#line = str(fl_pkts[f])+','+str(fl_dur)+','+str(pkt_rate)
	line =str(fl_pkts[f])+','+str(fl_dur)+','+str(pkt_rate)+','+str(fl_bytes[f])+','+str(pkt_byte) #change
	#target.write(line+'\n')
	if f.proto == 1: #change
		tgticmp.write(line+'\n') #change
	elif f.proto == 6: #change
		tgttcp.write(line+'\n') #change
	elif f.proto == 17:#change
		tgtudp.write(line+'\n')	#change		
	else:#change
		pass#change
