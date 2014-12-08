import json
import csv
import sys
from pprint import pprint
output_dir = list(sys.stdin)[0]
output_dir = output_dir[0:len(output_dir)-1]

f = open(output_dir+'/hmm_out', 'r')
rows = list(f)
MAP_seq = []
for i in range(0, len(rows)):
	if (rows[i].startswith('Distribution of values for S(@')):
		#print(rows[i+1][7])
		MAP_seq.append(int(rows[i+1][7]))
myfile = open(output_dir+'/MAP_seq', 'wb')
wr = csv.writer(myfile)
wr.writerow(MAP_seq)


#data = json.load(json_data)
#pprint(data)
#json_data.close()