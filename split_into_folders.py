import numpy as np
import pandas as pd
import os
import shutil
import sys
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--csv')
	parser.add_argument('--path')
	args = parser.parse_args()

	print(sys.version)

	train_csv_path = './train_dataset_train/train.csv'
	train_images_path = './train_dataset_train/train'

	if args is not None:
		if args.csv and args.path:
			train_csv_path = args.csv
			train_images_path = args.path

	train = pd.read_csv(train_csv_path)
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
		shutil.copy(f'{train_images_path}/{file_name}', './0')
	for file_name in class_1:
	    shutil.copy(f'{train_images_path}/{file_name}', './1')
	for file_name in class_2:
	    shutil.copy(f'{train_images_path}/{file_name}', './2')

	print('copy done')