import csv
data = open('problem-1-data.csv')
csv_data = list(csv.reader(data))

filename = 'prob1_obs.blog'
f = open(filename, "w")
f.write('fixed RealMatrix x(Integer i) =\n')

for i  in range(1, len(csv_data)):
	if (i == 1):
		line = str('\tif i == ') + str(i) + ' then vstack('
	else:
		line = str('\telse if i == ') + str(i) + ' then vstack('
	line += csv_data[i][1] + ',' + csv_data[i][2] + ',' + csv_data[i][3] + ',' + csv_data[i][4] + ',' + csv_data[i][5] + ')\n'
	f.write(line)

f.write(';\n')
f.write('random Real y(Integer i) ~ Gaussian(transpose(w) * x(i), inverse_num(tao));\n')
for i  in range(1, len(csv_data)):
	line = str('obs y(') + str(i) + ') = ' + csv_data[i][6] + ';\n'
	f.write(line)
