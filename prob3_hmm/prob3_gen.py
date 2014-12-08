import csv
import sys

input_dir = list(sys.stdin)[0]
input_dir = input_dir[0:len(input_dir)-1]

rule = open('hmm_rule.blog', "r")
f = open('prob3.blog', 'w')
for line in rule:
	f.write(line)
data = open(input_dir+'/problem-3-outputs.csv')
csv_data = list(csv.reader(data))
for i  in range(1, len(csv_data)):
	f.write('obs O(@' +str(i-1) + ') = result[' + str(csv_data[i][1]) + '];\n')
for i in range(1, len(csv_data)):
	f.write('query S(@' +str(i-1) + ');\n')
