import csv
import sys

input_dir = list(sys.stdin)[0]
input_dir = input_dir[0:len(input_dir)-1]
data = open(input_dir+'/problem-2-disease-priors.csv')
csv_data = list(csv.reader(data))

filename = 'prob2.blog'
f = open(filename, "w")
f.write('random Real ToReal(Boolean disease) ~\n')
f.write('\tif disease then 1.0\n')
f.write('\telse 0.0;\n')
f.write('random Boolean disease(Integer i) ~ \n')
disease_vec = str('vstack(')
for i  in range(1, len(csv_data)):
	if (i == 1):
		line = str('\tif i == 1 then BooleanDistrib(') + str(csv_data[i][1])  + ')\n'
	elif (i == len(csv_data) - 1):
		line = str('\telse if i == ') + str(i) + ' then ' + ' BooleanDistrib(' + str(csv_data[i][1]) + ');\n'		
	else:
		line = str('\telse if i == ') + str(i) + ' then ' + ' BooleanDistrib(' + str(csv_data[i][1]) + ')\n'
	f.write(line)
	if (i != len(csv_data) - 1):
		disease_vec += str('ToReal(disease(' +str(i) +')),')
	else:
		disease_vec += str('ToReal(disease(' +str(i) +')))')

data = open(input_dir+'/problem-2-edges.csv')
csv_data = list(csv.reader(data))

f.write('random Boolean finding(Integer i) ~ \n')
edges = list()
for i in range(1, len(csv_data[0])):
	edges.append('vstack(')
	for j  in range(1, len(csv_data)):
		if (j == (len(csv_data)-1)):
			edges[i-1] += str(float(csv_data[j][i]))+')'
		else:
			edges[i-1] += str(float(csv_data[j][i]))+','
for i in range(1, len(csv_data[0])):
	if (i == 1):
		line = '\tif i == ' + str(i) + ' then NoisyOr(' + disease_vec +','+edges[i-1] + ')\n'
	elif (i == (len(csv_data[0]) -1)):
		line = '\telse if i == ' + str(i) + ' then NoisyOr(' + disease_vec +','+edges[i-1] + ');\n'
	else:
		line = '\telse if i == ' + str(i) + ' then NoisyOr(' + disease_vec +','+edges[i-1] + ')\n'
	f.write(line)
f.write('\n')

data = open(input_dir+'/problem-2-cases-findings.csv')
csv_data = list(csv.reader(data))
for i in range(1, len(csv_data)):
	if (csv_data[i][1] == '0'):
		line = 'obs finding(' +str(i) + ') = false;\n'
	else:
		line = 'obs finding(' +str(i) + ') = true;\n'
	f.write(line)
f.write('\n')
for i in range(1, len(csv_data)):
	line = 'query disease(' + str(i)+');\n'
	f.write(line)



