import json
import csv
from pprint import pprint
f = open('out_hmm', 'r')
rows = list(f)
MAP_seq = []
for i in range(0, len(rows)):
	if (rows[i].startswith('Distribution of values for S(@')):
		#print(rows[i+1][7])
		MAP_seq.append(int(rows[i+1][7]))
myfile = open('MAP_seq2', 'wb')
wr = csv.writer(myfile)
wr.writerow(MAP_seq)
#data = json.load(json_data)
#pprint(data)
#json_data.close()