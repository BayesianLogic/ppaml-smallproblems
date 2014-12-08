import csv
import sys

input_dir = list(sys.stdin)[0]
input_dir = input_dir[0:len(input_dir)-1]

data = open(input_dir+'/problem-1-data.csv')
csv_data = list(csv.reader(data))


filename = 'prob1.blog'
f = open(filename, "w")
f.write('fixed RealMatrix sigma1 =  diag(vstack(2.0,2.0,2.0,2.0,2.0));\n')
f.write('random RealMatrix Mu ~ MultivarGaussian(vstack(0.0,0.0,0.0,0.0,0.0), sigma1);\n')
f.write('fixed RealMatrix sigma2 = eye(5);\n')
f.write('random RealMatrix inversesigma_prior ~ InverseWishart(sigma2, 5);\n')
f.write('random RealMatrix w ~ MultivarGaussian(Mu, inversesigma_prior);\n')
f.write('fixed Real inverse_num(Real origin_num) = 1.0 / origin_num;\n')
f.write('random Real tao ~ Gamma(0.5, 2.0);\n')

f.write('fixed RealMatrix x(Integer i) =\n')

for i  in range(1, len(csv_data)):
	if (i == 1):
		line = str('\tif i == ') + str(i) + ' then vstack('
	else:
		line = str('\telse if i == ') + str(i) + ' then vstack('

	line += str(float(csv_data[i][1])) + ',' + str(float(csv_data[i][2])) + ',' + str(float(csv_data[i][3])) + ',' + str(float(csv_data[i][4])) + ',' + str(float(csv_data[i][5])) + ')\n'
	f.write(line)

f.write(';\n')
f.write('random Real y(Integer i) ~ Gaussian(det(transpose(w) * x(i)), inverse_num(tao));\n')
for i  in range(1, len(csv_data)):
	line = str('obs y(') + str(i) + ') = ' + csv_data[i][6] + ';\n'
	f.write(line)

f.write('query(w);\n')
