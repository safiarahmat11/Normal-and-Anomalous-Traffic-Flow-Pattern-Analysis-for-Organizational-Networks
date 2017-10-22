import logging
import sys
import glob, os
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from collections import namedtuple
from scapy.all import *

time = 0.0
fdfl = {}
fdfc = {}

tuf=namedtuple("TCPUDP",['proto', 'src', 'dst', 'sp', 'dp'])
icf=namedtuple("ICMP",['proto','src', 'dst', 'type'])
pktcnt = 0
base = 0.0

target = open('adstiscx.txt','w')

def customAction(p):
	global fdfl, fdfc 
	global icf, tuf
	global time, pktcnt
	global target
	try:
		pktcnt = pktcnt + 1
		if pktcnt == 1:
			time = p[0].time + 60.0
	
		if p[0].time > time :
			for k in fdfc:
				line = str(fdfc[k])
				target.write(k+':'+line+'\n')
			fdfc = {}
			fdfl = {}
			time = time + 60.0
			

		if p[0].proto == 1 and (p[0].type == 0 or p[0].type == 8):
			f = icf(1, p[0].src, p[0].dst, p[0].type)
			dst = p[0].dst
			if dst in fdfl:
				if not (f in fdfl[dst]):
					fdfl[dst].append(f)
					fdfc[dst] = fdfc[dst] + 1
			else:
				fdfl[dst] = []
				fdfl[dst].append(f)
				fdfc[dst] = 1

	except:
		print('Error in packet: '+ str(pktcnt)+ ' source: '+ str(p[0].src) + ' destination: '+ str(p[0].dst))

filelist = ['ddostrace.20070804_141436.pcap','ddostrace.20070804_141936.pcap','ddostrace.20070804_142436.pcap',
'ddostrace.20070804_142936.pcap','ddostrace.20070804_143436.pcap','ddostrace.20070804_143936.pcap','ddostrace.20070804_144436.pcap',
'ddostrace.20070804_144936.pcap','ddostrace.20070804_145436.pcap']
for fn in filelist:
	print ('File processing: '+fn)
	sniff(offline=fn,filter="ip",store=0, prn=customAction)
	for k in fdfc:
		line = str(fdfc[k])
		target.write(k+':'+line+'\n')
	fdfc = {}
	fdfl = {}
	pktcnt = 0
target.close()
