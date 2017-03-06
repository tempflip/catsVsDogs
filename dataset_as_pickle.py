from scipy import misc
import os
import pickle

train_dir = './train/'
test_dir = './test/'

train_x = []
train_y = []
test_y = []

c = 0
for f in os.listdir(train_dir):
	label = f[0:3]
	im = misc.imresize(misc.imread(train_dir + f), (32,32))
	train_x.append(im)
	if (label == 'cat') : train_y.append(1)
	else : train_y.append(0)
	#c+= 1
	#if c > 100 : break

d = {'train_x' : train_x, 'train_y' : train_y}

pickle.dump(d, open("train_data.p", "wb"))

