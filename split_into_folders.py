import numpy as np
import pandas as pd
import os
import shutil
import sys

if __main__:
	train = pd.read_csv('./train.csv')
	print(sys.version)
	print(train.info())
	print(train.info())

	if not os.path.exists('0'):
    	os.mkdir('0')
	if not os.path.exists('1'):
	    os.mkdir('1')
	if not os.path.exists('2'):
	    os.mkdir('2')

	class_0 = train[train['class'] == 0].ID_img.values
	class_1 = train[train['class'] == 1].ID_img.values
	class_2 = train[train['class'] == 2].ID_img.values

	for file_name in class_0:
    	shutil.copy(f'./train/{file_name}', './0')
	for file_name in class_1:
	    shutil.copy(f'./train/{file_name}', './1')
	for file_name in class_2:
	    shutil.copy(f'./train/{file_name}', './2')

	print('copy done')